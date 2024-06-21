import requests
import csv

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

def save_to_csv(filename, stock_data, exchange):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Symbol", "Name", "Exchange"])
        for stock in stock_data.get('data', []):
            writer.writerow([stock['symbol'], stock['name'], exchange])

def main():
    # Get stock list for NSE
    nse_stocks = get_stock_list('NSE')
    if nse_stocks:
        print("NSE Stock List:")
        for stock in nse_stocks.get('data', []):
            print(f"{stock['symbol']}: {stock['name']}")
        save_to_csv('nse_stocks.csv', nse_stocks, 'NSE')
    
    # Get stock list for BSE
    bse_stocks = get_stock_list('BSE')
    if bse_stocks:
        print("\nBSE Stock List:")
        for stock in bse_stocks.get('data', []):
            print(f"{stock['symbol']}: {stock['name']}")
        save_to_csv('bse_stocks.csv', bse_stocks, 'BSE')

if __name__ == '__main__':
    main()
