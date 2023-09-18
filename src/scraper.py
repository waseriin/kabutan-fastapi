import requests
from bs4 import BeautifulSoup
import json

class Scraper():
    def kabutan_search(self, stock_code):
        # ウェブサイトのURL
        url = f"https://kabutan.jp/stock/kabuka?code={stock_code}&ashi=shin"

        # HTTP GETリクエストを送信してページのHTMLを取得
        response = requests.get(url)

        # HTMLをBeautifulSoupで解析
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {}

        # 銘柄コードと銘柄名を取得
        h2_element = soup.find('h2')
        stock_code = h2_element.find(string=True, recursive=True)
        stock_name = h2_element.find(string=True, recursive=False)
        data['id'] = stock_code
        data['name'] = stock_name

        # 日付、売り残、買い残を取り出す
        table = soup.find('table', class_='stock_kabuka_dwm')
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')

        body = []
        for row in rows:
            columns = row.find_all('td')
            date = row.find('time')['datetime']
            sell_remain = columns[4].get_text().replace(',', '')
            buy_remain = columns[5].get_text().replace(',', '')
            body.append({
                'date': date,
                'sell_remain': sell_remain,
                'buy_remain': buy_remain
            })

        data['body'] = body

        return data
