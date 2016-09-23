from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import LivingSocialDeal


class LivingSocialSpider(BaseSpider):
    """
    Spider for regularly updated livingsocial.com site, San Francisco page
    """

    # Spider name
    name = "livingsocial"
    # Base urls list
    allowed_domains = ["livingsocial.com"]
    # Start crawling from this urls list
    start_urls = ["https://www.livingsocial.com/cities/15-san-francisco"]

    # XPath Selectors - define which elements to look at in HTML
    deals_list_xpath = '//li[@dealid]'
    # Relative to deals_list_xpath
    item_fields = {
        'title': './/span[@itemscope]/meta[@itemprop="name"]/@content',
        'link': './/a/@href',
        'location': './/a/div[@class="deal-details"]/p[@class="location"]/text()',
        'orig_price': './/a/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/div[@class="strikethrough-wrapper"]/text()',
        'curr_price': './/a/div[@class="deal-prices"]/div[@class="deal-price"]/text()',
        'end_date': './/span[@itemscope]/meta[@itemprop="availabilityEnds"]/@content'
    }


    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link
        """
        # Gives ability to select parts of response defined in deals_list_xpath
        selector = HtmlXPathSelector(response)

        # Iterate through found deals
        for deal in selector.xpath(self.deals_list_xpath):
            # Loads data into item fields defined in items.py
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

            # Define processors for clean up and joining elements
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # Iterate over item_fields dict and add xpaths to loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
