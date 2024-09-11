path='test_repo/'
user_name='user_name'
user_email='user@email.com'
editor='vim'
RED='\033[0;31m'
NC='\033[0m' # No Color

# definindo configurações globais do git
# git config --global user.name $user_name
# git config --global user.email $user_email
# git config --global core.editor $editor

# criando e entrando em um diretório
mkdir $path
cd $path

# inicializando o repositório
git init

# criando um arquivo
touch file.txt
echo "# GitHub" > file.txt

# estado dos arquivos no git
git status

# adiciona modificações para o próximo commit
git add file.txt

echo "# Git" >> file.txt

git add *

# commita as modificações adicionadas
git commit -m "text file added"

echo "# Necessary text" > file.txt

# visualiza as modificações não rastreadas
git diff

git add *
git commit -m "Necessary text added"

ls
# cria um novo branch
git branch bugFix

git checkout bugFix

touch necessary.txt

echo -e "${RED}Arquivos no novo branch:${NC}"
ls

git add *
git commit -m "necessary file added"

git checkout master

echo -e "${RED}Arquivos no branch master:${NC}"
ls

# junta os dois branches
git merge bugFix
echo -e "${RED}Após o merge:${NC}"
ls

git status

# conectar a um repositorio remoto
# link='git@github.com:user/repository.git'
# git remote add origin $link

# envia as alterações locais (origin) para o branch master do repo remoto (master)
# git push -u origin master
