import account, login

print"""
                    Welcome to Steve's I430 Final Project
"""
print" "*12,'-'*50

def check_link(hyperlink):
    if 'twitter' in hyperlink.lower():
        global link
        link="https://twitter.com/signup"

def fix_email():
    global user_email
    user_email.replace("@",",")

ask=raw_input("Would you like to create a new account or login to an existing one? ")
if 'create' in ask:
    name=raw_input("What social media site would you like create an account for? ")
    link=raw_input("Please enter the website url that you want to use: ")
##    binary=FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
    user_email=raw_input("Please enter the email you want to use with the account: ")
    check_link(link)
##    fix_email()
    page=account.Webpage(name, link, user_email)
    page.verify_url()
    page.add_to_db()
    
elif 'login' in ask:
    name=str(raw_input("Please enter the name of the social media site you want to use: "))
    info=login.select(name)
    for item in list(info):
        site=item[0]
        url=item[1]
        usrn=item[2]
        psswd=item[3]
    page2=account.Webpage(site,url,usrn,psswd)
    if name.lower()=='facebook':
        page2.login_fb()
    else:
        page2.login_twitter()
