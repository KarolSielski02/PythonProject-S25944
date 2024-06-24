import matplotlib.pyplot as plt
import seaborn as sns
from data_analyzer import DataAnalyzer

class DataVisualizer:
    data_analyzer = DataAnalyzer()

    def __init__(self, data):
        self.data = data

    def bar_diagram_of_strokes_per_age(self):
        diagram_data = self.data_analyzer.select_fields_data(self.data, ["age", "id"])
        diagram_data = self.data_analyzer.group_by_column_count(diagram_data, "age", "id")
        diagram_data = self.data_analyzer.sort_data_ascending(diagram_data)

        fig, ax = plt.subplots(figsize=(20, 10))
        diagram_data.plot(kind='bar', ax=ax)
        ax.set_title("Age vs Number of cases")
        ax.set_xlabel('Age')
        ax.set_ylabel('Number of cases')
        return fig

    def pie_of_strokes_per_smoker(self):
        diagram_data = self.data_analyzer.select_fields_data(self.data, ["smoking_status", "id"])
        diagram_data = self.data_analyzer.group_by_column_count(diagram_data, "smoking_status", "id")

        fig, ax = plt.subplots()
        ax.pie(diagram_data, labels=["Unknown", "formerly smoked", "never smoked", "smokes"], autopct='%1.1f%%')
        return fig

    def line_of_man_vs_woman_per_age(self):
        age_bins = range(0, 101, 10)
        diagram_data = self.data_analyzer.create_age_groups(self.data, age_bins)
        diagram_data = self.data_analyzer.group_and_count(diagram_data, ['age_group', 'gender'], count_column='gender')

        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(diagram_data.index, diagram_data['Male'], linestyle='-', color='b', label='Male')
        ax.plot(diagram_data.index, diagram_data['Female'], linestyle='-', color='g', label='Female')
        ax.set_xlabel('Age Group')
        ax.set_ylabel('Number of Strokes')
        ax.set_title('Number of Strokes by Age Group and Gender')
        ax.legend()
        ax.grid(True)
        return fig

    def over_dated_heatmap_bmi_age_glucose_correlation(self):
        columns = ['bmi', 'age', 'avg_glucose_level', 'hypertension', 'heart_disease']
        diagram_data = self.data_analyzer.select_fields_data(self.data, columns)
        matrix = diagram_data.corr()

        fig, ax = plt.subplots(figsize=(20, 10))
        sns.heatmap(matrix, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={'size': 12}, ax=ax)
        ax.set_title('Correlation Heatmap for BMI, Age, and Avg Glucose Level', fontsize=16)
        return fig

    def scatter_plot(self, x_field, y_field):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(self.data[x_field], self.data[y_field], alpha=0.5)
        ax.set_xlabel(x_field.replace('_', ' ').title())
        ax.set_ylabel(y_field.replace('_', ' ').title())
        ax.set_title(f'Scatter Plot of {x_field.replace("_", " ").title()} vs {y_field.replace("_", " ").title()}')
        ax.grid(True)
        return fig

    def plot_work_type_distribution(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        self.data['work_type'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, ax=ax)
        ax.set_ylabel('')
        ax.set_title('Work Type Distribution')
        return fig

    def plot_residence_type_distribution(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x='Residence_type', data=self.data, ax=ax)
        ax.set_xlabel('Residence Type')
        ax.set_ylabel('Count')
        ax.set_title('Residence Type Distribution')
        return fig

    def plot_marital_status_by_gender(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x='ever_married', hue='gender', data=self.data, ax=ax)
        ax.set_xlabel('Marital Status')
        ax.set_ylabel('Count')
        ax.set_title('Marital Status by Gender')
        return fig

    def plot_pair_plot(self, fields, hue=None):
        g = sns.pairplot(self.data[fields], height=4, aspect=1.5, hue=hue)
        g.fig.suptitle('Pair Plot of Selected Fields', y=1.02)
        return g.fig

    def count_average_year_of_columns(self, columns):
        result_df = self.data_analyzer.calculate_averages(self.data, columns)
        return result_df

    def print_gender_distribution(self):
        gender_df = self.data_analyzer.calculate_gender_distribution(self.data)
        return gender_df

    def calculate_risk_score(self):
        df = self.data_analyzer.compute_risk_score(self.data)
        df = self.data_analyzer.sort_data(df, "risk_score")
        df = self.data_analyzer.remove_na_from_column(df, "risk_score")
        return df