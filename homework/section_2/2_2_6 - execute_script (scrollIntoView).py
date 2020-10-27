#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
import time, math
try: 
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/execute_script.html') # Открыть страницу http://SunInJuly.github.io/execute_script.html.

	x = int(browser.find_element_by_css_selector('#input_value').text) # Считать значение для переменной x.
	result = math.log(abs(12*math.sin(x))) # Посчитать математическую функцию от x.

	element = browser.find_element_by_css_selector('#answer')
	browser.execute_script("return arguments[0].scrollIntoView(true);", element) # Проскроллить страницу вниз.

	browser.find_element_by_css_selector('#answer').send_keys(str(result)) # Ввести ответ в текстовое поле.
	browser.find_element_by_css_selector('#robotCheckbox').click() # Выбрать checkbox "I'm the robot".
	browser.find_element_by_css_selector('#robotsRule').click() # Переключить radiobutton "Robots rule!".
	browser.find_element_by_css_selector('button.btn').click() # Нажать на кнопку "Submit".

	answer = browser.switch_to.alert.text
	print(answer.split()[-1])

finally:
	time.sleep(10) # ожидание чтобы визуально оценить результаты прохождения скрипта
	browser.quit() # закрываем браузер после всех манипуляций
