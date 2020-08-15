import requests
import json
from time import sleep
from Scrapper import Scrapper
import sys

URL_LOOP = "https://howlongtobeat.com/game?id="

class ScrapperLoop():
    dataDict = {}
    def main(self, loopStart, loopEnd, fileName):
        """
        Obtain data for each game in howlongtobeat
        """

        for i in range(loopStart, loopEnd):

            req = requests.post(URL_LOOP + str(i))
            if req.url != "https://howlongtobeat.com/404.php":
                sc = Scrapper()
                print(i)
                print(req.url)
                print("-"*40)
                dataGame = sc.bsScrapper(req.text)
                self.__class__.dataDict[i] = dataGame
            else:
                print("Game " + i + " 404")
                print("-"*40)

            #sleep(1)
        self.convertData(fileName)

    def convertData(self, fileName):
        """
        Transform into json and save it
        """
        gamesJson = json.dumps(self.__class__.dataDict)
        with open(fileName, 'w') as f:
            f.write(gamesJson)

if __name__ == "__main__":
    if (len(sys.argv) < 4 or len(sys.argv) > 4):
        print("Ussage: python3 hltb_pages_loop.py [Initial number] [Final number] [FileName]")
        print("Initial/Final numbers are the range in which the loop will scrap data.")
        print("FileName is the name of the json savefile with the result")
    else:
        ScrapperLoop().main(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
