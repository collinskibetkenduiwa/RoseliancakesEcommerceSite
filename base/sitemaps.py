# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.translation import get_language, activate
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')

"""
This sitemap file will generate according to the categories in database and their categories
"""

# class StaticSitemap(I18nSitemap):


class ProductSitemap(Sitemap):
    priority = 0.3
    changefreq = 'monthly'
    
    def items(self):
        return Product.objects.browsable()


class CategorySitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    
    def items(self):
        return Category.objects.all()

class Main_Pages(Sitemap):
    priority = 0.4
    changefreq = 'daily'

    def items(self):
        return ['home',]

    def location(self, item):
        return reverse(item)
  
class OtherPages(Sitemap):
    priority = 0.2
    changefreq = 'monthly'

    def items(self):
        return ['contact',]

    def location(self, item):
        return reverse(item)    