import requests
import json
from time import sleep
from Scrapper import Scrapper

URL_LOOP = "https://howlongtobeat.com/game?id="

class ScrapperLoop():
    dataDict = {}
    def main(self):
        """
        Obtain data for each game in howlongtobeat
        """

        for i in range(1, 90000):

            req = requests.post(URL_LOOP + str(i))
            if req.url != "https://howlongtobeat.com/404.php":
                sc = Scrapper()
                print(i)
                print(req.url)
                print("-"*40)
                dataGame = sc.bsScrapper(req.text)
                self.__class__.dataDict[i] = dataGame

            #sleep(1)
        self.convertData()

    def convertData(self):
        """
        Transform into json and save it
        """
        gamesJson = json.dumps(self.__class__.dataDict)
        with open('hltb_games.json', 'w') as f:
            f.write(gamesJson)

if __name__ == "__main__":
    ScrapperLoop().main()
