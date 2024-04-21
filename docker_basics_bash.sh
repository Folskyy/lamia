echo "Criação de dois containers usando alpine e ubuntu como imagem."
read -n 1 -s -r -p "Pressione qualquer tecla para continuar."

docker container create --name alpine_test alpine # cria um container  usando o SO alpine como imagem

docker container create --name ubuntu_test ubuntu # cria um container usando o SO ubuntu como imagem

echo "Container ubuntu_test e alpine_test criados."
read -n 1 -s -r -p "Pressione qualquer tecla para continuar."

echo "Lista dos containers criados:"
docker container ls -a # listagem dos containers (-a para mostras os itens ocultos)
echo "lista das imagens disponíveis localmente:"
docker image ls -a # listagem das imagens locais
echo "lista das imagens disponíveis com alpine no nome:"
docker image ls alpine # listagem das imagem com 'alpine' no nome

echo "Remoção do container 'ubuntu_test'"
read -n 1 -s -r -p "Pressione qualquer tecla para continuar."
docker container rm ubuntu_test # remoção de um container
echo "Lista dos containers criados:"
docker container ls -a # listagem após a remoção

echo "Remoção do container 'alpine_test'"
read -n 1 -s -r -p "Pressione qualquer tecla para continuar."
docker container rm alpine_test # remoção de um container
echo "Lista dos containers criados:"
docker container ls -a # lsitgem após a remoção

echo "Criação do container test."
read -n 1 -s -r -p "Pressione qualquer tecla para continuar."
docker container create --name test -it alpine sh
# o parametro -i permite a interação com o container atraves do seu terminal
# o parametro -t simula um pseudo-terminal para facilitar a interação dentro do container
# o parametro sh indica o pseudo-terminal que será simulado. 'ash' (bash) é o padrão
docker container start test # inicia o container 'test' (pode ser usado os primeiros char do id do container como alternativa)
docker container attach test # conecta ao container antes inicializado.

docker container stop test # interrompe o funcionamento do container test
docker container start -ia test # inicia na forma iterativa (-i/--interactive) e conecta ao conteiner (-a -attach)

docker container run -it --name test_2 alpine sh # cria, inicia e conteca ao container. Alternativa ao docker crate/docker start

docker container rename test_2 test2 # renomeia o container 'test_2' para 'test2'

ls
touch note.md
echo "TESTE DE INICIALIZAÇÃO INTERATIVA" > note.md
cat note.md

### CONTAINERS SÃO DESCARTÁVEIS ###


