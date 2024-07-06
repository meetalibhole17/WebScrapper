# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQLite3/SQL/Mongo database

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import sqlite3
#
#
# class Pblsem4Pipeline(object):
#
#     def __init__(self):
#         self.curr = None
#         self.conn = None
#         self.create_connection()
#         self.create_table()
#
#     def create_connection(self):
#         self.conn = sqlite3.connect("bookinfo.db")
#         self.curr = self.conn.cursor()
#
#     def create_table(self):
#         self.curr.execute("""DROP TABLE IF EXISTS book_info""")
#         self.curr.execute("""CREATE TABLE IF NOT EXISTS book_info(
#                      product_name text,
#                      product_author text,
#                      product_price text,
#                      product_imagelink text)""")
#         # self.conn.commit()
#
#     def process_item(self, item, spider):
#         self.store_db(item)
#         return item
#
#     def store_db(self, item):
#         self.curr.execute("""INSERT INTO book_info VALUES(?,?,?,?)""", (
#             item['product_name'][0],
#             item['product_author'][0],
#             item['product_price'][0],
#             item['product_imagelink'][0]
#         ))
#         self.conn.commit()


