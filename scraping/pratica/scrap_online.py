from bs4 import BeautifulSoup
from colorama import Fore, Style
import requests

# obtendo o html da página
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text

# transformando o html em uma estrutura para o BeautifulSoup
soup = BeautifulSoup(html_text, 'lxml')

# atribui a jobs uma lista de cards de vagas 
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

unfamiliar_skill = input('Put some skill that youre not familiar with\n> ')

print(f"Filtering out {unfamiliar_skill}")

# abre um arquivo md para salvar as vagas encontradas
with open ('job_logs.md', 'w') as file:
    count = 1
    for job in jobs: # itera sobre todos os cards de cada vaga atribuida a variavel jobs
        # atribui cada uma das informações desejadas da vaga a uma variavel
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '').replace('\n', '')
        job_description = job.find('ul', class_ = 'list-job-dtl clearfix').text.replace('\n', '')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '').replace('\n', '')
        
        # acessa o conteúdo dentro da tag <a> que esta dentro de <h2> que esta dentro da tag <header>
        more_info = job.header.h2.a.text

        # a vaga só é salva no arquivo caso a skill inserida anteriormente não esteja na variável skills (não seja exigida na vaga)
        if unfamiliar_skill not in skills:
            file.write(f"# {more_info.strip().lower()} #\n")
            file.write(f"**Company name:** {company_name.strip().lower()}\n")
            file.write(f"**Skills:** {skills.strip().lower()}\n")
            file.write(f"**Job Description:** {job_description.strip().lower()}\n\n")
            
            print(f"Job saved: line {count}")
            
            count += 6
