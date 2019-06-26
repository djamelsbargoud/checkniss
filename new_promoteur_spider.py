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
        new_promoteur = []
        old_promoteur = []
        with open(self.pathfile + 'new_promoteur.csv', "r", encoding="utf8") as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                new_promoteur.append(row)

        with open(self.pathfile + 'old_promoteur.csv', "r", encoding="utf8") as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                old_promoteur.append(row)

        print('============')
        print(new_promoteur)
        print('============')
        print(old_promoteur)
        print('============')
        for new in new_promoteur:
            user = new
            if new[0] is not None:
                for old in old_promoteur:
                        if new[0] == old[0] and new[1] == old[1]:
                            user = old
                            break
                        else :
                            user = new



            yield {'EMAIL' : user[0],
                    # 'num store' : user[1],
                   'tel.' : user[1] ,
                    'Manuel ispromoteur':user[2]
                    }

