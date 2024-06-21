import requests

# Your Twelve Data API key
API_KEY = '739e405083604c21967dc03d85875f02'

# API endpoint for stock list from NSE or BSE
BASE_URL = 'https://api.twelvedata.com/stocks'

def get_stock_list(exchange):
    params = {
        'exchange': exchange,
        'apikey': API_KEY
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        stock_data = response.json()
        return stock_data
    else:
        print(f"Error: Unable to fetch data (Status code: {response.status_code})")
        return None

def main():
    # Get stock list for NSE
    nse_stocks = get_stock_list('NSE')
    if nse_stocks:
        print("NSE Stock List:")
        for stock in nse_stocks.get('data', []):
            print(f"{stock['symbol']}: {stock['name']}")
    
    # Get stock list for BSE
    bse_stocks = get_stock_list('BSE')
    if bse_stocks:
        print("\nBSE Stock List:")
        for stock in bse_stocks.get('data', []):
            print(f"{stock['symbol']}: {stock['name']}")

if __name__ == '__main__':
    main()
