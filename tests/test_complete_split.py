from nbresult import ChallengeResultTestCase


class TestCompleteSplit(ChallengeResultTestCase):
    def test_four_features(self):
        self.assertGreaterEqual(self.result.X_train_shape[1], 4,
                                "Should have at least 4 features")
        self.assertGreaterEqual(self.result.X_test_shape[1], 4,
                                "Should have at least 4 features")

    def test_correct_features(self):
        required_features = ['poss', 'mp', 'do_ratio', 'pacing']
        self.assertTrue(all(feat in self.result.feature_names for feat in required_features),
                        f"X must include these features: {required_features}. Extra features are okay!")

    def test_scaling_shape(self):
        self.assertEqual(
            self.result.X_train_scaled_shape,
            self.result.X_train_shape,
            "Scaled data should preserve shape")

    def test_X_is_2D_array(self):
        """Defensive check: Detect if X and y were swapped in train_test_split"""
        self.assertEqual(
            len(self.result.X_train_shape),
            2,
            f"X_train should be 2D (rows, columns), got shape {self.result.X_train_shape}. "
            f"Did you swap X and y? Should be: train_test_split(X, y, ...)"
        )
        self.assertEqual(
            len(self.result.X_test_shape),
            2,
            f"X_test should be 2D (rows, columns). Did you swap X and y in train_test_split?"
        )
