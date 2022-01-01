import requests,csv,json,os,time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url_travel = 'https://1000.taiwan.net.tw/VoucherShopList.aspx'
url_food = 'https://foodlover.tw/lookup-shop.html'
url_efun = 'https://artsfungo.moc.gov.tw/promote_s/public/page'
url_Farm = 'https://888.coa.gov.tw/Discount'
url_i_original = 'https://www.explorethesun.tw/cipshop/upload/20211229204424.pdf'
url_sports = 'https://500.gov.tw/FOAS/actions/Vendor.action?view'
url_hakka = "https://www.hakka500.tw/store/index.html"
url_creation = "https://twrr-vouchers.ndc.gov.tw/store.php"


city = ["KLU","TPE","TPH","TYC","HSC","HSH","MAL","TXG","CWH","NTO","YLH","CYI","CHY","TNN","KHH","IUH","TTT","HWA","ILN","PEH","KMN","LNN"]
"""
"KLU"基隆市	"TPE"臺北市	"TPH"新北市	"TYC"桃園市	"HSC"新竹市	"HSH"新竹縣	"MAL"苗栗縣	"TXG"臺中市	"CWH"彰化縣	"NTO"南投縣	"YLH"雲林縣	"CYI"嘉義市	"CHY"嘉義縣	"TNN"臺南市	"KHH"高雄市
"IUH"屏東縣	"TTT"臺東縣	"HWA"花蓮縣	"ILN"宜蘭縣	"PEH"澎湖縣	"KMN"金門縣	"LNN"連江縣
"""

Max = 5000

class Coupon(object):

	def __init__(self):
		super(Coupon, self).__init__()
		options = Options()
		options.add_argument("--disable-notifications")

	def get_travel(self, city):
		print('Excuting get_travel...')

		driver = webdriver.Chrome()
		driver.get(url_travel)
		select_City = Select(driver.find_element_by_name(
		    'ctl00$ContentPlaceHolder1$ddlShopCity'))
		select_City.select_by_index(city)
		txtPag = driver.find_element_by_id("ContentPlaceHolder1_txtPageSize")
		txtPag.send_keys('0')
		txtPag.submit()
		time.sleep(1)
		driver.find_element_by_xpath(
		    "//input[@type='submit' and @value='更新']").click()
		time.sleep(2)
		js = "var q=document.documentElement.scrollTop=10000000"
		driver.execute_script(js)
		time.sleep(3)

		soup = BeautifulSoup(driver.page_source, 'html.parser')
		tb = soup.find(id='ContentPlaceHolder1_GridView1')
		data_travel = pd.read_html(tb.prettify(), encoding='utf-8', header=0)[0]
		print(data_travel)
		file_name = 'data_travel_'+str(city)+'.csv'
		data_travel.to_csv(file_name, index=0, encoding='utf-8')
		driver.close()
		return data_travel

	def get_sports(self,city):
		driver = webdriver.Chrome()
		driver.get(url_sports)
		time.sleep(3)
		choose_city = Select(driver.find_element_by_name ("city"))
		# select by value 
		choose_city.select_by_value(city)
		time.sleep(2)

		for i in range(1,10):
			driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
			time.sleep(2)
			print(i)
		
		soup = BeautifulSoup(driver.page_source, 'html.parser') 
		links = soup.find('div',id='rowtest').find_all(name='a')
		data_sports_name = []
		data_sports_link = []
		for i in links:
			data_sports_name.append(i.text)
			data_sports_link.append("https://500.gov.tw/FOAS/actions/"+i.get("href"))

		data_sports_list = soup.find('div',id='rowtest').find_all('div','px-3')
		data_sports = []
		for i in data_sports_list:
			data_sports.append(i.text)


		with open('data_sports_'+city+'.csv', 'w', newline='',encoding='utf-8') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerows(zip(data_sports_name))
			writer.writerows(zip(data_sports_link))
			writer.writerows(zip(data_sports))
		driver.close()
		return data_sports	



if __name__ == '__main__':
	Coup=Coupon()
	"""
	for i in range(1,24):
		Coup.get_travel(i)
		print(i)
	
	for i in range (len(city)):
		Coup.get_sports(city[i])
		print(city[i])
	"""