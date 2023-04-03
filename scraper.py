from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=coding")
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
for i in range(len(df)):
    if type(df.iloc[i,6]) == type('a') and len(df.iloc[i,6]) < 4:
        df.iloc[i,5] += df.iloc[i,6]
        df.iloc[i, 6:8] = df.iloc[i, 6:8].shift(-1)
for i in range(len(df)):
    if type(df.iloc[i,1]) == type('a') and 'watching' in df.iloc[i,1]:
        df.iloc[i, 2:] = df.iloc[i, 2:].shift()
for i in range(len(df)):
    if df.iloc[i,8] is not None:
        df.iloc[i,7], df.iloc[i,8] = df.iloc[i,8], df.iloc[i,7]
if len(df.columns) > 8:
    df = df.drop([8],axis=1)
df.columns=['Title','Views','Age','Author','Text','CC','Moments','Number_of_moments']

print(df)
