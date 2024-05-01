#%%
import torch # as pt
import plotly.graph_objs as go
import plotly.offline as pyo

#%%
# 1-D array
sample = torch.tensor([19, 21])
sample.shape

#%%
x = torch.tensor([[10, 11], [1, 2]])
x.shape

#%%
y = torch.tensor([[10], [11]])
y.shape

#%%
# 3-D Tensor visualization
a = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

x_vals = []
y_vals = []
z_vals = []

# armazenar todos os pontos de x, y e z
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            x_vals.append(i)
            y_vals.append(j)
            z_vals.append(k)

#%%
trace = go.Scatter3d(x=x_vals, y=y_vals, z=z_vals, mode='markers', marker=dict(size=5, color=a.flatten(), colorscale='Viridis', opacity=0.8))

#%%
# Create the plot layout
layout = go.Layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(
        xaxis=dict(title='Dimension 1'),
        yaxis=dict(title='Dimension 2'),
        zaxis=dict(title='Dimension 3')
    )
)

#%%
# Combine the trace and layout into a figure and display it
fig = go.Figure(data=[trace], layout=layout)

#%%
pyo.plot(fig, filename='tensor3d.html')

#%%
#2-D
a = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

x_vals = []
y_vals = []

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
            x_vals.append(i)
            y_vals.append(j)

#%%
trace = go.Scatter(x=x_vals, y=y_vals, mode='markers', marker=dict(size=5, color=a.flatten(), colorscale='Viridis', opacity=0.8))

#%%
# Create the plot layout
layout = go.Layout(
    margin=dict(l=0, r=0, b=0, t=0),
    scene=dict(
        xaxis=dict(title='Dimension 1'),
        yaxis=dict(title='Dimension 2'),
        zaxis=dict(title='Dimension 3')
    )
)

#%%
# Combine the trace and layout into a figure and display it
fig = go.Figure(data=[trace], layout=layout)

#%%
pyo.plot(fig, filename='tensor2d.html')

########################OPERATIONS########################
#%%
x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
x.shape

#%%
x * 10 # multiplica cada elemento do tensor

#%%
x.add(10) # add 10 em cada elemento do tensor

#%%
# o view é como se planificasse e redimensionasase o tensor
print(x, "\nShape:\n", x.shape, "\n\n4x2:\n", x.view(4, 2),
      "\n\n8x1:\n", x.view(8, 1),"\n\n1x8:\n", x.view(1, 8))

#%%
y = torch.ones(2, 1, 10) # tensor de 1s com dimensão 2x1x10
y

#%%
# .squeeze() remove dimensões de tamanho 1
# pode receber um inteiro como parametro indicando a dimensão p/ realizar o squeeze
print(f"Tamanho do tensor: {y.shape}\nTamanho do tensor depois do squeezing: {y.squeeze().shape}")

# %%
y = torch.ones(2, 3, 1)
y
#%%
print("Sem squeeze: ", y.shape)
print("Squeeze em todas as dimensões:", y.squeeze().shape)
print("Squeeze na prieira dimensão:  ", y.squeeze(0).shape)
print("Squeeze na segunda dimensão:  ", y.squeeze(1).shape)
print("Squeeze na terceira dimensão: ", y.squeeze(2).shape)
# %%
# .unsqueeze() adiciona uma dimensão de tamanho 1
# nesse caso o parâmetro indicando a dimensão é obrigatório
print("Sem unsqueeze: ", y.shape)
print("unsqueeze na prieira dimensão:  ", y.unsqueeze(0).shape)
print("unsqueeze na segunda dimensão:  ", y.unsqueeze(1).shape)
print("unsqueeze na terceira dimensão: ", y.unsqueeze(2).shape)
# %%
# alternativa ao unsqueeze
print("Sem unsqueeze: ", y.shape)
print("unsqueeze na prieira dimensão:  ", y[None].shape)
print("unsqueeze na segunda dimensão:  ", y[:,None].shape)
print("unsqueeze na terceira dimensão: ", y[:,:,None].shape)

# %%
a = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
b = torch.tensor([[1, 2, 3],
                  [2, 3, 4],
                  [4, 5, 6],
                  [7, 8, 9]])

# %%
# multiplicação de matrizes A(nxm) x B(mxz) = C(nxz)
print("Resultado da multiplicação: \n", torch.matmul(a, b))
print(f"\na {a.shape}\nb {b.shape}\na x b = {torch.matmul(a, b).shape}")
# %%
# concatena tensores ao longo de uma dimensão escolhida
print(torch.cat([a, a], axis=2))
print("\na:\n", a.shape, "\naxa:\n", torch.cat([a, a]).shape)

# %%
# .permute reordena as ordem das dimensões
# os parametro é uma sequencia de int representando a nova ordem desejada
a = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
a = a.unsqueeze(2)
print("a:\n", a.shape, "\n[0]=[2], [1]=[0], [2]=[1]: \n", a.permute(2, 0, 1).shape)
print(a, "\n\n", a.permute(2, 0, 1))
# %%


