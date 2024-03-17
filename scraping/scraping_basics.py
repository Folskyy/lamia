from bs4 import BeautifulSoup
import requests # fazer requisições HTTP

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text # recebe o html do site em formato de texto

html_text

soup = BeautifulSoup(html_text, 'lxml') # trnsforma o texto html em um objeto

jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx') # retorna todas as tags li com a classe clearfix job-bx wht-shd-bx

job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx') # retorna a primeira tag li com a classe clearfix job-bx wht-shd-bx

company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').replace('\n', '')
company_name

job_description = job.find('ul', class_ = 'list-job-dtl clearfix').text.replace('\n', '')
job_description

skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').replace('\n', '')
skills