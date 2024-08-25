import subprocess

command = [
    'scrapy', 'runspider', 
    r'F:\Python\Autovit Web Scraper\scrapper\scrapper\spiders\spider1.py',
    '-O', 
    r'F:\Python\Autovit Web Scraper\scrapper\buffer.json'
]

result = subprocess.run(command, capture_output=True, text=True)

command = [
    'python', '-u', 'F:\Python\Autovit Web Scraper\scrapper\merge.py'
]

subprocess.run(command, capture_output=False, text=True)