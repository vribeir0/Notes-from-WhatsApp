from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import os,sys
from dotenv import load_dotenv


class WhatsApp():

    def __init__(self):
        load_dotenv()
        self.name = os.getenv('CONTACT')
        self.contact_exists()
        self.driver = self.launch()
     
    def contact_exists(self):
        if(len(self.name) < 1):
            print("** Insert the contact name in the '.env' file **")
            sys.exit(1)  

    def launch(self):
        #Browser params    
        base_dir = os.getcwd()
        chromedriver = os.path.join(base_dir,'resources','webdriver',"chromedriver.exe")
        profile = os.path.join(base_dir,'resources','profile',)
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=" + profile)
        driver = webdriver.Chrome(executable_path=chromedriver, options=options)
        return driver
    
    def open_chat(self):
        self.driver.get('https://web.whatsapp.com/')
        try:
            wait = WebDriverWait(self.driver,10)
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title^='"+self.name+"']")))
        except TimeoutException:
            pass
        try:
            self.driver.find_element(By.CSS_SELECTOR, "[title^='"+self.name+"']").click()
        except NoSuchElementException as e:
            print(self.name + " not found")
            self.driver.quit()
            sys.exit(1)
        chat = self.driver.find_element_by_id('main')
        return chat.get_attribute('innerHTML')
    
    def get_messages(self):
        source = self.open_chat()
        print(source)

        
    

    


wp = WhatsApp()
wp.get_messages()