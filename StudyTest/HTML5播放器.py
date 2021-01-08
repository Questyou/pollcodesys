from time import  sleep
from  selenium import webdriver

driver = webdriver.Chrome(r'd:\chromedriver.exe')
driver.get("http://videojs.com/")
sleep(2)
vedio = driver.find_element_by_id('preview-player_html5_api')



url = driver.execute_script("return arguments[0].currectSrc;" , vedio)
print(url)

print("start")
driver.execute_script("arguments[0].play()" , vedio)

sleep(10)
print('stop')

driver.execute_script("arguments[0].pause()" , vedio)



driver.quit()
