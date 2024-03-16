from bs4 import BeautifulSoup

with open('scraping/test.html', 'r') as html_file:
    cont = html_file.read() # todo o conteúdo do html

    print(cont)

    soup = BeautifulSoup(cont, 'lxml') # cria um objeto BeautifulSoup

    print(soup.prettify()) # conteúdo identado (estética)

    tags = soup.find_all('li') # soup.find encontra somente a primeira tag 'li' .find_all retorna uma lista com todas encontradas
    print(tags)

    for course in tags:
        print(course.text) # printa somente o conteúdo textual contido dentro de cada tag

    course_cards = soup.find_all('div', class_="card") # usa o underline_ por conta do class ser uma palavra reservada da linguagem

    print('Shapes')
    # for course in course_cards:
    #     print(course.p.text.split()[1]) # split só funciona com o .text
    #     print(course.span.text)

    brand = []
    price = []
    
    for course in course_cards: # separando todas as tags div com o class="card" em duas listas
        brand.append(course.p.text.split()[1])
        price.append(course.span.text)

print(brand, price)