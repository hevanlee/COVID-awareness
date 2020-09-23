# Scraper to find hotspots in NSW
# Run with "scrapy runspider scraper.py"

# hotspots.json format:
# {"New South Wales": 
#   [
#     {
#       "suburb": "Albury", 
#       "start_date": "8 August 2020", 
#       "start_time": "1.00 am"
#     }
#   ]
# }

import scrapy
import json
from datetime import datetime

class HotspotScraper(scrapy.Spider):
    name = "hotspot_spider"
    start_urls = ['https://www.qld.gov.au/health/conditions/health-alerts/coronavirus-covid-19/current-status/hotspots-covid-19']

    def parse(self, response):
        
        hotspots = {
            "New South Wales": [],
            "Victoria": [],
            "Queensland": [],
            "Australian Capital Territory": [],
            "South Australia": [],
            "Western Australia": [],
            "Northern Territory": [],
            "Tasmania": []
        }

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
                    hotspot = {
                        "suburb" : [],
                        "start_date": [],
                        "start_time": []
                    }

                    hotspot["suburb"] = row.xpath('td//text()')[0].extract().strip()
                    hotspot["start_time"] = row.xpath('td//text()')[1].extract().strip()
                    hotspot["start_date"] = row.xpath('td//text()')[2].extract().strip()
                    hotspots[state_key].append(hotspot)

            elif row.xpath('th//strong'):
                state_string = row.xpath('th//strong//text()')[0].extract()
                for key in hotspots.keys():
                        if key in state_string:
                            state_key = key
                            break
            else:
                continue
        
        for state in hotspots.keys():
            hotspots[state] = sorted(hotspots[state], key=lambda k: k["suburb"]) 

        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        hotspots["Last updated"] = date_time

        with open("public/backend/info_corner/scraper/hotspots.json", 'w') as outfile:
            json.dump(hotspots, outfile, ensure_ascii = False)
