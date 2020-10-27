#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
import time

try: 
	form = input ('Какую форму тестировать, 1 или 2? (введите цифру): ')
	link = f'http://suninjuly.github.io/registration{form}.html'
	browser = webdriver.Chrome()
	browser.get(link)

	# Код, заполняющий обязательные поля
	for clss in ['first', 'second', 'third']: # required classes
		element = browser.find_element_by_css_selector (f'input.{clss}[required]') # also check <input> tag and 'required' attribute.
		element.send_keys("Мой ответ")

	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	# Проверяем, что смогли зарегистрироваться
	time.sleep(1) # ждем загрузки страницы

	welcome_text_elt = browser.find_element_by_tag_name("h1") # находим элемент, содержащий текст
	welcome_text = welcome_text_elt.text # записываем в переменную welcome_text текст из элемента welcome_text_elt

	assert "Congratulations! You have successfully registered!" == welcome_text # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

finally:
	time.sleep(10) # ожидание чтобы визуально оценить результаты прохождения скрипта
	browser.quit() # закрываем браузер после всех манипуляций
