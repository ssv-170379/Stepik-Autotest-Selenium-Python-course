#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time, math, pyperclip # https://stepik.org/lesson/184253/step/2?discussion=1038936&unit=158843

try: 
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/explicit_wait2.html') # Открыть страницу http://suninjuly.github.io/explicit_wait2.html.

	WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), "100") # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
	)

	browser.find_element_by_css_selector('button#book').click() # Нажать на кнопку "Book"

	# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
	x = int(browser.find_element_by_css_selector('#input_value').text) # Считать значение для переменной x.
	result = math.log(abs(12*math.sin(x))) # Посчитать математическую функцию от x.
	browser.find_element_by_css_selector('#answer').send_keys(str(result)) # Ввести ответ в текстовое поле.
	browser.find_element_by_css_selector('button#solve').click() # Нажать на кнопку "Submit".

	answer = browser.switch_to.alert.text.split()[-1]
	pyperclip.copy(answer)
	print(f'The answer "{answer}" is copied to your clipboard')

finally:
	time.sleep(10) # ожидание чтобы визуально оценить результаты прохождения скрипта
	browser.quit() # закрываем браузер после всех манипуляций
