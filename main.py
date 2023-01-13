from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

url = "https://www.bcv.org.ve"
info = requests.get(url, verify=False).text
content = BeautifulSoup(info, 'lxml')

coin1 = content.findChildren('div', attrs={'id':'euro'})[0]
coin2 = content.findChildren('div', attrs={'id':'yuan'})[0]
coin3 = content.findChildren('div', attrs={'id':'lira'})[0]
coin4 = content.findChildren('div', attrs={'id':'rublo'})[0]
coin5 = content.findChildren('div', attrs={'id':'dolar'})[0]
date = content.findChildren('div', attrs={'class':'pull-right dinpro center'})[0]

coins = [
    {'Euro':
        {
            'name': coin1.span.string,
            'price':coin1.strong.string,
        }
    },
    {'Yuan':
        {
            'name': coin2.span.string,
            'price':coin2.strong.string,
        }
    },
    {'Lira':
        {
            'name': coin3.span.string,
            'price':coin3.strong.string,
        }
    },
    {'Rublo':
        {
            'name': coin4.span.string,
            'price':coin4.strong.string,
        }
    },
    {'Dolar':
        {
            'name': coin5.span.string,
            'price':coin5.strong.string,
        }
    },
    {
        'Date': 'Fecha Valor : '+date.span.string
    }                
]


app = FastAPI()
@app.get('/')
def name():
    return coins
