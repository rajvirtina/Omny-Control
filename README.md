Omny-Control

To use the library, first install the required dependencies using the following command in the command prompt:

Python -m pip install -U Selenium

After importing the project, select the interpreter and install the following libraries:

Selenium
pytest
pytest-html
pytest-xdist
pytest-order
pytest-ordering
pytest-order-modify
pytest-metadata
openpyxl
allure-pytest
allure-python-commons

To execute a single test case, use the following command in the terminal:

pytest -v --browser chrome testCases/specificTestName.py --html=Reports/report.html

To execute all test cases at once, use the following command in the terminal:

pytest -v --browser chrome testCases/ --html=Reports/report.html
