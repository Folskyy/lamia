docker container create --name alpine_test alpine # cria um container  usando o SO alpine como imagem

docker container create --name ubuntu_test ubuntu # cria um container usando o SO ubuntu como imagem

docker container ls -a # listagem dos containers (-a para mostras os itens ocultos)
docker image ls -a # listagem das imagens locais
docker image ls alpine # listagem das imagem com 'alpine' no nome

docker container rm ubuntu_test # remoção de um container
docker container ls -a # listagem após a remoção

docker container rm alpine_test # remoção de um container
docker container ls -a # lsitgem após a remoção

docker container create --name test -it alpine sh
# o parametro -i permite a interação com o container atraves do seu terminal
# o parametro -t simula um pseudo-terminal para facilitar a interação dentro do container
# o parametro sh indica o pseudo-terminal que será simulado. 'ash' (bash) é o padrão
### OBS: CTRL+P + CTRL+Q para desconectar do container sem encerrá-lo (só funciona se o container tiver um pseudo-terminal). ###
docker container start test # inicia o container 'test' (pode ser usado os primeiros char do id do container como alternativa), mas não conecta ao container.

docker container exec test ls # exec: executa o comando ls no container test mesmo não conectado a ele
docker container exec test touch notes.md # cria o arquivo 'notes.md'
docker container exec test ls # lista com o notes.md adicionado

mkdir allumy # criando um diretório na máquina para ser usado em um container
touch allumy/hello.txt

docker container exec test ls
docker container cp allumy test:/ # copia o diretório allumy da máquina para o diretório / do container test
docker container exec test ls # diretório allumy inserido no container
docker container exec test ls allumy # listagem do diretorio allumy

docker container attach test # conecta ao container antes inicializado.
	cd allumy
	echo "TESTE DE ATTACH" > hello.txt
	cat hello.txt
	exit # container é encerrado ao sair

docker container start -ia test # inicia na forma interativa (-i/--interactive) e conectado ao conteiner (-a/-attach)
	exit

docker container run -it --name test_2 alpine sh # cria, inicia e conteca ao container. Alternativa ao docker crate/docker start
	# comandos shell dentro do container:
	ls
	touch note.md
	echo "TESTE DE INICIALIZAÇÃO INTERATIVA" > note.md
	cat note.md
	ls
	exit

docker container ls -a
docker container rename test_2 test2 # renomeia o container 'test_2' para 'test2'
docker container ls -a # listagem após renomear o container

docker stop test test2 # paralisação os containers

docker container logs test # apresenta os últimos comandos executados no container
docker container inspect test # informações detalhadas do container

docker container rm test test2 # remoção dos containers

# CONTAINERS SÃO DESCARTÁVEIS #

### MAPEAMENTO DE VOLUMES ###
docker run -v allumy: --name test-volume -it alpine ash # mapeamento do volume 'allumy'
# diferente da cópia de um volume, o mapeamento usa um ponteiro do volume para ser usado no container. Assim, as alterações são feitas universalmente

docker run -it --name alpine-docker -v /data alpine
	ls
	cd data
	mkdir allumy
	cd allumy
	touch dockerfile
	# ctrl+p ctrl+q

docker volume ls
docker volume inspect 'VOLUME NAME' # conseguimos obter o endereço da pasta 'data' na máquina local

docker volume create teste-volume # cria um volume com o nome personalizado

### MAPEAMENTO DE PORTAS ###
docker container run -d -p 80:80 --name nginx nginx
# OBS: pode haver problemas sem a declaração explicita '-p' da porta
# 80:80 -> mapear a porta 80 do host na porta 80 do container
# para acessar entrar em localhost:**porta mapeada** ou *docker inspect* e acessar o IPaddress

### CONCEITO DE IMAGEM ###
docker container run --name nginx-allumy -it alpine sh
	# alterações no container
	mkdir allumy
	cd allumy
	touch docker
	echo "teste container para imagem" > docker

	cat docker
	exit

docker container commit nginx-allumy nginx-allumy-img # salva o container como uma imagem
docker image ls

docker container run -it --rm nginx-allumy-img sh # inicia um container com a imagem anteriormente salva
	# checando se as alterações estão na imagem
	ls
	cd allumy
	ls
	cat docker
	exit
# o --rm exclui o container logo após ser encerrado

docker image save -o nginx-allumy.tar nginx-allumy-img # salva a imagem como um arquivo .tar
ls # verifica se o arquivo foi gerado

docker image ls # lista das imagens
docker image rm nginx-allumy-img # remoção da imagem do banco de imagens do dokcer
docker image ls # verifica se foi removida

docker image load -i nginx-allumy.tar # importa a imagem a partir do arquivo tar salvo anteriormente.
# o nome da imagem é salvo no arquivo, a imagem não herda o nome do arquivo ao carregá-la

docker image ls

docker image history nginx-allumy # histórico desde que a imagem atual foi criada

### (IM/EX)PORTAÇÃO DE CONTAINERS ###
docer container run --name test-export -it ubuntu

docker container export test-export -o test-export.tar # exportação do container para um arquivo tar
docker image import test-export.tar ubuntu-imported # cria uma imagem 'ubuntu-imported' a partir do container exportado para o 'test-export.tar'

docker image rm alpine
docker image pull alpine # baixa a imagem alpine do dockerhub

docker image tag ubuntu allumy/meu-ubuntu:1 # cria a tag 'allumy/meu-ubuntu' da imagem ubuntu, versão 1

docker image push allumy/meu-ubuntu:1 # empurra a imagem para o seu repo no dockerhub

### SYSTEM ###

docker system df # informações de consumo de armazenamento do docker

docker system info # resumo de informações da docker engine

docker 'OBJETO' prune # limpa os objetos (image, container, volume, network) que não estão em uso. 

