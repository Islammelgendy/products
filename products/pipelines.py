# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ProductsPipeline:
    def __init__(self):
        self.create_connection()
        self.creat_table()

    def create_connection(self):
        self.conn = sqlite3.connect('products.db')
        self.curr = self.conn.cursor()

    def creat_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS products_tb""")
        self.curr.execute("""CREATE TABLE products_tb(
            title text ,
            url text,
            tag text

        ) """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into products_tb values(?,?,?)""", (
            item['title'],
            item['url'],
            item['category']


        ))
        self.conn.commit()
