#%%
import torch
import matplotlib.pyplot as plt
# from torchviz import make_dot # não encontrei a biblioteca para o conda

#%%
# dataset: y é a soma dos elementos de x
x = [[1,2],[3,4],[5,6],[7,8]]
y = [[3],[7],[11],[15]]

#%%
# conversão de lista para tensores e inteiros para o tipo float
X = torch.tensor(x).float()
Y = torch.tensor(y).float()

#%%
import torch.nn as nn # nn = neural network

#%%
# os modelos no pytorch podem ser declarados em classes
class neural_net(nn.Module):
    def __init__(self):  
        super().__init__() # inicia os métodos da classe pai (nn.Module)
        self.layer1 = nn.Linear(2,8)
        # a camada linear utiliza da operação linear y = ax + b
        # y = saída; a = entrada; x = peso (matriz); b = bias
        # em resumo, multiplica a entrada pelo peso que funciona como um conjunto de coeficientes
        # aprendidos, seguido pela soma do bias para introduzir deslocamento na saída
        self.activation = nn.ReLU() # activation function
        self.layer2 =  nn.Linear(8,1)

    # determina o fluxo de dados através da rede (ordem, como são processados e transformados)
    def forward(self,x): 
        x = self.layer1(x)
        x = self.activation(x)
        x = self.layer2(x)
        return x

#%%
model = neural_net()
print(model, "\n", X.shape)

# %%
# matriz de pesos
print(model.layer1.weight, "\n\n", model.parameters().__next__())

#%%
# função de ativação
import math

class ReLU(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.max(torch.zeros_like(x), x)

#%%
# loss-function
import numpy as np

def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# %%
# ajustando os parametros do modelo
from torch.optim import SGD

loss_func = nn.MSELoss()
# lr = learning rate
optimizer = SGD(model.parameters(), lr=0.001)

#%%
import time
#%%
# training loop
losses = []

start = time.time()

for i in range(50): # 50 epochs
    optimizer.zero_grad() # zerando o gradiente

    loss_value = loss_func(model(X), Y)
    # ativa o algoritmo de *backpropagation*: calcula os gradientes da
    # função de perda em relação a cada parâmetro do modelo
    loss_value.backward() 

    # atualização dos pesos e biases usando os gradientes calculados no backpropagation
    optimizer.step()
    losses.append(loss_value.detach().numpy()) # add o valor do loss nessa iteração

end = time.time()

print("Tempo de execução: ", end-start)

#%%
plt.plot(losses)
plt.title('Variação da perda em relação ao aumento do número de épocas')
plt.xlabel('épocas')
plt.ylabel('loss_value')

#%%
import torch
import time
import torch.nn as nn
from torch.optim import SGD
from torch.utils.data import Dataset # estrutura abstrata para armazenar dados personalizados
from torch.utils.data import DataLoader # gerenciador de datasets para preparar os dados para o treinamento
device = 'cuda' if torch.cuda.is_available() else 'cpu'
#%%
# classe para transformar numpy arrays em tensores
class MyDataset(Dataset):
    def __init__(self, x, y):
        super().__init__()
        # tensor de entrada
        self.x = torch.tensor(x).float().to(device)
        # tensor com o resultado esperado
        self.y = torch.tensor(y).float().to(device)
    def __len__(self):
        # retorna o número de amostras, supondo que os dois tensores tem o mesmo tamanho
        return len(self.x)
    def __getitem__(self,ix):
        # retorna dois elementos: um é a entrada e o outro é a saída esperada
        return self.x[ix], self.y[ix]
    
#%%
# dataset: y é a soma dos elementos de x
i = [[1,2],[3,4],[5,6],[7,8]]
j = [[3],[7],[11],[15]]

#%%
ds = MyDataset(i, j) # cria uma instancia onde os dados de entrada são convertidos em tensores
dl = DataLoader(ds, batch_size=2, shuffle=True) # classe para carregar conj de dados durante o treinamento

#%%
seq_model = nn.Sequential(nn.Linear(2, 8),
                          nn.ReLU(),
                          nn.Linear(8, 1)).to(device)

optimizer = SGD(seq_model.parameters(), lr=0.001)

loss_func = nn.MSELoss()

#%%
loss_history = []
start = time.time()

seq_model.train() # ativa o modo de treinamento: permite que seus parametros sejam atualizados

for _ in range(100):
    for ij, ik in dl:
        optimizer.zero_grad()
        loss_value = loss_func(seq_model(ij), ik)
        loss_value.backward()

        optimizer.step()
        loss_history.append(loss_value)

end = time.time()
print(end - start)
#%%
# valores para teste de previsão do modelo
test_val = [[8, 9], [10, 11], [1.5, 2.5]]
test_val = torch.tensor(test_val).float()
#%%
seq_model(test_val).float()
# %%
