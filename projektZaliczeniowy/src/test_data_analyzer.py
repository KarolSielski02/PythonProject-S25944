import unittest
import pandas as pd
from data_analyzer import DataAnalyzer


class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'age': [25, 35, 45, 55],
            'gender': ['Male', 'Female', 'Female', 'Male'],
            'hypertension': [1, 0, 1, 0],
            'heart_disease': [0, 1, 0, 1],
            'avg_glucose_level': [85.1, 89.5, 77.3, 88.1],
            'bmi': [23.1, 28.5, 31.4, 22.8],
            'smoking_status': ['never smoked', 'smokes', 'formerly smoked', 'unknown'],
            'stroke': [1, 0, 1, 0]
        })

    def test_select_fields_data(self):
        result = DataAnalyzer.select_fields_data(self.data, ['id', 'age'])
        self.assertTrue('id' in result.columns and 'age' in result.columns and len(result.columns) == 2)

    def test_filter_data(self):
        result = DataAnalyzer.filter_data(self.data, 'gender', 'Female')
        self.assertEqual(len(result), 2)

    def test_sort_data(self):
        sorted_data = DataAnalyzer.sort_data(self.data, 'age')
        self.assertTrue(list(sorted_data['age']), [25, 35, 45, 55])

    def test_remove_na_from_column(self):
        self.data.loc[2, 'bmi'] = pd.NA
        result = DataAnalyzer.remove_na_from_column(self.data, 'bmi')
        self.assertEqual(result.isna().sum()['bmi'], 0)
        self.assertEqual(len(result), 3)

    def test_calculate_averages(self):
        result = DataAnalyzer.calculate_averages(self.data, ['age', 'bmi', 'stroke'])
        expected_result = pd.DataFrame([
            {'Column': 'age', 'Average': 40.0},
            {'Column': 'bmi', 'Average': 26.45},
            {'Column': 'parent_had_stroke(per 100 people)', 'Average': 50.0}
        ])
        pd.testing.assert_frame_equal(result, expected_result)

    def test_calculate_gender_distribution(self):
        result = DataAnalyzer.calculate_gender_distribution(self.data)
        self.assertAlmostEqual(result.loc[result['Gender'] == 'Female', 'Percentage'].values[0], 50.0)

    def test_compute_risk_score(self):
        result = DataAnalyzer.compute_risk_score(self.data)
        self.assertIn('risk_score', result.columns)
        self.assertIn('risk_score_level', result.columns)


if __name__ == '__main__':
    unittest.main()