from os import system

import pytest
from selenium import webdriver

import time
import math

links=(
'https://stepik.org/lesson/236895/step/1', 
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1')

@pytest.fixture(scope="function")
def browser():
	browser = webdriver.Chrome() # start browser for test.
	browser.implicitly_wait(5) # говорим WebDriver искать нужный элемент в течение 5 секунд
	yield browser
	browser.quit() # quit browser.

@pytest.mark.parametrize('link', links)
def test_aliens_riddle(browser, link):
	browser.get(link)
	element = browser.find_element_by_css_selector('textarea.string-quiz__textarea')
	result = math.log(int(time.time()))
	element.send_keys(str(result))
	browser.find_element_by_css_selector('button.submit-submission').click()

	message_part = browser.find_element_by_css_selector('pre.smart-hints__hint').text
	if message_part != 'Correct!': print (message_part)
	assert message_part == 'Correct!', f'The secret message is: {message_part}'

def main():
	system(f'pytest -s -v "{__file__}"')
if __name__ == "__main__":
	main()
