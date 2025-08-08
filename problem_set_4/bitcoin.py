import requests
import sys

def bitcoin():
    try:
        num = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')
    except IndexError:
        sys.exit('Missing coommand-line argument')


    try:
        response=requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=5b14991634d7e0cefae34bf44b94c16793acc7d2340e8148aabbb62f70f5c26c')
        content=response.json()
        price= (float(content['data']['priceUsd'])) * num
        round_price=round(price, 4)
    except requests.RequestException:
        sys.exit()
    except ValueError:
        sys.exit()

    print(f'${round_price:,}')



bitcoin()