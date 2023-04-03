from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=data+science")
a = []
df = pd.DataFrame(columns=['Title','Views','Age','Author','Text','CC','Moments','Numer_of_moments'])
for i in range(len(driver.find_elements(By.CLASS_NAME,'style-scope ytd-video-renderer'))):
    if not driver.find_elements(By.CLASS_NAME,'style-scope ytd-video-renderer')[i].text == "":
        a.append(driver.find_elements(By.CLASS_NAME,'style-scope ytd-video-renderer')[i].text)
df['Title'] = a
df = df['Title'].str.split('\n',expand=True)
for i in range(len(df)):
    if type(df.iloc[i,5]) == type('a') and len(df.iloc[i,5]) > 4:
        df.iloc[i, 5:8] = df.iloc[i, 5:8].shift()
print(df.iloc[:,5:7])
