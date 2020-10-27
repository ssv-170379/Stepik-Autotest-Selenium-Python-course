import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options # Needed to select language for Chrome browser.

def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default='Chrome', help="Choose browser (Chrome by default): Chrome or Firefox.")
	parser.addoption('--language', action='store', default='en', help="Set browser language (en by default), two-letter, see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes.")

@pytest.fixture(scope="function")
def browser(request):
	browser_name = request.config.getoption("browser_name").capitalize()
	user_language = request.config.getoption("language").lower()
	print(f'\nStarting browser "{browser_name}" with "{user_language}" language.')
	if browser_name == "Chrome":
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
		browser = webdriver.Chrome(options=options)
#		browser = webdriver.Chrome() # если не нужно выбирать язык - достаточно этой строки
	elif browser_name == "Firefox":
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		browser = webdriver.Firefox(firefox_profile=fp)
		#browser = webdriver.Firefox() # если не нужно выбирать язык - достаточно этой строки
	else:
		print(f'\nWhoopsie! {browser_name} browser is not supported. Starting Chrome instead.')
		browser = webdriver.Chrome()
#		raise pytest.UsageError("--browser_name should be chrome or firefox") # вариант без фолбека к хрому, просто кидаем ошибку, если неизвестный браузер.
	yield browser
	print('\nBrowser shutdown.')
	browser.quit()

