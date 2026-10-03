# LAB1 — MLOps (IE-7374)

Lab 1 submission: virtual environment, repository/folder structure, `calculator.py`,
pytest + unittest test suites, and two GitHub Actions workflows.

## Structure

```
mlops-lab1/
├── .github/workflows/
│   ├── pytest_action.yml      # CI: runs pytest, uploads JUnit XML report
│   └── unittest_action.yml    # CI: runs python -m unittest test.test_unittest
├── data/                      # project data files
├── src/
│   └── calculator.py          # fun1..fun4
├── test/
│   ├── test_pytest.py         # pytest tests (incl. a parametrized example)
│   └── test_unittest.py       # unittest.TestCase tests
├── .gitignore                 # ignores lab_01/ virtualenv, caches, reports
├── requirements.txt
└── README.md
```

## Functions in `src/calculator.py`

| Function | Behaviour |
|---|---|
| `fun1(x, y)` | adds `x` and `y` |
| `fun2(x, y)` | subtracts `y` from `x` |
| `fun3(x, y)` | multiplies `x` and `y` |
| `fun4(x, y, z)` | returns the sum of the three results |

`fun1`–`fun3` raise `ValueError` if either input is not a number.

## Setup

```
python -m venv lab_01
lab_01\Scripts\activate          # Windows
source lab_01/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

## Running the tests

```
pytest                                  # pytest suite
python -m unittest test.test_unittest   # unittest suite
```

Both suites are also run automatically by GitHub Actions on every push and pull
request to `main`.
