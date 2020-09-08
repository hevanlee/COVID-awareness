# Scraper to find hotspots in NSW
import scrapy

hotspots = []
class Hotspot:
    def __init__(self, suburb, location, dates, notes):
        self.suburb = suburb
        self.location = location
        self.dates = dates 
        self.notes = notes

class HotspotScraper(scrapy.Spider):
    name = "hotspot_spider"
    start_urls = ['https://www.nsw.gov.au/covid-19/latest-news-and-updates']

    def parse(self, response):
        set_selector = '.nsw-table-responsive'
        for 


'''
        table = response.xpath('//*[@id="table20116"]//tbody')
        rows = table.xpath('//tr')[2:]
        for row in rows:
            if row.xpath('td//text()'):
                suburb = row.xpath('td//text()')[0].extract()
                start_time = row.xpath('td//text()')[1].extract()
                start_date = row.xpath('td//text()')[2].extract()
                hotspots.append(Hotspot(suburb, start_date, start_time))
            else:
                continue

'''
print("Hotspots:", hotspots)
            

