from selenium import webdriver

deiver = webdriver.Chrome(r'd:\chromedriver.exe')
deiver.get("http://www.baidu.com/")

cookie  = deiver.get_cookies()

print(cookie)

deiver.add_cookie({'domain': 'www.baidu.com', 'httpOnly': False,
                   'name': 'keyaaaaaa', 'value':'value-bbbbbbbbbb','path': '/', 'secure': False, 'value': '1'})
cookie1  = deiver.get_cookies()
print(cookie1)

for cookie in deiver.get_cookies():
    print("%s - > %s " % (cookie['name'] , cookie['value']))
deiver.quit()