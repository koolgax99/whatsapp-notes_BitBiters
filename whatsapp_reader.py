from selenium import webdriver
import time


driver = webdriver.Chrome(
    r'C:\Users\Nihar\Downloads\chromedriver_win32\chromedriver')

driver.get("https://web.whatsapp.com/")
time.sleep(15)

user_name = 'Anany Talwad Dwd'

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

"""for i in range(10):
    message_box = driver.find_element_by_xpath('//div[@class="class="_1RAno _2rBI0 message-out focusable-list-item""]')
    message_box.send_keys("hey, this is a whatsapp bot + {i} ")

    message_box = driver.find_element_by_xpath('//button[@class="_2Ujuu"]')
    message_box.click()
"""

#print(driver.page_source)

main_div = driver.find_element_by_xpath('//div[@class="tSmQ1"]')

div = main_div.find_elements_by_xpath('//div[@class="_1RAno message-out focusable-list-item"]')
print("div = ", div)

for i in range(len(div)):
    print(div[i].text)



"""for i in range(len(div)):
    text = div[i].find_elements_by_xpath('//div[@class="_1ij5F _2tbXF _1zinb"]')
    print(text)

    for j in range(len(text)):
        print(text[j])
        msg = text[j].find_element_by_xpath('//div[@class="_1ij5F _2tbXF _1zinb"]').text
        print(msg)
"""


