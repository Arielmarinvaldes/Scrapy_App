from scrapy.crawler import CrawlerProcess
import pandas as pd
from scrapy.utils.project import get_project_settings
import os

os.chdir(r"C:\Users\amval\OneDrive\Escritorio\ScrapyApp\amazontablet\amazontablet\spiders")

process = CrawlerProcess(get_project_settings())

process.crawl('amazon_tabl')
process.start()

PATH = r"C:\Users\amval\OneDrive\Escritorio\ScrapyApp\amazontablet\amazontablet\spiders\amazontabletas.csv"

df = pd.read_csv(PATH, usecols=[0, 1, 2], encoding="utf-8")
print(df)
