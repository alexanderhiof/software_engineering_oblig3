# Oblig 3 Software engineering and testing

1. Generated .github/workflows/python.yml

```yml
name: Python package

on: [push]

jobs:
  build:

    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest]
        python-version: ["3.7", "3.8", "3.9", "3.10"]

    steps:
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Lint with flake8
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
      - name: Test with pytest
        run: |
          pytest
```


2. Made it install pytest and flake8 for code linting
3. Added file from previous Oblig and the tests ran successfully
```
Run pytest
============================= test session starts ==============================
platform linux -- Python 3.8.14, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/runner/work/software-engineering-testing/software-engineering-testing
collected 4 items

test_oblig2.py ....                                                      [100%]

============================== 4 passed in 0.01s ===============================
```

Sources:
https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python - Building and testing Python
