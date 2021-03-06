#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
import time, math, pyperclip # https://stepik.org/lesson/184253/step/2?discussion=1038936&unit=158843
try: 
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/redirect_accept.html') # Открыть страницу http://suninjuly.github.io/redirect_accept.html.

	browser.find_element_by_css_selector('button.btn').click() # Нажать на кнопку (откроется новая вкладка).

	browser.switch_to.window(browser.window_handles[1]) # Переключиться на новую вкладку (window_handles возвращает массив имён всех вкладок)

	# Пройти капчу для робота и получить число-ответ
	x = int(browser.find_element_by_css_selector('#input_value').text) # Считать значение для переменной x.
	result = math.log(abs(12*math.sin(x))) # Посчитать математическую функцию от x.
	browser.find_element_by_css_selector('#answer').send_keys(str(result)) # Ввести ответ в текстовое поле.
	browser.find_element_by_css_selector('button.btn').click() # Нажать на кнопку "Submit".

	answer = browser.switch_to.alert.text.split()[-1]
	pyperclip.copy(answer)
	print(f'The answer "{answer}" is copied to your clipboard')

finally:
	time.sleep(10) # ожидание чтобы визуально оценить результаты прохождения скрипта
	browser.quit() # закрываем браузер после всех манипуляций
