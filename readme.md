
pip install pytest allure-pytest

pytest --alluredir=results tests/test_script.py

allure serve results
