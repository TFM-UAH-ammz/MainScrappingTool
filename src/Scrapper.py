from bs4 import BeautifulSoup

class Scrapper(object):
    def bsScrapper(self, htmltext):
        soup = BeautifulSoup(htmltext, "lxml")
        data = {}
        #----------------------basic Data
        data["name"] = soup.find("div", {"class": "profile_header shadow_text"}).get_text(strip=True)
        data["description"] = soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find("p").get_text(strip=True)
        data["developer"] = soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[0].get_text(strip=True).strip("Developer:")
        data["publisher"] = soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[1].get_text(strip=True).strip("Publisher:")
        data["playable_On"] = soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[2].get_text(strip=True).strip("Playable On:").split(",")
        data["genres"] = soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[3].get_text(strip=True).strip("Genres:").split(",")

        #---------------------- Aditional content

        dummyArray = []
        for tbody in soup.find("div", {"class": "in scrollable back_primary shadow_box"}).find_all("tbody"):
            td = tbody.find_all("td")
            tempArray = []
            for element in td[1:]:
                tempArray.append(element.get_text(strip=True))
            dummyArray.append({"name":td[0].get_text(strip=True), "data":tempArray})

        data["additionalContent"] = dummyArray

        #----------------------------Single player

        dummDict = {}
        for tbody in soup.find_all("div", {"class": "in scrollable shadow_box back_primary"})[0].find_all("tbody"):
            td = tbody.find_all("td")
            tempArray = []
            for element in td[1:]:
                tempArray.append(element.get_text(strip=True))
            dummDict[td[0].get_text(strip=True)] = tempArray
        data["singlePlayer"] = dummDict

        #----------------------------SpeedRun

        dummDict = {}
        for tbody in soup.find_all("div", {"class": "in scrollable shadow_box back_primary"})[1].find_all("tbody"):
            td = tbody.find_all("td")
            tempArray = []
            for element in td[1:]:
                tempArray.append(element.get_text(strip=True))
            dummDict[td[0].get_text(strip=True)] = tempArray
        data["speedRun"] = dummDict
        data

        #----------------------- Rating

        data["rating"] = int(soup.find("h5", {"style":"margin-top: -67px;"}).get_text(strip=True).strip("% Rating"))

        data["retirement"] = float(soup.find("h5", {"style":"margin-top: -86px;"}).get_text(strip=True).strip("%Retirement")[-4:])

        #---------------- Platform

        dummDict = {}
        for tbody in soup.find("div", {"class": "in shadow_box back_primary"}).find_all("tr")[1:]:
            td = tbody.find_all("td")
            tempArray = []
            for element in td[1:]:
                tempArray.append(element.get_text(strip=True))
            dummDict[td[0].get_text(strip=True)] = tempArray
        data["platform"] = dummDict

        return data
