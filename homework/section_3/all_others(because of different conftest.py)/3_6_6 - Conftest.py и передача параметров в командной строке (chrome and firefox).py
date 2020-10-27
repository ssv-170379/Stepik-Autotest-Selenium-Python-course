from os import system

import pytest
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

def test_browser_selection(browser):
	browser.get("https://what-is-my.com/browser/version/")

def main():
	system(f'pytest -s -v --browser_name=chrome "{__file__}"')
	system(f'pytest -s -v --browser_name=firefox "{__file__}"')
if __name__ == "__main__":
	main()
