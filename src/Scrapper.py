from bs4 import BeautifulSoup
import re

class Scrapper(object):
    def bsScrapper(self, htmltext):
        """
        Given an html text from the web HowlongToBeat it will extract the main data that are of interest.
        """
        soup = BeautifulSoup(htmltext, "lxml")
        dict_keys= {'name':None, 'description': None, 'Developer':None, 'Publisher':None, 'Playable On':None, 'Genres':None, 'NA':None, 'EU':None, 'JP':None, 'Additional Content':None, 'Single-Player': None, 'Speedrun':None, 'Retirement':           None, 'Platform':None}
        data = {}
        #----------------------basic Data
        if self.check_data(soup.find("div", {"class": "profile_header shadow_text"})):
            data["name"] = soup.find("div", {"class": "profile_header shadow_text"}).get_text(strip=True)

        if self.check_data(soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find("p")):
            data["description"] = soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find("p").get_text(strip=True)

        try:
            name, info = self.get_game_data(soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[0].get_text(strip=True))
            data[name] = self.check_if_split(name,info)

            name, info = self.get_game_data(soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[1].get_text(strip=True))
            data[name] = self.check_if_split(name,info)

            name, info = self.get_game_data(soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[2].get_text(strip=True))
            data[name] = self.check_if_split(name,info)

            name, info = self.get_game_data(soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[3].get_text(strip=True))
            data[name] = self.check_if_split(name,info)

            name, info = self.get_game_data(soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[4].get_text(strip=True))
            data[name] = self.check_if_split(name,info)

            name, info = self.get_game_data(soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[5].get_text(strip=True))
            data[name] = self.check_if_split(name,info)

            name, info = self.get_game_data(soup.find_all("div",{"class": "in back_primary shadow_box"})[2].find_all("div", {"class":"profile_info"})[6].get_text(strip=True))
            data[name] = self.check_if_split(name,info)



        except Exception as e:
            pass

        data = self.delete_extra_tags(data)
        #---------------------- Aditional content
        try:
            dummyArray = []
            if self.check_data(soup.find("div", {"class": "in scrollable back_primary shadow_box"})):
                item = soup.find("div", {"class": "in scrollable back_primary shadow_box"}).find("td").get_text(strip=True)
                for tbody in soup.find("div", {"class": "in scrollable back_primary shadow_box"}).find_all("tbody"):
                    td = tbody.find_all("td")
                    tempArray = []
                    for element in td[1:]:
                        tempArray.append(element.get_text(strip=True))
                    dummyArray.append({"name":td[0].get_text(strip=True), "data":tempArray})

                data[item] = dummyArray
        except Exception as e:
            pass

        #----------------------------Single player
        try:
            dummDict = {}
            item = soup.find_all("div", {"class": "in scrollable shadow_box back_primary"})[0].find("td").get_text(strip=True)
            for tbody in soup.find_all("div", {"class": "in scrollable shadow_box back_primary"})[0].find_all("tbody"):
                td = tbody.find_all("td")
                tempArray = []
                for element in td[1:]:
                    tempArray.append(element.get_text(strip=True))
                dummDict[td[0].get_text(strip=True)] = tempArray
            data[item] = dummDict
            #data["singlePlayer"] = dummDict
        except Exception as e:
            pass

        #----------------------------SpeedRun
        try:
            dummDict = {}
            item = soup.find_all("div", {"class": "in scrollable shadow_box back_primary"})[1].find("td").get_text(strip=True)
            for tbody in soup.find_all("div", {"class": "in scrollable shadow_box back_primary"})[1].find_all("tbody"):
                td = tbody.find_all("td")
                tempArray = []
                for element in td[1:]:
                    tempArray.append(element.get_text(strip=True))
                dummDict[td[0].get_text(strip=True)] = tempArray
            data[item] = dummDict
            #data["speedRun"] = dummDict
        except Exception as e:
            pass
        #----------------------- Rating

        if self.check_data(soup.find("h5", {"style":"margin-top: -67px;"})):
            name, info = self.get_game_points(soup.find("h5", {"style":"margin-top: -67px;"}).get_text(strip=True))
            data[name] = int(info)

        if self.check_data(soup.find("h5", {"style":"margin-top: -86px;"})):
            name, info = self.get_game_points(soup.find("h5", {"style":"margin-top: -86px;"}).get_text(strip=True))
            data[name] = float(info)

        #---------------- Platform
        try:
            dummDict = {}
            if self.check_data(soup.find("div", {"class": "in shadow_box back_primary"})):
                item = soup.find("div", {"class": "in shadow_box back_primary"}).find("td").get_text(strip=True)
                for tbody in soup.find("div", {"class": "in shadow_box back_primary"}).find_all("tr")[1:]:
                    td = tbody.find_all("td")
                    tempArray = []
                    for element in td[1:]:
                        tempArray.append(element.get_text(strip=True))
                        dummDict[td[0].get_text(strip=True)] = tempArray
                data[item] = dummDict
        except Exception as e:
            pass


        dict_keys.update(data)
        return dict_keys

    def get_game_points(self, str_element):
        name = re.sub(r"^.*%\s?", "", str_element)
        info = re.search(r"^\D*(.*)\%\s?\w+$", str_element).group(1)
        return name, info

    def get_game_data(self, str_element):
        name = re.sub(r":.*$","",str_element)
        info = re.sub(r"^.*:","",str_element)
        return name, info

    def check_data(self, object_data):
        if object_data is not None:
            return True
        else:
            return False

    def check_if_split(self, name, string):
        """
        Checks if the variables from the basic data set are in the set of spliteable data
        """
        if name in ["Playable On","Genres"]:
            return list(map(str.strip, string.split(",")))
        else:
            return string

    def delete_extra_tags(self, data):
        """
        Delete JP, EU ,NA and Updated tag
        """
        data.pop("Updated", None)
        return data
