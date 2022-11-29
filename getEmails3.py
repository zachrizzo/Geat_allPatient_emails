from calendar import different_locale
from re import search
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from pynput.mouse import Button, Controller
# Import smtplib for the actual sending function
import smtplib
import requests
# Import the email modules we'll need
from email.mime.text import MIMEText

mouse = Controller()
sleep1 = time.sleep(2.5)

driver = webdriver.Chrome()

upgrade_action = ActionChains(driver)
driver.get('https://azamasapp.ecwcloud.com/mobiledoc/jsp/webemr/login/newLogin.jsp')
driver.maximize_window()
time.sleep(3)
emails = []
StartTime = time.time()
print(StartTime)
From = 'zachcilwa@gmail.com'
to ='zachcilwa@gmail.com'
bot = 11

def send_Email(message:str  ):
        
	return requests.post(
		"https://api.mailgun.net/v3/sandboxc737f3da6b94416ea1a493e0ff6f7e4a.mailgun.org/messages",
		auth=("api", "2ec664b6dc7e27eb0e3a27ee419477f0-18e06deb-c5adc1c8"),
		data={"from": "Mailgun Sandbox <postmaster@sandboxc737f3da6b94416ea1a493e0ff6f7e4a.mailgun.org>",
			"to": "Zachary Morgan M Rizzo <zachcilwa@gmail.com>",
			"subject": f"Bot {bot}",
			"text": message})


    


def login():
    try:
        Eclinical_loging = driver.find_element(By.XPATH, '//*[@id="doctorID"]')
        Eclinical_loging.send_keys('zachrizzo')
        time.sleep(2)
        loging_buttom_1 = driver.find_element(By.XPATH, '//*[@id="nextStep"]')
        loging_buttom_1.click()
        password_2 = driver.find_element(By.XPATH, '//*[@id="passwordField"]')
        password_2.send_keys('Karen013074!')
        login_2 = driver.find_element(By.XPATH, '//*[@id="Login"]')
        login_2.click()
        time.sleep(15)
        
    except:
        input("Press Enter to continue...")


def addPerson(ACC_Number):
    try:
        try:
            try: 
                time.sleep(4)

                search = driver.find_element(
                    By.XPATH, ' //*[@id="jellybean-panelLink65"]')
                search.click()
                time.sleep(3)
                searchType = driver.find_element(
                    By.XPATH, '/html/body/div[3]/div[2]/div[10]/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[1]/div/div/div/div[2]/div/div')
                searchType.click()
                sleep1
                time.sleep(3)
                account_numberType = driver.find_element(
                    By.XPATH, '/html/body/div[3]/div[2]/div[10]/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[1]/div/div/div/div[2]/div/ul/li[5]/a')
                account_numberType.click()
                sleep1
                time.sleep(3)
                search_person = driver.find_element(
                    By.XPATH, '/html/body/div[3]/div[2]/div[10]/div/div/div/div/div[2]/div[1]/form/div/div/div[1]/div[1]/div/div/div/div[1]/div/input')
                search_person.send_keys(ACC_Number)
                sleep1
                time.sleep(3)
                if search.is_displayed() is True:
                    print('search')
                try:
                    driver.implicitly_wait(10)
                    person = driver.find_element(
                        By.XPATH, '//*[@id="rule-table2"]/tbody/tr/td[4]/span')
                    print('person1')
                    if person.is_displayed() is True:
                        print('person2')
                        person.click()
                        sleep1
                        time.sleep(6)

                        # try:
                        email = driver.find_element(
                                By.XPATH, ' //*[@id="phub_dialog"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[4]/p/span[1]/a/span')
                        #     if len(email.text) > 2:
                        #         emails.append(email.text)
                        #         print(email.text)
                            
                        # except Exception as e:
                        emails.append(email.text)
                        print(email.text)
                            # print(e)
                            # print('close 1')
                        sleep1
                        close_button = driver.find_element(
                                By.XPATH, '/html/body/div[3]/div[2]/div[10]/div/ng-include/div/div[1]/div[1]/div/div[1]/button')
                        close_button.click()
                        sleep1
                        # emails.append('No-Email') 
                    # else:
                    #     print('close 2')
                    #     try:
                    #         time.sleep(6)
                    #         emails.append('No-Email')
                    #         sleep1
                    #         close_button = driver.find_element(
                    #             By.XPATH, '/html/body/div[3]/div[2]/div[10]/div/ng-include/div/div[1]/div[1]/div/div[1]/button')
                    #         close_button.click()
                    #         pass
                    #     except Exception as e:
                    #         print(e)
                            

                except Exception as e:
                    # print(e)
                    print('nested')
        
                    try:
                
                        driver.find_element(
                                By.XPATH, '/html/body/div[3]/div[2]/div[10]/div/div/div/div/div[1]/button').click()
                        emails.append('No-Email')
                    except:
                        print("close2")       
                        driver.find_element(
                                By.XPATH, '//*[@id="patient-hubBtn1"]').click()
                        emails.append('No-Email')
            
            except:
                    try:
                        print('nested2')
                        close_button = driver.find_element(
                            By.XPATH, '/html/body/div[3]/div[2]/div[10]/div/div/div/div/div[1]/button')
                        close_button.click() 
                        emails.append('No-Email') 
                        
                    except Exception as e:
                        print('nested3')
                        # print(e)
                        driver.refresh()
                        
                        time.sleep(3)
                        driver.switch_to.alert.accept()
                        time.sleep(7)

                        emails.append('No-Email')
        except:
            print("rapidRefresh")

            for i in range(10):
                driver.refresh()
                
                time.sleep(3)
                try:
                    driver.switch_to.alert.accept()
                except:
                    pass
                time.sleep(7)
            login()
            emails.append('No-Email')                 

          
    except Exception as e:
        # print(e)
        try:
            print('nested4')
            close_button = driver.find_element(
                By.XPATH, '/html/body/div[3]/div[2]/div[10]/div/div/div/div/div[1]/button')
            close_button.click() 
            emails.append('No-Email') 
            
        except Exception as e:
            print('nested4')
            # print(e)
            emails.append('No-Email') 
            send_Email(f'Bot {bot} needs your help')
            input("Press Enter to continue...")
            pass



login()


# def searchPerson():


df = pd.read_csv(
    filepath_or_buffer='eclinical report 13.csv'

)
dfShort = df.head()

names = df.loc[:, 'Patient Name']
account_number = df.loc[:, "Acc #"]

z =1
for i in account_number:
    t = [ 23566, 21755,4343343434,334645,8394893489348]
    z += 1
    if z == 5 or z == 100 or z == 500 or z == 700 or z == 900 :
        st = ", ".join(emails)
        send_Email(f'we are at email {z}, these are the emails so far {st}')
    # if z == 50:
    #     break
    # if i != 9968:
    addPerson(i)
    print(i)
    print(f" 2patient  {z}")
    # else:
    #     pass

difference = 0
emails_length = len(emails)
df_length = len(df)
print(emails_length)  
print (df_length) 
if emails_length != df_length :
        try:
            if emails_length > df_length:
                difference = emails_length-df_length
                print(f' the email List was {difference} off ')
                for i in range(difference):
                    # reversre_index =df_length-i+1
                    emails.pop()
                    # print(f'{reversre_index} index')

            elif emails_length < df_length:
                difference = df_length - emails_length
                print(f' the df List was {difference} off ')
                z =1
                for i in range(0,difference):
                    z+=1
                    #time.sleep(.01)
                    emails.append('No-Email')
                    
                
                print(len(emails))
                    

           # input('the output was off, enter to continue ... ')
            
        
            
        except Exception as e:
            print(e)
            st2 = ", ".join(emails)
            send_Email(f'Final list of emails {st2}')
else:
    pass

print(emails_length)  
print (df_length)     

st2 = ", ".join(emails)
send_Email(f'Final list of emails {st2}')
df['Email'] = emails

df.to_csv(f'out-{bot} -2.csv')

# print(df)
endTime = time.time()
print(endTime)
print(endTime-StartTime/1000/1000)