import time
import random
import math
import numpy as np
import plotly.graph_objects as px
import math

start_time= time.time()
mars_map = np.load('crater_map.npy')
nr, nc = mars_map.shape
scale = 10.0174

ci = round(3350 / scale)
ri = nr - round(5800 / scale)
states=[]

class Board(object):
    def __init__(self,board):
        self.map = board
        self.x=ci
        self.y=ri
        self.z=self.map[self.y][self.x]
        self.initial = (ci, ri)
        self.state=(ci,ri,self.z)

    def states(self,est_min):
        self.x=est_min[0]
        self.y=est_min[1]
        self.z=est_min[2]
        self.state=est_min
        states.append((self.x,self.y,self.z))
        return (self.x,self.y,self.z)
    
    def cost(self):
        return self.z
    
    def neighbor(self):
        ns=[]
        for i in (0,-1,1):
            for j in (-1,0,1):
                xn=self.x+i
                yn=self.y+j
                zn=self.map[yn][xn]
                if abs(self.z - zn) <= 2:
                    ns.append((xn,yn,zn))
        return ns

random.seed(time.time()*1000)
board = Board(mars_map)
costo = board.cost()
punto_bajo=np.amin(mars_map)
step = 0
estado_actual=board.states(board.state)
alpha = 0.999
t0 = 2
t = t0
while t > 0.001 and costo > 0:
    step += 1
    t = t0 * math.pow(alpha, step)
    vecinos=board.neighbor()
    cost_min=costo
    for new_cost in vecinos:
        if new_cost[2]<costo:
            cost_min=min(cost_min,new_cost[2])
        else:
            p = math.exp(-(new_cost[2] - costo)/t)
            if p >= random.random():
                new_state=new_cost
                estado_actual=board.states(new_state)
                costo=board.cost()
                step += 1
                t = t0 * math.pow(alpha, step)
                vecinos=board.neighbor()
                cost_min=costo
    new_state=estado_actual
    for vec in vecinos:
        if vec[2]==cost_min:
            new_state=vec
    estado_actual=board.states(new_state)
    costo=board.cost()
    print("Iteration: ", step, " Cost: ", costo)
print("--------Solution-----------")

path_x = []
path_y = []
path_z = []
for i in states:
    u = i
    x = u[0]
    y = u[1]
    path_x.append(x)
    path_y.append(y)
    z = u[2]
    path_z.append(z)

sumad=0
cont=0

for i in range(len(path_x)):
    path_x[i] = path_x[i] * scale

for i in range(len(path_y)):
    path_y[i] = (nr - path_y[i]) * scale

sumad=path_z[0]-path_z[-1]
print("Distancia bajada: ",round(sumad,4))

tiempo = time.time()-start_time

x = scale * np.arange(mars_map.shape[1])
y = scale * np.arange(mars_map.shape[0])
X, Y = np.meshgrid(x, y)
fig = px.Figure(data=[px.Surface(x=X, y=Y, z=np.flipud(mars_map), colorscale='hot', cmin=0,
                                 lighting=dict(ambient=0.0, diffuse=0.8, fresnel=0.02, roughness=0.4, specular=0.2),
                                 lightposition=dict(x=0, y=nr / 2, z=2 * mars_map.max())),
                      px.Scatter3d(x=path_x, y=path_y, z=path_z, name='path', mode="markers",
                                   marker=dict(color=np.linspace(0, 1, len(path_x)), colorscale="Bluered", size=4))],
                layout=px.Layout(scene_aspectmode='manual',
                                 scene_aspectratio=dict(x=1, y=nr / nc, z=max(mars_map.max() / x.max(), 0.2)),
                                 scene_zaxis_range=[0, mars_map.max()]))
fig.show()