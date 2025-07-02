
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebAutomatn:

    def __init__(self):
        #Define driver, options, and service- driver is what runs Selenium on a specific browser
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        #Options for downloading the file to a different folder
        download_dir = os.getcwd()
        prefs = {"download.default_directory":download_dir}
        chrome_options.add_experimental_option("prefs",prefs)

        # serviceA = Service(r"C:\Users\imjog\Programming_Projects_and_Exercises\Projects\WebAutomation tool\CommitFolder\chromedriver.exe")
        # driver = webdriver.Chrome(service=serviceA)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        #this opens chrome browser
        webdriver.Chrome()


    def login(self, username_i, password_i):
        self.driver.get("https://demoqa.com/login")
        #Code to login to webpage
        #Locate username and password fields, then find the id tag in html
        #id="userName"
        username_field = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "userName")))
        password_field = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "password")))
        # login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login")))
        login_button = self.driver.find_element(By.ID, "login")

        #automatically fills in those fields on the webpage
        #and click the login button on the webpage
        username_field.send_keys(username_i)
        password_field.send_keys(password_i)
        # login_button.click()

        #string argument is Javascript
        self.driver.execute_script("arguments[0].click();", login_button)


    def fill_form(self, fullname_i, email_i, currentaddress_i,permaddress_i):
        #Locate the Elements dropdown button and Text Box
        #inspect page to locate it (XPATH from rightclick)
        #then click the textbox
        elements = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, 
                                            """//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]""")))
        elements.click()

        Textbox = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "item-0")))
        Textbox.click()

        #Locate form input text fields
        fullname_field = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "userName")))
        email_field = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "userEmail")))
        currentaddress_field = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
        permaddress_field = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
        submit_button = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "submit")))

        #fill in form fields
        fullname_field.send_keys(fullname_i)
        email_field.send_keys(email_i)
        currentaddress_field.send_keys(currentaddress_i)
        permaddress_field.send_keys(permaddress_i)

        #click submit button
        self.driver.execute_script("arguments[0].click();", submit_button)


    def download(self):
        #locate the download/upload button and click download
        upload_or_download = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "item-7")))
        upload_or_download.click()

        download_button = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "downloadButton")))
        download_button.click()


    def close(self):
        # input("\n\nPress Enter to close the browser\n\n")
        self.driver.quit()

if __name__ == "__main__":

    My_WebAutomation = WebAutomatn()
    My_WebAutomation.login(username_i="imjogiat", password_i="iF0rg07i12")
    My_WebAutomation.fill_form(fullname_i="Fred Frederickssen", 
                            email_i="ffssen@gmail.com", 
                            currentaddress_i= "123 Stockholm Street NW", 
                            permaddress_i= "456 Oslo Avenue SE")

    My_WebAutomation.download()
    My_WebAutomation.close()