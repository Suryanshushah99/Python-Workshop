from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

names = ['My No BSNL','My No Airtel']
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

for name in names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()
