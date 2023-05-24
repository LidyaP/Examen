from browser import Browser

# before_all este o metoda care contine toate instructiunile care trebuie rulate inainte de orice test
# este echivalentul metodei setUp de la libraria unit test
from pages.home_page import Home_page
from pages.my_dashboard import My_dashboard


def before_all(context):
	context.browser = Browser()  # instantiem un obiect din clasa Browser
	context.home_page = Home_page()
	context.my_dashboard = My_dashboard()
	context.browser.maximise_window()


def after_all(context):
	context.browser.close_browser()  # apelam metoda close_browser pe baza obiectului instantiat din clasa Browser()