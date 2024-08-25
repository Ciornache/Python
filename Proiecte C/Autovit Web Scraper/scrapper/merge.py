import json

def mergeJsons(l:list, output:str) -> None:
    data=[]
    for jsonObject in l:
        with open(jsonObject, 'r') as f:
            data.append(json.load(f))
    with open(output, "w") as f2:
            json.dump(data, f2)

mergeJsons(['F:/Python/Autovit Web Scraper/scrapper/buffer.json', 'F:/Python/Autovit Web Scraper/scrapper/cars.json'], 'F:/Python/Autovit Web Scraper/scrapper/cars.json')