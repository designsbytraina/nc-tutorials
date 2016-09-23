from scrapy.item import Item, Field

class LivingSocialDeal(Item):
    """Livingsocial object for scraped data, inherits from Item."""

    # Define items/metadata for scrapy
    title = Field()
    link = Field()
    location = Field()
    orig_price = Field()
    curr_price = Field()
    end_date = Field()
