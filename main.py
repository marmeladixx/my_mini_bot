from bs4 import BeautifulSoup
import requests
import schedule
import telegram_send
import time

url = 'https://www.mediaexpert.pl/komputery-i-tablety/monitory-led/monitor-34wn700-b-ips-ultra-wide-300cd-m2-3440x1440-21-9?gclid=Cj0KCQjwm6KUBhC3ARIsACIwxBhEmAZdSf5XIqGy7edxMttl6DmPFokuj_Oy___RUmN3e4pUZb8MzcAaAjKKEALw_wcB'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
req = requests.get(url, headers= header)
src = req.text

soup = BeautifulSoup(src, 'lxml')
price = soup.find(class_= 'whole').text

def job():
    global price
    text = 'Стоимость монитора на сегодня: ' + price
    telegram_send.send(messages=[text])

schedule.every().day.at('09:00').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)