# To get all the HTML of the page

from selenium import webdriver

driver = webdriver.Chrome(executable_path= r'/home/nidhi/ChromeDriver/chromedriver')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)