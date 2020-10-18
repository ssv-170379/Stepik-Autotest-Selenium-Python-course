#!/usr/bin/python3
#coding=utf-8

from selenium import webdriver
import time, os, pyperclip # https://stepik.org/lesson/184253/step/2?discussion=1038936&unit=158843

try:
	browser = webdriver.Chrome()
	browser.get('http://suninjuly.github.io/file_input.html') # Открыть страницу http://suninjuly.github.io/file_input.html.

	for element in browser.find_elements_by_css_selector('input[type="text"][required]'):
		element.send_keys('Hi!') # Заполнить текстовые поля: имя, фамилия, email

	curr_dir = os.getcwd() # есть нюансы, см https://www.makeuseof.com/how-to-get-the-current-directory-in-python/
	newfile = os.path.join(curr_dir, 'hi.txt')
	open(newfile, 'a').close() # создастся, если не было. если был - файл не изменится
	browser.find_element_by_css_selector('input#file').send_keys(newfile) # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым

	browser.find_element_by_css_selector('button.btn').click() # Нажать кнопку "Submit".
	os.remove(newfile) # удаляем в конце

	answer = browser.switch_to.alert.text
	answer = answer.split()[-1]
	pyperclip.copy(answer)
	print(f'The answer "{answer}" is copied to your clipboard')

finally:
	time.sleep(10) # ожидание чтобы визуально оценить результаты прохождения скрипта
	browser.quit() # закрываем браузер после всех манипуляций
