import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from zelda_game.items import zelda_gameItem


class GameSpider(CrawlSpider):
    name = 'zelda_game'
    allowed_domain = ['www.howlongtobeat.com']
    start_urls = ['https://howlongtobeat.com/game?id=38019']
    
    rules = {
        Rule(LinkExtractor(allow ='Items/'), callback='parse_item', follow=True),
    }
    
    def parse_item(self, response):
        zg_item = zelda_gameItem()

        zg_item['game_name'] = response.xpath('//*[@class="profile_header shadow_text"]/text()').extract()
        zg_item['game_description'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[2]/p/text()').extract()
        zg_item['game_developer'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[1]/text()').extract()
        zg_item['game_publisher'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[2]/text()').extract()
        zg_item['game_pleyable_On'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[3]/text()').extract()
        zg_item['game_genres'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[4]/text()').extract()
        zg_item['game_realeases_NA'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[5]/text()').extract()
        zg_item['game_realeases_EU'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[6]/text()').extract()
        zg_item['game_realeases_JP'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[2]/div/div[7]/text()').extract()
        zg_item['game_additionalContent'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[4]/table/text()').extract()
        zg_item['game_singlePlayer'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[5]/table/text()').extract()
        zg_item['game_speedRun'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[6]/table/tbody/tr/text()').extract()
        zg_item['game_rating'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[7]/div[1]/h5/text()').extract()
        zg_item['game_retirement'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[7]/div[2]/h5/text()').extract()
        zg_item['game_platform'] = response.xpath('//*[@id="global_site"]/div[2]/div/div[2]/div[8]/div[1]/table/text()').extract()
    
        return zg_item