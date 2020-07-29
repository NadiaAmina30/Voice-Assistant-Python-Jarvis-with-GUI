from selenium import webdriver
import pyttsx3 as p 
from webdriver_manager.chrome import ChromeDriverManager
drive = webdriver.Chrome(ChromeDriverManager().install())
class info():
    def __init_(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Nadia Amina\Downloads\chromedriver_win32\chromedriver.exe')
    
    def get_info(self,query):
        self.query = query 
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')  
        search.click()
        search.send_keys(query)
        
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()
        
        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[2]')
        readable_text = info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()
        
bot = info()
bot.get_info("liberty bell")        