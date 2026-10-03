# LAB1 — MLOps (IE-7374)

Lab 1 submission: virtual environment, repository/folder structure, a geometry
module, pytest + unittest test suites, and two GitHub Actions workflows.

## Structure

```
mlops-lab1/
├── .github/workflows/
│   ├── pytest_action.yml      # CI: runs pytest, uploads JUnit XML report
│   └── unittest_action.yml    # CI: runs python -m unittest test.test_unittest
├── data/                      # project data files
├── src/
│   └── shapes.py              # area calculations
├── test/
│   ├── test_pytest.py         # pytest tests (incl. a parametrized example)
│   └── test_unittest.py       # unittest.TestCase tests
├── .gitignore                 # ignores lab_01/ virtualenv, caches, reports
├── requirements.txt
└── README.md
```

## Functions in `src/shapes.py`

| Function | Behaviour |
|---|---|
| `rectangle_area(length, width)` | area of a rectangle, `length * width` |
| `triangle_area(base, height)` | area of a triangle, `0.5 * base * height` |
| `circle_area(radius)` | area of a circle, `pi * radius ** 2` |
| `total_area(a1, a2, a3)` | sum of the three areas above |

The three area functions raise `ValueError` if an input is not a number or is
negative.

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
