import unittest, os, sys
sys.path.append(os.path.abspath('..'))
from src.Scrapper import Scrapper 


class TestGeneratedJson(unittest.TestCase):
        
    scrappedData = {}

    def setUp(self):
        test =  open("testSource/zelda.html", "r")
        testData = test.readlines()
        sc = Scrapper()
        self.__class__.scrappedData = sc.bsScrapper(testData)

    def test_type(self):
        self.assertEqual(type(self.__class__.scrappedData).__name__, "dict")

    def test_basicData(self):
        self.assertEqual(self.__class__.scrappedData.name, "The Legend of Zelda: Breath of the Wild")
        self.assertEqual(self.__class__.scrappedData.description, "Forget everything you know about The Legend of Zelda games. Step into a world of discovery, exploration and adventure in The Legend of Zelda: Breath of the Wild, a boundary-breaking new game in the acclaimed series. Travel across fields, through forests and to mountain peaks as you discover what has become of the ruined kingdom of Hyrule in this stunning open-air adventure.")
        self.assertEqual(self.__class__.scrappedData.developer, "Nintendo EPD")
        self.assertEqual(self.__class__.scrappedData.publisher, "Nintendo")
        self.assertEqual(self.__class__.scrappedData.playable_On, ["Nintendo Switch", "Wii U"])
        self.assertEqual(self.__class__.scrappedData.genres, ["Third-Person", "Action", "Adventure", "Open World"])


    def test_additionalContent(self):
        self.assertEqual(self.__class__.scrappedData.additionalContent, [{"name":"The Champions' Ballad DLC", "data":["137","83%","10h","12h","14h","11h"]},
                                                    {"name":"The Master Trials DLC", "data":["76","81%","4h","7h","7h","6h"]}])

    def test_singlePlayer(self):
        self.assertEqual(self.__class__.scrappedData.singlePlayer,{
            "Main Story":["1.2K","49h 41m","50h","28h 19m","69h 55m"],
            "Main + Extras":["2.9K","97h","06m","90h","52h 38m",	"189h 16m"],
            "Completionists":["544","186h 47m","180h 43m","117h 05m","319h 22m"],
            "All PlayStyles":["4.7K","95h 09m","80h","47h 11m","271h 17m"]
        })

    def test_speedRun(self):
        self.assertEqual(self.__class__.scrappedData.speedRun, {"Any%":["8","4h 02m 55s","2h 37m 30s","59m 57s","12h 50m"]})

    def test_rating(self):
        self.assertEqual(self.__class__.scrappedData.rating, 94)
        self.assertEqual(self.__class__.scrappedData.retirement, 1.69)
        #rating distribution: #aqui vamos a tener que integrar los datos

    def test_platform(self):
        self.assertEqual(self.__class__.scrappedData.platform,{"Emulated": ["87","39h 23m","88h 06m","168h 04m","6h 48m","300h"],
                                                "Nintendo Switch": ["3.9K","50h 21m","98h 01m","187h 38m","7h 08m","455h"],
                                                "Wii U":["706","47h 14m","93h 29m","183h 43m","11h 35m","400h"]                       
                                                })
if __name__ == '__main__':
    unittest.main()