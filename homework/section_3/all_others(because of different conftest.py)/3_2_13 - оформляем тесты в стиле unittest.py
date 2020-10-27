#!/usr/bin/python3
#coding=utf-8

'''
- Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
- Создайте новый файл
- Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
- Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
- Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
- Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
- Запустите получившиеся тесты из файла
- Просмотрите отчёт о запуске и найдите последнюю строчку
- Отправьте эту строчку в качестве ответа на это задание

Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. 

Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке.
'''

from selenium import webdriver
import unittest


def register(url):
	browser = webdriver.Chrome()
	browser.get(url)

	# Код, заполняющий обязательные поля
	for clss in ['first', 'second', 'third']: # required classes
		element = browser.find_element_by_css_selector (f'input.{clss}[required]') # also check <input> tag and 'required' attribute.
		element.send_keys("Мой ответ")

	browser.find_element_by_css_selector('button.btn').click()# Отправляем заполненную форму

	# Проверяем, что смогли зарегистрироваться
	browser.implicitly_wait(5) # на случай медленной прогрузки выставляем ожидание элемента.
	welcome_text = browser.find_element_by_css_selector('h1').text # находим элемент, содержащий текст
	browser.close()
	return welcome_text

class TestRegForm(unittest.TestCase):
	def test_form1(self):
		welcome_text = register('http://suninjuly.github.io/registration1.html')
		self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'WTF?!!')

	def test_form2(self):
		welcome_text = register('http://suninjuly.github.io/registration2.html')
		self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'WTF?!!')

if __name__ == "__main__":
	unittest.main()
