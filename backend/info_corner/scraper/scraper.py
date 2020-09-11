# Scraper to find hotspots in NSW
# Run with "scrapy runspider scraper.py"
import scrapy

hotspots = {
    "New South Wales": [],
    "Victoria": [],
    "Australian Capital Territory": [],
    "South Australia": [],
    "Western Australia": [],
    "Northern Territory": [],
    "Tasmania": []
}

class Hotspot:
    def __init__(self, suburb, start_date, start_time):
        self.suburb = suburb
        self.start_date = start_date
        self.start_time = start_time

class HotspotScraper(scrapy.Spider):
    name = "hotspot_spider"
    start_urls = ['https://www.qld.gov.au/health/conditions/health-alerts/coronavirus-covid-19/current-status/hotspots-covid-19']

    def parse(self, response):
        table = response.xpath('//table[@id="table20116"]//tbody')
        rows = table.xpath('//tr')[2:]

        # Initial key in <thead>, others in <tbody>
        # Scrapy returning all tables instead of only specified id
        # Cleaning data for only current hotspots
        state_key = "New South Wales"
        for row in rows:
            if row.xpath('td//text()'):
                # print(row.xpath('td//text()')[0].extract().strip())#, row.xpath('td//text()')[1].extract().strip(), row.xpath('td//text()')[2].extract().strip())
                try:
                    end_date = row.xpath('td//text()')[3].extract().strip()
                except:
                    continue    
                
                if end_date == 'Current':
                    suburb = row.xpath('td//text()')[0].extract().strip()
                    start_time = row.xpath('td//text()')[1].extract().strip()
                    start_date = row.xpath('td//text()')[2].extract().strip()
                    hotspots[state_key].append(Hotspot(suburb, start_date, start_time))

            elif row.xpath('th//strong'):
                state_string = row.xpath('th//strong//text()')[0].extract()
                for key in hotspots.keys():
                        if key in state_string:
                            state_key = key
                            break
            else:
                continue

        print("Hotspots:")
        for state in hotspots.keys():
            if hotspots[state] != []:
                print(state + ":")
                for hotspot in hotspots[state]:
                    print(hotspot.suburb, "since", hotspot.start_date, "at", hotspot.start_time)                             