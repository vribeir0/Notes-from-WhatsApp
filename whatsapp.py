from selenium import webdriver
import os,sys
from dotenv import load_dotenv
load_dotenv()
CONTACT = os.getenv('CONTACT')
if(len(CONTACT) < 1):
    print("** Insert the contact name in the '.env' file **")
    sys.exit(0)

def main():    
    
    base_dir = os.getcwd()
    chromedriver = os.path.join(base_dir,'resources','webdriver',"chromedriver.exe")
    profile = os.path.join(base_dir,'resources','profile',)

    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir=" + profile)
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.get('https://web.whatsapp.com/')
    get_messages(driver)

# def get_messagees(driver):
    # driver.find_element_by_css_selector("")


if __name__ == "__main__":
    main()
