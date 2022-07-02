from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time 
import sys
import numpy as np
import os
import subprocess
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") 
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "normal"
drivera = webdriver.Chrome(options=chrome_options, executable_path='/home/srijithreddy/Desktop/Srijith reddy/chromedriver')
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return
driver = webdriver.Chrome('/home/srijithreddy/Desktop/Srijith reddy/chromedriver')
driver.get("https://www.cricbuzz.com/")
driver.find_element_by_xpath('//*[@id="hm-scag-mtch-blk"]/ul/li[1]/a').click()
drivera.get("https://web.whatsapp.com/")
target = '"Meghanites🔥🤙🌚"'
#Replace the below string with your own message
string = "Arey wicket ra!!!"
string2 = "six ra!!!"
string4 = "four ra!!!"
string3 = "half century"
x_arg = '//span[contains(@title,' + target + ')]'
group_title = WebDriverWait(drivera,60).until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
l=100000000
over=[]
total=[]
total2=[]
wickets=[]
over2=[]
sco = []
state = 0
for i in range(l):
    time.sleep(2)
    try:
        options = WebDriverWait(driver,100).until(EC.presence_of_all_elements_located((By.ID, 'matchCenter')))
    except NoSuchElementException:
        print('No match available')
        driver.close()
        drivera.close()
        break
    score = driver.find_element_by_xpath('//*[@id="matchCenter"]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/h2').text
    try:
        ind = driver.find_element_by_xpath('//*[@id="matchCenter"]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]').text
    except NoSuchElementException:
        print('No match available')
        driver.close()
        drivera.close()
        break
    scop=ind[ind.index('*')+1:ind.index('*')+3]
    sco+=[scop]
    over+= [score]
    if over[i]!=over[i-1] and over[i]!='':
        total+=[score]
        total2+=[score[score.index(' ')+1:score.index('(')-3]]
        wickets+=[score[score.index('(')-2:score.index('(')-1]]
        over2+=[score[score.index('(')+1:len(score)-1]]
        state = 1
        print('score is',score)
        print(i)
    if  len(wickets)>=2 and wickets[len(wickets)-1]!= wickets[len(wickets)-2] and state ==1 and int(wickets[len(wickets)-1])>0:
        sendmessage("wicket ra score chusko "+score)
        WebDriverWait(drivera,10).until(EC.presence_of_all_elements_located((By.ID, 'main')))
        input_box = drivera.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
        input_box.send_keys(string + score + Keys.ENTER)
        time.sleep(100)
    if len(total2)>=2 and int(total2[len(total2)-1]) ==  (int(total2[len(total2)-2])+6)and state ==1:
        sendmessage("six ra")
        WebDriverWait(drivera,10).until(EC.presence_of_all_elements_located((By.ID, 'main')))
        input_box = drivera.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
        input_box.send_keys(string2 + score + Keys.ENTER)
        time.sleep(100)
    if len(total2)>=2 and int(total2[len(total2)-1]) ==  (int(total2[len(total2)-2])+4)and state ==1:
        sendmessage("four ra")
        WebDriverWait(drivera,10).until(EC.presence_of_all_elements_located((By.ID, 'main')))
        input_box = drivera.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
        input_box.send_keys(string4 +  Keys.ENTER)
        time.sleep(100)
    if i>1 and int(sco[i])>=51 and int(sco[i-1])<=50 and state ==1:
        sendmessage("half century")
        WebDriverWait(drivera,10).until(EC.presence_of_all_elements_located((By.ID, 'main')))
        input_box = drivera.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
        input_box.send_keys(string3 + ind[0:ind.index('*')] + Keys.ENTER)
        time.sleep(60)   
    driver.refresh()
    state = 0
