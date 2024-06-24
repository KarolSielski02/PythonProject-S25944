import pandas as pd


class DataAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def select_fields_data(data, columns):
        return data[columns]

    @staticmethod
    def filter_data(data, column, value):
        return data[data[column] == value]

    @staticmethod
    def sort_data(data, column):
        return data.sort_values(by=column)

    @staticmethod
    def sort_data_ascending(data, is_ascending=True):
        return data.sort_values(ascending=is_ascending)

    @staticmethod
    def remove_na_from_column(data, column_name):
        if column_name in data.columns:
            data = data.dropna(subset=[column_name])
        else:
            print(f"No such column named {column_name}")
        return data

    @staticmethod
    def convert_categorical_to_numeric(data, column):
        data[column] = pd.factorize(data[column])[0]

    @staticmethod
    def group_by_column_count(data, group_by_column, count_column):
        return data.groupby(group_by_column)[count_column].count()

    @staticmethod
    def create_age_groups(data, age_bins):
        data.loc[:, 'age_group'] = pd.cut(data['age'], bins=age_bins, right=False, labels=[f"{(i+10)}" for i in age_bins[:-1]])
        return data

    @staticmethod
    def group_and_count(data, group_by_columns, count_column):
        grouped_data = data.groupby(group_by_columns, observed=False)[count_column].size().unstack(fill_value=0)
        return grouped_data

    @staticmethod
    def calculate_averages(data, columns):
        averages = []
        for column in columns:
            if column in data.columns:
                try:
                    average = data[column].mean()
                    if column == "stroke":
                        column = "parent_had_stroke(per 100 people)"
                        average *= 100
                    averages.append({'Column': column, 'Average': average})
                except TypeError:
                    averages.append({'Column': column, 'Error': "Contains non-numeric data"})
            else:
                averages.append({'Column': column, 'Error': "Does not exist"})
        return pd.DataFrame(averages)

    @staticmethod
    def calculate_gender_distribution(data):
        gender_counts = data['gender'].value_counts()
        gender_distribution = (gender_counts / len(data)) * 100
        return pd.DataFrame({
            'Gender': gender_distribution.index,
            'Percentage': gender_distribution.values
        })

    @staticmethod
    def compute_risk_score(data):
        weights = {
            'age': 0.3,
            'hypertension': 2,
            'heart_disease': 2,
            'avg_glucose_level': 0.1,
            'bmi': 0.05,
            'smoking_status': {
                'never smoked': 1,
                'formerly smoked': 1.5,
                'smokes': 2,
                'unknown': 0
            }
        }

        # Normalizacja
        data['normalized_age'] = data['age'] / 100
        data['normalized_glucose'] = data['avg_glucose_level'] / 200
        data['normalized_bmi'] = data['bmi'] / 50

        # Wyliczanie riskScore
        data['risk_score'] = (
                data['normalized_age'] * weights['age'] +
                data['hypertension'] * weights['hypertension'] +
                data['heart_disease'] * weights['heart_disease'] +
                data['normalized_glucose'] * weights['avg_glucose_level'] +
                data['normalized_bmi'] * weights['bmi']
        )

        # dodanie riskScore związanego z paleniem
        data['risk_score'] += data['smoking_status'].map(weights['smoking_status'])

        # dodanie risk_score_level czyli labelki w zaleznosci od score
        data['risk_score_level'] = pd.cut(
            data['risk_score'],
            bins=[0, 2.5, 4, float('inf')],
            labels=['Low', 'Medium', 'High'],
            right=False
        )

        return data[['id', 'risk_score', 'risk_score_level']]
