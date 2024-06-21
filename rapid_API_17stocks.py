import requests
from datetime import datetime
from tabulate import tabulate

# Function to fetch stock details for a given symbol
def fetch_stock_details(symbol):
    url = "https://real-time-finance-data.p.rapidapi.com/stock-overview"
    querystring = {"symbol": symbol, "language": "en"}
    headers = {
        "x-rapidapi-key": "709ec67693msh579df1437015176p131167jsn0cabe74a07de",
        "x-rapidapi-host": "real-time-finance-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        try:
            data = response.json()['data']
            stock_details = {
                "Symbol": data['symbol'],
                "Name": data['name'],
                "Date": datetime.strptime(data['last_update_utc'], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d'),
                "Open Price": f"{data['open']} USD",
                "High Value": f"{data['high']} USD",
                "Low Value": f"{data['low']} USD",
                "Previous Close": f"{data['previous_close']} USD",
                "Volume": f"{data['volume']}",
                "Market Cap": f"{data['company_market_cap']} USD",
                "Exchange": f"{data['exchange']} ({data['primary_exchange']})",
                "Currency": f"{data['currency']}"
            }
            return stock_details
        except KeyError:
            print(f"Error: Required data fields not found for symbol {symbol}")
    else:
        print(f"Error: Unable to fetch data for symbol {symbol} (Status code: {response.status_code})")

# List of top 17 stocks from Indian market (example)
top_stocks = [
    "INFY", "RELIANCE", "TCS", "HDFC", "HDFCBANK",
    "ICICIBANK", "HINDUNILVR", "ITC", "SBI", "BAJFINANCE",
    "AXISBANK", "MARUTI", "KOTAKBANK", "ONGC", "LT",
    "NTPC", "INDUSINDBK"
]

def main():
    stock_details_all = []
    for symbol in top_stocks:
        stock_details = fetch_stock_details(symbol)
        if stock_details:
            stock_details_all.append(stock_details)

    # Display all fetched stock details in a tabular format
    if stock_details_all:
        print("\nStock Details for Top 17 Indian Stocks:\n")
        headers = ["Symbol", "Name", "Date", "Open Price", "High Value", "Low Value", "Previous Close", "Volume", "Market Cap", "Exchange", "Currency"]
        data_rows = [[
            stock['Symbol'], stock['Name'], stock['Date'], stock['Open Price'], stock['High Value'],
            stock['Low Value'], stock['Previous Close'], stock['Volume'], stock['Market Cap'],
            stock['Exchange'], stock['Currency']
        ] for stock in stock_details_all]
        print(tabulate(data_rows, headers=headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
