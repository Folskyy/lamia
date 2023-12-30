from bs4 import BeautifulSoup
from colorama import Fore, Style
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text

html_text

soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')

company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').replace('\n', '')
company_name

job_description = job.find('ul', class_ = 'list-job-dtl clearfix').text.replace('\n', '')
job_description

skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').replace('\n', '')
skills