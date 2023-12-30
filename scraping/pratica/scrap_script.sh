# script para utilizar o scraping para obter algumas vagas para emprego em python
# salva informações chave dessas vagas em um arquivo
# as palavras desse arquivo são ranqueadas para ver quais são os termos mais requeridos

RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m' # sem cor

echo -e "${BLUE}Realizando scraping...${NC}"
python3 scrap_online.py

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Extração completa.${NC}"
else
    echo -e "${RED}Falha ao realizar o scraping.${NC}"
    exit
fi

echo -e "${BLUE}Vagas lidas: ${NC}"
cat 'job_logs.md'

echo -e "${BLUE}Ranqueando as palavras extraídas...${NC}"

python3 key_count.py

if [ $? -eq 0 ]; then
    echo -e "${GREEN}Ranqueamento concluído.${NC}"
else
    echo -e "${RED}Falha ao realizar o ranqueamento.${NC}"
    exit
fi

echo -e "${BLUE}RANKING: ${NC}"

cat 'rank_words.md'
