import unittest
import os
import pandas as pd
from sqlalchemy import create_engine

class TestFoodHabitAnalysis(unittest.TestCase):
    def setUp(self):
        self.db_path = "../data/resturnent.sqlite"
        self.expected_columns = [
            'name', 'city', 'state', 'zipcode', 'country', 'cuisines',
            'pickup_enabled', 'delivery_enabled', 'weighted_rating_value',
            'aggregated_rating_count'
        ]
        self.expected_row_count = 1500
        self.engine = create_engine(f"sqlite:///{self.db_path}")

    def test_column_names(self):
        query = "SELECT * FROM restaurants LIMIT 1;"
        df = pd.read_sql(query, con=self.engine)
        actual_columns = df.columns.tolist()
        self.assertListEqual(actual_columns, self.expected_columns)

    def test_row_count(self):
        query = "SELECT COUNT(*) AS row_count FROM restaurants;"
        result = self.engine.execute(query).fetchone()
        actual_row_count = result["row_count"]
        self.assertEqual(actual_row_count, self.expected_row_count)

if __name__ == "_main_":
    unittest.main()
    