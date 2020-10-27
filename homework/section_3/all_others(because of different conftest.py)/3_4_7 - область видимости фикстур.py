from os import system

import pytest

@pytest.fixture(scope="class")
def prepare_faces():
	print("^_^", "\n")
	yield
	print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
	print(":)", "\n")


@pytest.fixture(autouse=True) # благодаря autouse будет исполняться для каждого теста, и первой среди прочих, уступая только prepare_faces, у которой scope='class'
def print_smiling_faces():
	print(":-Р", "\n")


class TestPrintSmilingFaces():
	def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
		pass # какие-то проверки

	def test_second_smiling_faces(self, prepare_faces): # prepare_faces проигнорируется, т.к. она относится к классу и выполняется единожды
		pass # какие-то проверки
'''
порядок вывода смайликов
^_^ - начало prepare_faces(), вызвано из test_first_smiling_faces()
:-Р - print_smiling_faces(), не вызвано ниоткуда, но выполняется перед каждой функцией благодаря autouse=True
:)  - very_important_fixture(), вызвано из test_first_smiling_faces()
--- первая функция отработала ---
:-Р - print_smiling_faces(), не вызвано ниоткуда, но выполняется перед каждой функцией благодаря autouse=True
    - в параметрах второй функции есть вызов prepare_faces(), но он проигнорирован, т.к. фикстура относится к классу и уже выполнялась в нём.
:3  - завершение prepare_faces(), блок команд фикстуры после строки yield
'''
def main():
	system(f'pytest -s "{__file__}"')

if __name__ == "__main__":
	main()
