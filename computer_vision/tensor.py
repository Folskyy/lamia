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
pyo.plot(fig, filename='tensor.html')

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
pyo.plot(fig, filename='tensor.html')

# %%

