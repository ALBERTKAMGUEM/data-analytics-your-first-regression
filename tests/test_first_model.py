from nbresult import ChallengeResultTestCase


class TestFirstModel(ChallengeResultTestCase):
    def test_model_type(self):
        self.assertEqual(self.result.model_type, "LinearRegression",
                         "Should use LinearRegression model")

    def test_score_range(self):
        self.assertGreater(self.result.single_score, 0.5,
                           "Score should be greater than 0.5")
        self.assertLess(self.result.single_score, 0.6,
                        "Score should be less than 0.6")

    def test_score_approximate(self):
        self.assertAlmostEqual(self.result.single_score, 0.54, places=1,
                               msg="Score should be approximately 0.54")
