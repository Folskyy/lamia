import numpy as np
from keras.models import model_from_json

arquivo = open('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/output/classificador_breast.json', 'r')
estrutura_rede = arquivo.read()
arquivo.close

classificador = model_from_json(estrutura_rede)
classificador.load_weights('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/output/classificador_breast.h5')

