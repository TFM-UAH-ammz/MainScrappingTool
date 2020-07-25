import scrapy

class GameItems(scrapy.Item):
    
    game_title = scrapy.Field()
    game_profiledetails = scrapy.Field()
    game_times = scrapy.Field()
    game_profileinfo = scrapy.Field()
    game_additionalcontent = scrapy.Field()
    game_timetable = scrapy.Field()
    game_chart = = scrapy.Field()
    game_userratings = scrapy.Field()
    game_platformtable = scrapy.Field()


from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from game.items import GameItems

class GameSpider(CrawlSpider):
    name = 'game'
    allowed_domain = ['www.howlongtobeat.com']
    start_url = ['https://howlongtobeat.com/game?id=38019']
    
    rules = {
        Rule(LinkExtractor(allow ='Items/'), callback='parse_item', follow=True),
    }
    
    def parse_item(self, response):
        i = GameItem()
        i['game_title'] = response.xpath('//div[@class="profile_header shadow_text"]').extract()
        i['game_profiledetails'] = response.xpath('//div[@class="profile_details"]').extract()
        i['game_times'] = response.xpath('//div[@class="game_times"]').extract()
        i['game_profileinfo'] = response.xpath('//div[@class="profile_info"]').extract()
        i['game_additionalcontent'] = response.xpath('//div[@class="in scrollable back_primary shadow_box"]').extract()
        i['game_timetable'] = response.xpath('//table[@class="game_main_table"]').extract()
        i['game_chart'] = response.xpath('//div[@class="in game_chart back_form shadow_box"]').extract()
        i['game_userratings'] = response.xpath('//div[@class="in game_chart_rev back_form shadow_box"]').extract()
        i['game_platformtable'] = response.xpath('//div[@class="in shadow_box back_primary"]').extract()
        return i