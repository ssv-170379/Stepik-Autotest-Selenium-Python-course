#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
import time, math
try: 
	link = 'http://suninjuly.github.io/math.html'
	browser = webdriver.Chrome()
	browser.get(link) # Открыть страницу http://suninjuly.github.io/math.html.

	x_element = browser.find_element_by_css_selector('#input_value')
	x = int(x_element.text) # Считать значение для переменной x.
	y = math.log(abs(12*math.sin(x))) # Посчитать математическую функцию от x (код для этого приведён ниже).

	field = browser.find_element_by_css_selector('#answer')
	field.send_keys(str(y)) # Ввести ответ в текстовое поле.

	im_robot = browser.find_element_by_css_selector('#robotCheckbox')
	im_robot.click() # Отметить checkbox "I'm the robot".
	robots_rule = browser.find_element_by_css_selector('#robotsRule')
	robots_rule.click() # Выбрать radiobutton "Robots rule!".
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click() # Нажать на кнопку Submit.

finally:
	time.sleep(10) # ожидание чтобы визуально оценить результаты прохождения скрипта
	browser.quit() # закрываем браузер после всех манипуляций
