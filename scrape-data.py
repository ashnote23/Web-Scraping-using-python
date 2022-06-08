import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas
driver = webdriver.Firefox()
url = 'https://dir.indiamart.com/search.mp?ss=vermicompost&prdsrc=1'
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
indian_soup = BeautifulSoup(html, 'html.parser')
elements = indian_soup.findAll('section',{'class':['lst_cl prd-card fww brs5 pr bg1 prd-card-mtpl', 'lst_cl prd-card fww brs5 pr bg1 prd-card-mtpl mr0']})  
driver.quit()

file_path = 'indian.txt'

with open(file_path, "w")as textfile:
	for ele in elements:
		title = ele.find('a',{'class':['clr3 fs12 fwn rsrc', 'clr3 fs12 fwn rsrc']})
		lin1 = ele.findAll('span',{'class': ['elps elps2 p10b0 fs14 tac mListNme','elps elps2 p10b0 fs14 tac mListNme']})
		name=title.text
		for sup in lin1:#links generating
			ele1 = sup.find("a")
			try:
				if 'href' in ele1.attrs:
					link=ele1.get('href')
					#print(link)
			except:
				#print("\n")
				link="none"
				pass
		
		page_line = "{title},{link} \n".format(
							title=name,
							link=link
						)
		textfile.write(page_line)



dataframe = pd.read_csv(file_path,header = None)
dataframe.columns = ['Name', 'Link']
dataframe.to_csv("indian.csv",index = None)
	

