import requests
from bs4 import BeautifulSoup
req = requests.get('https://howlongtobeat.com/game?id=38019')
soup = BeautifulSoup(req.text, "lxml")

#------------------------- TITLE -----------------------------------------------
Title=soup.find("div", {"class": "profile_header shadow_text"}).get_text(strip=True)
Title = {"Title":Title}
Title

#---------------------- Game times ----------------------------------

soup.find("li", {"class": "short time_100"}).get_text(strip=True)
Main_Story=soup.find("li", {"class": "short time_100"}).get_text(strip=True)
Main_Story

#-------------------------------------------------------
soup.findAll("li", {"class": "short time_100"})

#------------------------- info ------------------------------------
#Description
Description = soup.find("p", {"style": "margin-bottom: 10px;"}).get_text(strip=True)
Description = {"Description" : Description}
Description
#Profile_info
Profile_info=[]
Profile_info=soup.findAll("div", {"class": "profile_info"})
Profile_info

#----------------------- La primera tabla -----------------------------

Table1 = soup.findAll("div", {"class":"in scrollable back_primary shadow_box"})

for row in Table1:
    name_row=row.find("a", {"href":"game?id=46968"}).get_text(strip=True)
    name_row2=row.find("a", {"href":"game?id=46967"}).get_text(strip=True)
    head_table1=row.find("td", {"style":"min-width:175px;"}).get_text(strip=True)
    print(head_table1)
    print(name_row)
    print(name_row2)

#------------------------ Otras tablas -----------------------------------

Otras_tablas=soup.findAll("table", {"class":"game_main_table"})
Otras_tablas

#------------------------- Rating -----------------------------------------

Rating = soup.find("h5", {"style":"margin-top: -67px;"}).get_text(strip=True)
Rating={"Rating":Rating}
Rating

#-------------------------- Retirement -----------------------------------

Retirement = soup.find("h5", {"style":"margin-top: -86px;"}).get_text(strip=True)
Retirement

#-------------------------- Based_on --------------------------------------

Based_on = soup.findAll("div", {"class":"in game_chart_rev back_form shadow_box"})
Based_on

#-------------------------- Platform --------------------------------------

Platform_user = soup.findAll("div", {"style":"padding: 5px 0;height: 26px;line-height:16px;vertical-align:middle;"})
Platform_user