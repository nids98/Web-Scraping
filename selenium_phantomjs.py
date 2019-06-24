from selenium import webdriver

driver = webdriver.PhantomJS(executable_path= r'/home/nidhi/PhantomJS/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)