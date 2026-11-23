from nbresult import ChallengeResultTestCase


class TestFinalModel(ChallengeResultTestCase):
    def test_score_improvement(self):
        self.assertGreater(
            self.result.multiple_score,
            self.result.single_score,
            "Multiple features should improve score")
        self.assertGreater(self.result.score_improvement, 0.05,
                           "Score should improve by at least 0.05")

    def test_multiple_score_range(self):
        self.assertGreater(self.result.multiple_score, 0.6,
                           "Score with multiple features should exceed 0.6")
        self.assertLess(self.result.multiple_score, 0.85,
                        "Score should be less than 0.85")

    def test_new_player_dataframe(self):
        self.assertEqual(self.result.new_df_shape[0], 1,
                         "New player DataFrame should have 1 row")
        self.assertGreaterEqual(
            self.result.new_df_shape[1],
            4,
            "New player DataFrame should have at least 4 required features")

    def test_prediction_reasonable(self):
        self.assertGreater(self.result.new_player_prediction, -10,
                           "Prediction should be greater than -10")
        self.assertLess(
            self.result.new_player_prediction,
            10,
            "Prediction should be less than 10 (scaled prediction)")

    def test_prediction_not_astronomical(self):
        # This catches the common mistake of forgetting to scale
        self.assertLess(abs(self.result.new_player_prediction), 100,
                        "Did you remember to scale the new player data?")

    def test_single_score_not_suspiciously_high(self):
        """Defensive check: Detect if model was evaluated on training data"""
        score = self.result.single_score
        self.assertLess(
            score, 0.95, f"Score of {score:.3f} is suspiciously high. "
            f"Did you evaluate on training data? Use: model.score(X_test_scaled, y_test)")

    def test_multiple_score_not_suspiciously_high(self):
        """Defensive check: Detect if model was evaluated on training data"""
        score = self.result.multiple_score
        self.assertLess(
            score, 0.95, f"Score of {score:.3f} is suspiciously high. "
            f"Did you evaluate on training data? Use: model.score(X_test_scaled, y_test)")

    def test_single_score_suggests_scaled_training(self):
        """Defensive check: Low score may indicate training on unscaled data"""
        score = self.result.single_score
        self.assertGreater(
            score, 0.30, f"Score of {score:.3f} is very low. "
            f"Did you train on unscaled data? Use: model.fit(X_train_scaled, y_train)")
