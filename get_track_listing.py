from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = 'D:\\Code\\Rogue\\Selenium\\chromedriver.exe'
driver = webdriver.Chrome(DRIVER_PATH)
base_url = 'https://en.wikipedia.org/'
driver.get(base_url)
album_name = input('Enter the album name: ')
search = driver.find_element_by_id('searchInput')
search.send_keys(album_name)
search.send_keys(Keys.RETURN)
result = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[3]/ul/li[1]/div[1]/a')
result.send_keys(Keys.RETURN)
track_listing = driver.find_elements_by_class_name('tracklist')
for i in track_listing:
    print(i.text)
driver.quit()