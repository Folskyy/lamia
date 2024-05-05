#%%
import torch
import torch.nn as nn
from torchvision.datasets import FashionMNIST
import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import Dataset, DataLoader

# %%
tr_images = FashionMNIST('',train=True, download=False).data
tr_targets = FashionMNIST('',train=True, download=False).targets

# %%
class FMNISTDataset(Dataset):
    def __init__(self,x,y):
        super().__init__()
        x = x.float()
        # normalização dos dados. Já que os possiveis valores para um pixel varia de 0-255
        x = x.float() / 255
        # -1 indica que vai redimensiona automaticamente o conjunto
        # de dados baseado no novo formato do tensor (planificação)
        x = x.view(-1, 28*28)
        # armazena os dados de entrada como atributos da clsse
        self.x, self.y = x,y
    def __getitem__(self,idx):
        x,y = self.x[idx], self.y[idx]
        return x, y
    def __len__(self):
        return len(self.x)

#%%
def get_data():
    train = FMNISTDataset(tr_images, tr_targets)
    trn_dl = DataLoader(train, batch_size=32, shuffle=True)
    return trn_dl

#%%
# definindo o modelo
from torch.optim import Adam# , SGD
def get_model():
    model = nn.Sequential(
        nn.Linear(28 * 28, 1000),
        nn.ReLU(),
        nn.Linear(1000, 10)
        )
    loss_fn = nn.CrossEntropyLoss()
    # optimizer = SGD(model.parameters(), lr=0.002)
    optimizer = Adam(model.parameters(), lr=1e-3)
    return model, loss_fn, optimizer

#%%
@torch.no_grad() # desativa temporariamente o calculo do gradiente para melhor avaliação
def accuracy(x, y, model):    
    model.eval() # modo de avaliação
    prediction = model(x)
    max_values, argmaxes = prediction.max(-1)
    # o .max() retorna um tensor com valores representando a probabilidade
    # de classificação em cada rótulo disponivel.
    # o max_value armazena o maior valor (maior probabilidade).
    # o argmaxes armazena o índice do max_value, indicando o rótulo mais provável para a entrada
    is_correct = argmaxes == y # verificação se a previsão está correta
    return is_correct.cpu().numpy().tolist()

#%%
def train_batch(x, y, model, optimizer, loss_fn):
    model.train()
    
    # zera o gradiente para o próximo batch
    optimizer.zero_grad()

    prediction = model(x)
    # calcula o loss
    batch_loss = loss_fn(prediction, y)
    # calcula os gradientes em reelação a todos os parametros
    batch_loss.backward()
    # atualização dos pesos usando o otimizador que recebe os gradientes como entrada
    optimizer.step()
    return batch_loss.item() # sem o .item() o loss é um tensor, com o item retorna um escalar

#%%
trn_dl = get_data()
model, loss_fn, optimizer = get_model()

#%%
losses, accuracies = [], []
for epoch in range(5):
    print(epoch)
    epoch_losses, epoch_accuracies = [], []

    for ix, batch in enumerate(iter(trn_dl)):
        # o iter cria um iterador para iterar sobre os batches.
        # o enumerate itera no batch atual, retornando um indice e o batch.
        x, y = batch
        batch_loss = train_batch(x, y, model, optimizer, loss_fn)
        epoch_losses.append(batch_loss)
    
    # média do loss na epoch atual
    epoch_loss = np.array(epoch_losses).mean()
    
    for ix, batch in enumerate(iter(trn_dl)):
        x, y = batch
        is_correct = accuracy(x, y, model)
        epoch_accuracies.extend(is_correct)
    epoch_accuracy = np.mean(epoch_accuracies)
    losses.append(epoch_loss)
    accuracies.append(epoch_accuracy)

#%%
epochs = np.arange(5)+1
plt.figure(figsize=(20,5))
plt.subplot(121)
plt.title('Loss value over increasing epochs')
plt.plot(epochs, losses, label='Training Loss')
plt.legend()
plt.subplot(122)
plt.title('Accuracy value over increasing epochs')
plt.plot(epochs, accuracies, label='Training Accuracy')
plt.gca().set_yticklabels(['{:.0f}%'.format(x*100) for x in plt.gca().get_yticks()]) 
plt.legend()

#%%
# visualização de um tensor de saída (previão)
num = 19
print(model(FashionMNIST('', download=False, train=False).data[num].float().view(-1, 28*28)))
print(FashionMNIST('', download=False, train=False).targets[num])
# %%
