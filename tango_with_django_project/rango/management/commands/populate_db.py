'''
Created on Jul 13, 2017

@author: jwang02
'''
from django.core.management.base import BaseCommand
from rango.models import Category, Page


class Command(BaseCommand):
    args = '<No command line options are needed...>'
    help = 'Use this to insert the data into Rango database'
    
    def __insert_category_page(self):
        cloud_cat = add_cat('Cloud Computing')
    
        add_page(cat=cloud_cat,
                 title="AMAZON AWS",
                 url="https://aws.amazon.com/")

        add_page(cat=cloud_cat,
                 title="Microsoft Azure",
                 url="https://azure.microsoft.com/en-us/")

        for c in Category.objects.all():
            for p in Page.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))


    def handle(self, *args, **options):
        self.__insert_category_page()
    
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c
