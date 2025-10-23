# Template scraper (adapt selectors per site). Save output to backend/static/data/empresas.json
import requests, json, os, time
from bs4 import BeautifulSoup

SOURCES = []

OUT = os.path.join('backend','static','data','empresas.json')

def main():
    all_items=[]
    for s in SOURCES:
        try:
            r = requests.get(s['url'], headers={'User-Agent':'reloadbot/1.0'}, timeout=15)
            r.raise_for_status()
            soup = BeautifulSoup(r.text,'html.parser')
            # parse accordingly...
        except Exception as e:
            print('err', e)
        time.sleep(1)
    # write empty array if none
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,'w',encoding='utf-8') as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)
    print('Saved',len(all_items),'items to', OUT)

if __name__=='__main__':
    main()
