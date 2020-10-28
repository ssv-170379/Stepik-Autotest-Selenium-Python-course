from os import system

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
	browser.get(link)
	browser.find_element_by_css_selector("#login_link")

def main():
	system(f'pytest -s -v "{__file__}"')
if __name__ == "__main__":
	main()
