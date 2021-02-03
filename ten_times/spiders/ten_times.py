# -*- coding: utf-8 -*-
import time
import json
import scrapy
import selenium
import re
import os.path

from scrapy import Spider
from scrapy.selector import Selector

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def hasNumbers(inputString):
        return bool(re.search(r'\d', inputString))

class TenTimesSpider(Spider):
    name = 'ten_times'
    allowed_domains = ['10times.com/']
    start_urls = ['https://10times.com/usa/tradeshows?datefrom=2021-04-24&dateto=2021-04-30']

    def parse(self, response):
        self.logger.info("procesing: "+response.url)
        
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--incognito")
        options.add_argument("--disable-extensions")
        options.add_argument(" --disable-gpu")
        options.add_argument(" --disable-infobars")
        options.add_argument(" -–disable-web-security")
        options.add_argument("--no-sandbox")
        caps = options.to_capabilities()
        self.driver = webdriver.Chrome('/Users/mmt8856/Downloads/chromedriver', desired_capabilities=caps)
        self.driver.get('https://10times.com/usa/tradeshows?datefrom=2021-04-24&dateto=2021-04-30')
        
        #home page
        # search_city = self.driver.find_element_by_xpath('//*[@id="explore-keywords"]').send_keys('Events in UAE')
        # time.sleep(3.8)
        # drop_down_selector = self.driver.find_element_by_xpath('//*[@id="kamal"]')
        # drop_down_selector.click()
        # time.sleep(5.9)
        
        #catalogue page with an infinite scroll
        # last_height = self.driver.execute_script("return document.body.scrollHeight")
        # SCROLL_PAUSE_TIME = 6.8
        # i=0
        # while True:
        # # while i < 1:
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(SCROLL_PAUSE_TIME+i)
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
        #     i+=1
        #     time.sleep(2.2)
        # try:
        #     modal_window = self.driver.find_element_by_xpath('//*[@id="_modal_close"]')
        #     modal_window.click()
        # except Exception as e:
        #     self.logger.info("exception for modal window is = " + str(e))
        
        # #fetch all the event urls
        # scrapy_selector = Selector(text = self.driver.page_source)
        # events_selector = scrapy_selector.xpath('//*[@aria-label="evt_bkmrk"]') #returns the list of selectors
        # self.logger.info('Theres a total of ' + str(len(events_selector)) + ' links.')
        # event_urls_distinct = []
        
        # # create a distinct list of event urls
        # try:
        #     s = 0
        #     event_selector = events_selector[0]
        #     for url in event_selector.xpath('//@data-url').extract():
        #         if url not in event_urls_distinct:
        #             #print("url = ", url)
        #             event_urls_distinct.append(url)
        #         else:
        #             print("duplicate url = ", url)
        #         s = s+1
        # except Exception as e:
        #     self.logger.info('Reached last iteration #' + str(s))
        #     self.logger.info("exception is = " + e)
        
        # Opening JSON file
        file_path = '/Users/mmt8856/Documents/Mac-personal-asianet/a1-shows/ten_times/data/url.json'
        f = open(file_path)
        # event_urls_distinct = json.load(f)['events_url_arr']
        # print("event_urls_distinct = ", event_urls_distinct)
        
        # fetch the event details from every event url
        organizer_links_distinct = []
        # q = 0
        # self.logger.info("event_urls_distinct length = " + str(len(event_urls_distinct)))
        # for event_url in event_urls_distinct:
        #     try:
        #         self.logger.info("event_url = " + event_url)
        #         self.logger.info('Event #' + str(q))
        #         self.driver.get(event_url)
        #         q = q+1
        #         sleep_time = (int(q/100)+1)*10
        #         time.sleep(q/sleep_time)
        #         self.logger.info("sleep time for events = "  + str(q/sleep_time))
        #         link_to_home = event_url
        #         event_scrapy_selector = Selector(text = self.driver.page_source)
        #         event_json_string = event_scrapy_selector.xpath('//*[@type="application/ld+json"]/text()').extract_first()
        #         event_schema_json = json.loads(event_json_string)
                
        #         # scraping event metadata started
        #         visitors = event_scrapy_selector.css('table.table.noBorder.mng tr')[1].css('td a[href*=visitors]::text').get()
        #         if visitors is not None and hasNumbers(visitors):
        #             exhibitors = event_scrapy_selector.css('table.table.noBorder.mng tr')[1].css('td a[href*=exhibitors]::text').get()
        #             if exhibitors is not None and hasNumbers(exhibitors):
        #                 pass
        #             else:
        #                 exhibitors = event_scrapy_selector.css('table.table.noBorder.mng tr')[1].css('td::text').get()
        #         else:
        #             visitors = event_scrapy_selector.css('table.table.noBorder.mng tr')[1].css('td::text')[0].get()
        #             exhibitors = event_scrapy_selector.css('table.table.noBorder.mng tr')[1].css('td::text')[1].get()

        #         event_metadata = {
        #             "ep": event_scrapy_selector.css('section#exhib p.desc::text').get(),
        #             "timing": event_scrapy_selector.css('tr#hvrout1 td::text').get(),
        #             "type": event_scrapy_selector.css('td#hvrout2::text').get(),
        #             "category": event_scrapy_selector.css('td#hvrout2 a::text').get(),
        #             "participants_visitors": visitors,
        #             "participants_exhibitors": exhibitors
        #         }
        #         for attr, value in event_metadata.items():
        #             if(event_metadata[attr] is not None):
        #                 event_schema_json[attr] = value.strip()
        #         # scraping event metadata ends
                
        #         self.logger.info("event name = " + event_schema_json["name"])
        #         event_schema_json["organizer_name"] = event_scrapy_selector.xpath('//*[@id="org-name"]/text()').extract_first()
        #         self.logger.info("Organizer Name = " + event_schema_json["organizer_name"])
        #         event_schema_json["organizer_link"] = event_scrapy_selector.xpath('//*[@id="org-name"]/@href').extract_first()
        #         if event_schema_json["organizer_link"] not in organizer_links_distinct and event_schema_json["organizer_link"] is not None:
        #             organizer_links_distinct.append(event_schema_json["organizer_link"])

        #         yield event_schema_json
        #     except Exception as e:
        #         self.logger.info("exception is = " + str(e))
        #         continue
        #     else:
        #         continue
    
        organizer_links_distinct = json.load(f)['organisers_url_arr']
        # print("organizer_links_distinct = ", organizer_links_distinct)

        # fetch organizer details from organizer url
        self.logger.info("organizer link length = " + str(len(organizer_links_distinct)))
        j = 0
        for organizer_link in organizer_links_distinct:
            try:
                self.logger.info('Organizer #' + str(j))
                self.logger.info("organizer_link = " + organizer_link)
                self.driver.get(organizer_link)
                organizer_scrapy_selector = Selector(text = self.driver.page_source)
                organizer_json_string = organizer_scrapy_selector.xpath('//*[@type="application/ld+json"]/text()').extract_first()
                organizer_schema_json = json.loads(organizer_json_string)
                
                yield organizer_schema_json
                sleep_time = (int(j/100)+1)*10
                time.sleep(j/(sleep_time))
                self.logger.info("sleep time for organizers = " + str(j/(sleep_time*2)))
                j = j+1
            except Exception as e:
                self.logger.info("exception is = " + str(e))
                continue
            else:
                continue
        
        self.driver.close()
