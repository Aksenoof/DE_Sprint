# парсинг данных о вакансиях python разработчиков с сайта hh.ru в colab
# установка нужных библиотек в colab
#!apt install chromium-chromedriver
#!pip install selenium
#!pip install webdriver_manager

from selenium import webdriver
from bs4 import BeautifulSoup
import json
import tqdm
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

data = {
	"data": []
}
for page in range(1, 40):
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	driver = webdriver.Chrome('chromedriver', options=options)
	url = 'https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA' \
		  '&salary=&clusters=true&area=113&ored_clusters=true&enable_snippets=true&customDomain=1'
	driver.get(url)
	html = driver.page_source
	soup = BeautifulSoup(html, 'lxml')
	tag = soup.find_all(attrs={"class": "serp-item__title"})
	for iter in tqdm.tqdm(tag):
		driver.get(iter.attrs ["href"])
		html_page = driver.page_source
		soup_page = BeautifulSoup(html_page, 'lxml')
		title = soup_page.find(attrs={"class": "bloko-header-section-1"})
		work_experience = soup_page.find(attrs={"data-qa": "vacancy-experience"})
		salary = soup_page.find(attrs={"data-qa": "vacancy-salary"})
		region1 = soup_page.find(attrs={"data-qa": "vacancy-view-raw-address"})
		region2 = soup_page.find(attrs={"data-qa": "vacancy-view-location"})

		if region1==None:
			region = region2.text.split(',')
		elif region2==None:
			region = region1.text.split(',')

		data ["data"].append({"title": title.text, "work_experience": work_experience.text, "salary": salary.text,
							  "region": region [0]})

		with open("data.json", "w") as file:
			json.dump(data, file, ensure_ascii=False)