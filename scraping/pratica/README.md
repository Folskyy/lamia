Com o script **exec.sh** é realizado o scraping de detalhes de vagas de emprego para programação,
excluindo vagas que possuem a skill que o usuário informou não ter usando o programa **scraping.py**
que retornaŕa o arquivo **jobs_logs.md** na pasta output.

Em seguida é feito um processo de ranqueamento das palavras resultantes do scraping no programa
**key_count.py**, que por sua vez retornará o arquivo **rank_words.md** na pasta output.

O arquivo **key_count.py** é imprimido na tela e o script é encerrado.

*Obs: Tô aprendendo a fazer alguns scripts em shell e só queria usar em alguma coisa :)*
