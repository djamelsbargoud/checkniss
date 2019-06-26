import string

import scrapy
import csv
from pyquery import PyQuery as pq


class CleanUrlSpider(scrapy.Spider):
    name = "cleanurl"
    incr = 1
    pathfile = "/home/djamel/scrapy/juritravail.com/juritravail/juritravail/spiders/"

    def start_requests(self):
        urls = ['https://consultation.avocat.fr/avocats/par-departement.php']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_user = []
        user_promoteur = []
        user_store = []
        with open(self.pathfile + 'all_user_checked.csv', "r", encoding="utf8") as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                all_user.append(row)

        with open(self.pathfile + 'non_promo_non_store.csv', "r", encoding="utf8") as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                user_promoteur.append(row)

        print('============')
        print(all_user)
        print('============')
        print(user_promoteur)


        for promoteur in user_promoteur:
                tel = ''
                # add phone in promoteur user
                for user in all_user:
                    if user[0] is not None:
                        if user[0] == promoteur[0]:
                            tel = user[2]
                            break



                yield {'EMAL' : promoteur[0],
                       'has_store': promoteur[1],
                       'ispromoteur': promoteur[2],
                       'Tel': tel,
                        }

