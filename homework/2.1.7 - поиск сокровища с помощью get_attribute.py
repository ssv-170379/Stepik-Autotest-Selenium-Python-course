#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
import time, math
try: 
	link = 'http://suninjuly.github.io/get_attribute.html'
	browser = webdriver.Chrome()
	browser.get(link) # Открыть страницу http://suninjuly.github.io/get_attribute.html.

	chest = browser.find_element_by_css_selector('#treasure') # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
	x = int(chest.get_attribute('valuex')) # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
	y = math.log(abs(12*math.sin(x))) # Посчитать математическую функцию от x (сама функция остаётся неизменной).

	field = browser.find_element_by_css_selector('#answer')
	field.send_keys(str(y)) # Ввести ответ в текстовое поле.

	im_robot = browser.find_element_by_css_selector('#robotCheckbox')
	im_robot.click() # Отметить checkbox "I'm the robot".
	robots_rule = browser.find_element_by_css_selector('#robotsRule')
	robots_rule.click() # Выбрать radiobutton "Robots rule!".
	
	button = browser.find_element_by_css_selector("button.btn")
	button.click() # Нажать на кнопку "Submit".

finally:
	time.sleep(10) # ожидание чтобы визуально оценить результаты прохождения скрипта
	browser.quit() # закрываем браузер после всех манипуляций
