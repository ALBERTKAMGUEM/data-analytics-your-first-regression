# Introduction

## 📁 Setup

To make challenge completion simpler, we have added terminal instructions to challenges that have test suites.

If you haven't already, **copy the terminal instructions at the top of this page and run them in your terminal**.

When you first run the challenge setup, all tests will fail. This is expected - you haven't written any code yet.

## Jupyter Notebooks

**📍 In your terminal**, run this command to start Jupyter:

```bash
jupyter notebook your_first_regression.ipynb
```

## Common Test Patters for Machine Learning - 🚧 READ THIS 🚧

Tests check specific **variables** in your code to ensure you've completed the required steps. For example, a test might check:

- That a variable called `df` exists and contains data
- That `X_train` has the correct shape
- That your model produces reasonable predictions

**Important:** Follow the variable names specified in the instructions. If the instructions say "store your result in `model`", the test will look for a variable called exactly `model`.

Typical test patterns for Machine Learning:

- **Shape checks:** `AssertionError: Expected shape (100, 4), got (100, 3)` → You're missing a column or row
-- **Type checks:** `AssertionError: Expected DataFrame, got ndarray` → Convert your data structure
-- **Existence checks:** `AttributeError: 'ChallengeResult' object has no attribute 'model'` → You didn't create or didn't name a required variable
-- **Value checks:** `AssertionError: Score should be between 0 and 1` → Check your calculation logic

### When you're finished with the challenge:

1. **Save your notebook** (File → Save in Jupyter, or `Cmd/Ctrl + S`)
2. Go back to the terminal tab where Jupyter is running
3. Press `Ctrl + C` to stop the Jupyter server
4. You'll see a message asking: `Shutdown this notebook server (y/[n])?`
5. Type `y` and press Enter to confirm

## 🚀 Test Your Solution

After completing the exercises in your notebook:

**📍 In your terminal** (use your second terminal tab - keep Jupyter running in the first), run:

```bash
make
```

This will run all tests and show you which parts are complete and which need more work. If you passed all tests in the notebook, this should be all green.

If your result is all green here, but you don't see it reflected on Kitt:

```bash
git add .
git commit -m "Committing everything"
git push
```
