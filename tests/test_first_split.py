from nbresult import ChallengeResultTestCase


class TestFirstSplit(ChallengeResultTestCase):
    def test_train_test_sizes(self):
        # Check 75/25 split
        total = self.result.X_train_shape[0] + self.result.X_test_shape[0]
        self.assertAlmostEqual(
            self.result.X_train_shape[0] /
            total,
            0.75,
            places=1,
            msg="Training set should be ~75% of data")
        self.assertAlmostEqual(
            self.result.X_test_shape[0] /
            total,
            0.25,
            places=1,
            msg="Test set should be ~25% of data")

    def test_single_feature(self):
        # More flexible: allow students to explore but check they're selecting
        # features intentionally
        self.assertGreaterEqual(
            self.result.X_train_shape[1],
            1,
            "X should have at least 1 feature (mp)")
        self.assertGreaterEqual(
            self.result.X_test_shape[1],
            1,
            "X should have at least 1 feature (mp)")
        self.assertLessEqual(
            self.result.X_train_shape[1],
            3,
            "X should be a focused feature selection for this exercise")

    def test_y_lengths_match(self):
        self.assertEqual(
            self.result.X_train_shape[0],
            self.result.y_train_len,
            "y_train length should match X_train")
        self.assertEqual(
            self.result.X_test_shape[0],
            self.result.y_test_len,
            "y_test length should match X_test")

    def test_scaling_applied(self):
        self.assertEqual(
            self.result.X_train_scaled_shape,
            self.result.X_train_shape,
            "Scaled data should have same shape as original")
        self.assertEqual(
            self.result.X_test_scaled_shape,
            self.result.X_test_shape,
            "Scaled data should have same shape as original")
