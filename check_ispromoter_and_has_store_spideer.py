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
        with open(self.pathfile + 'all_user.csv', "r", encoding="utf8") as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                all_user.append(row)

        with open(self.pathfile + 'email_phone_promoteur.csv', "r", encoding="utf8") as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                user_promoteur.append(row)

        with open(self.pathfile + 'store_mail_phn.csv', "r", encoding="utf8") as my_file:
            reader = csv.reader(my_file)
            for row in reader:
                user_store.append(row)


        print('============')
        print(all_user)
        print('============')
        print(user_promoteur)
        print('============')
        print(user_store)
        for user in all_user:
            has_store = False
            tel = user[1]
            ispromoteur = False

            if user[0] is not None:
                # checker si il a un store
                for store in user_store:
                        if user[0] == store[0]:
                            has_store = True
                            tel1= store[1]
                            tel = user[1]
                            break
                        else :
                            has_store =False
                            tel = user[1]
                            tel1 = ''
                # checker si c'est un promoteur
                for promoteur in user_promoteur:
                        if user[0] == promoteur[0]:
                            ispromoteur = True
                            break
                        else :
                            ispromoteur =False


            yield {'user' : user[0],
                   'ispromoteur':ispromoteur,
                   'tel.' : tel ,
                   'tel. 1' : tel1 ,
                    'has_store' : has_store
                    }

