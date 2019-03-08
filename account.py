import password_generator, create_db
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class Webpage(object):

    def __init__(self, name, url, email, password=password_generator.gen()):
        self.name=name
        self.url=url
        self.email=email
        self.password=password
        self.driver=webdriver.Firefox(firefox_binary=binary)


    def verify_url(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            
            print "Error",e,"occurred. Please start over to try again."
        else:
            if self.name.lower()=="facebook":
                 Webpage.create_facebook(self)
            elif self.name.lower()=="twitter":
                Webpage.create_twitter(self)
            print "Please fill in the rest of information to create account."
            
    def create_facebook(self):
        username=self.driver.find_element_by_name("reg_email__")
        username.send_keys(self.email)
        username2=self.driver.find_element_by_name("reg_email_confirmation__")
        username2.send_keys(self.email)
        password=self.driver.find_element_by_name("reg_passwd__")
        password.send_keys(self.password)

    def create_twitter(self):
        username=self.driver.find_element_by_name("user[email]")
        username.send_keys(self.email)
        password=self.driver.find_element_by_name("user[user_password]")
        print self.password
        password.send_keys(self.password)

    def add_to_db(self):
        create_db.create_database()
        create_db.create_table()
        create_db.insert(self.name,self.url,self.email,self.password)

    def login_fb(self):
        self.driver.get(self.url)
        username=self.driver.find_element_by_id("email")
        username.send_keys(self.email)
        password=self.driver.find_element_by_id("pass")
        password.send_keys(self.password)
        self.driver.find_element_by_id("loginbutton").click()

    def login_twitter(self):
        self.driver.get("https://twitter.com/login")
        username=self.driver.find_element_by_xpath("//input[@class='js-username-field email-input js-initial-focus']")
        username.send_keys(self.email)
        password=self.driver.find_element_by_xpath("//input[@class='js-password-field']")
        password.send_keys(self.password)
        self.driver.find_element_by_xpath("//button[@class='submit btn primary-btn']").click()

#main
##def check_link(hyperlink):
##    if 'twitter' in hyperlink.lower():
##        global link
##        link="https://twitter.com/signup"
        
##name=raw_input("What social media site would you like create an account for? ")
##link=raw_input("Please enter the website url that you want to use: ")
binary=FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
##user_email=raw_input("Please enter the email you want to use with the account: ")
##
##check_link(link)
##page=Webpage(name, link, user_email)
##page.verify_url()
##page.add_to_db()

