# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQLite3/SQL/Mongo database

import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import pymongo
#
# import mysql.connector as mysql
#
#


class QuotePipeline(object):

    def __init__(self):
        self.curr = None
        self.conn = None
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""CREATE TABLE quotes_tb (
                    title text,
                    author text,
                    tag text
                    )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO quotes_tb VALUES (?,?,?)""", (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
#
#
# # class QuotePipeline(object):
# #
# #     def __init__(self):
# #         self.conn = pymongo.MongoClient(
# #             'localhost',
# #             27017
# #         )
# #         db = self.conn['myquotes']
# #         self.collection = db['quotes_tb']
# #
# #     def process_item(self, item, spider):
# #         self.collection.insert(dict(item))
# #         return item
