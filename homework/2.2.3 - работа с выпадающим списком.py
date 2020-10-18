#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
import time
try: 
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/selects1.html') # Открыть страницу http://suninjuly.github.io/selects1.html

	x = int(browser.find_element_by_css_selector('#num1').text)
	y = int(browser.find_element_by_css_selector('#num2').text)
	result = x+y # Посчитать сумму заданных чисел

	browser.find_element_by_tag_name('select').click()
	browser.find_element_by_css_selector(f'[value="{str(result)}"]').click() # Выбрать в выпадающем списке значение равное рассчитанной сумме

	browser.find_element_by_css_selector('button.btn').click() # Нажать кнопку "Submit"

	answer = browser.switch_to.alert.text
	print(answer.split()[-1])

finally:
	time.sleep(10) # ожидание чтобы визуально оценить результаты прохождения скрипта
	browser.quit() # закрываем браузер после всех манипуляций
