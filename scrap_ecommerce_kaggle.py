from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
#options.add_argument('--incognito')
#options.add_argument('--window-size=1920x1080')
#options.add_argument('--no-sandbox') # Bypass OS security model
chrome_driver_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver_path)
driver.get("https://www.kaggle.com/olistbr/brazilian-ecommerce")
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

elements = driver.find_elements_by_xpath("//a[@class='button__anchor-wrapper']")
url = elements[0].get_attribute("href")
driver.get(url)

#elements2 = driver.find_elements_by_xpath("//a[@class='LoginRegisterStyles_SignInOrRegisterIconButton-sc-18qv3mq iAOZbU']")
elements2 = driver.find_elements_by_xpath("//a[@class='LoginRegisterStyles_SignInOrRegisterIconButton-sc-18qv3mq CsZte']")
elements2[0].click()

time.sleep(10) 

username = driver.find_element_by_name("identifier")
username.send_keys("user")
driver.find_element_by_id("identifierNext").click()

time.sleep(10)

password = driver.find_element_by_name("password")
password.send_keys("password")
driver.find_element_by_id("passwordNext").click()

time.sleep(10)

elements3 = driver.find_elements_by_xpath("//a[@class='button__anchor-wrapper']")
url2 = elements3[0].get_attribute("href")
driver.get(url2)
#download_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'download button ID')))
#download_button.click()
 
#storyUrls = [el.get_attribute("href") for el in elements]