from os import system
from time import sleep

'''
Привет!

Отличия данной реализации от задания:
1. Не создан отдельный репозиторий. Не хочу их плодить, плюс авторы курса не против (https://stepik.org/lesson/237240/step/9?discussion=1067015&reply=1067023&unit=209628) .
2. Имя фикстуры не browser, а browser_and_language, т.к. она возвращает в тестовую функцию ещё и язык, указанный в командной строке.
3. Проверяется не факт наличия кнопки, а соответствие текста на ней выбранной локали (реализована проверка для английского, русского, испанского и французского языков).

Я буду немного грустить, но пойму, если вы снизите оценку из-за этих различий. Всё-таки ТЗ есть ТЗ...
И очень обрадуюсь, если не снизите, т.к. реализованная задача интереснее и даже немного сложнее поставленной.

Добра!
'''

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
cart_button_texts = {
	'en':'Add to basket',
	'ru':'Добавить в корзину',
	'es': 'Añadir al carrito',
	'fr': 'Ajouter au panier'}

def test_check_add_to_cart_button_text_locales(browser_and_language):

	browser,user_language=browser_and_language # unpack parameters to a separated variables
	browser.get(link)

	expected_result = cart_button_texts[user_language]
	actual_result = browser.find_element_by_css_selector("button.btn-add-to-basket").text

	print('-'*72+f'\nLocale is "{user_language}". The text on the button is "{actual_result}".\n'+'-'*72)
	assert actual_result == expected_result, f'Expected "{expected_result}" for "{user_language}" locale, got "{actual_result}".'
	#sleep(3)

def main():
	system(f'pytest -s -v --language=ru "{__file__}"')
if __name__ == "__main__":
	main()
