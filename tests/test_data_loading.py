from nbresult import ChallengeResultTestCase


class TestDataLoading(ChallengeResultTestCase):
    def test_df_shape(self):
        self.assertEqual(
            self.result.df_shape[0],
            4000,
            "Hint: DataFrame should have 4000 rows")
        self.assertGreaterEqual(
            self.result.df_shape[1],
            6,
            "Hint: DataFrame should have at least 6 columns")

    def test_df_columns(self):
        required_columns = [
            'season',
            'poss',
            'mp',
            'do_ratio',
            'pacing',
            'win_rating']
        self.assertTrue(all(col in self.result.df_columns for col in required_columns),
                        f"Hint: DataFrame must contain these columns: {required_columns}. Extra columns are fine!")
