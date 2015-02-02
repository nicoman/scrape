# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class LivingSocialDeal(Item):
    """Livingsocial container (dictionary-like object for scraped data"""

    # Scrapy only have one field type
    title = Field()
    link = Field()
    location = Field()
    original_price = Field()
    price = Field()
    end_date = Field()