import numpy as np
from simpleai.search import SearchProblem, astar
import matplotlib.pyplot as plt
import plotly.graph_objects as px


# cargar el mapa
mars_map = np.load('mars_map.npy')
escala = 10  # meters per pixel
nr, nc = mars_map.shape
# Define parameters
height_threshold = 0.25  # in meters
# Define start and end positions
x_start, y_start, z_start = 2850, 6400, mars_map[nr -round(6400 / escala), round(2850 / escala)]
x_end, y_end, z_end = 545, 13500, mars_map[nr -round(13500 / escala), round(545 / escala)]
# dimensiones del mapa

x_start_escalado= round(x_start/escala)
y_start_escalado= nr - round(y_start/escala)

x_end_escalado= round(x_end/escala)
y_end_escalado= nr - round(y_end/escala)


class RoverProblem(SearchProblem):
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.camino = []

    def set_initial(self):
        return self.initial_state

    def is_goal(self, state):
        # la meta es llegar a la posición (3150, 6800, z_end)
        return state == self.goal_state

    def actions(self, state):

        actions = ['N', 'S', 'E', 'W','NE','NW','SE','SW']
        c, r, z = state
        if (mars_map[r-1][c] == -1) or ((abs(z-mars_map[r-1][c]))>=height_threshold):
            actions.remove('W')

        if (mars_map[r+1][c] == -1) or ((abs(z-mars_map[r+1][c]))>=height_threshold):
            actions.remove('E')

        if (mars_map[r][c-1] == -1) or ((abs(z-mars_map[r][c-1]))>=height_threshold):
            actions.remove('S')

        if (mars_map[r][c+1] == -1) or ((abs(z-mars_map[r][c+1]))>=height_threshold):
            actions.remove('N')

        if (mars_map[r-1][c-1] == -1) or ((abs(z-mars_map[r-1][c-1]))>=height_threshold):
            actions.remove('SW')

        if (mars_map[r+1][c+1] == -1) or ((abs(z-mars_map[r+1][c+1]))>=height_threshold):
            actions.remove('NE')

        if (mars_map[r+1][c-1] == -1) or ((abs(z-mars_map[r+1][c-1]))>=height_threshold):
            actions.remove('SE')

        if (mars_map[r-1][c+1] == -1) or ((abs(z-mars_map[r-1][c+1]))>=height_threshold):
            actions.remove('NW')
        
        return actions

    def result(self, state, action):
        c, r, z = state
        if action == 'N':
            self.camino.append((r,c+1, mars_map[r,c+1]))
            return (c+1, r, mars_map[r,c+1])
        elif action == 'S':
            self.camino.append((r,c-1, mars_map[r,c-1]))
            return (c-1,r, mars_map[r,c-1])
        elif action == 'E':
            self.camino.append((r+1,c, mars_map[r+1,c]))
            return ( c,r+1,mars_map[r+1,c])
        elif action == 'W':
            self.camino.append((r-1,c, mars_map[r-1,c]))
            return (c,r-1, mars_map[r-1,c])
        elif action == 'NW':
            self.camino.append((r-1,c+1, mars_map[r-1,c+1]))
            return (c+1, r-1, mars_map[r-1,c+1])
        elif action == 'NE':
            self.camino.append((r+1,c+1, mars_map[r+1,c+1]))
            return (c+1,r+1, mars_map[r+1,c+1])
        elif action == 'SW':
            self.camino.append((r-1,c-1, mars_map[r-1,c-1]))
            return (c-1,r-1, mars_map[r-1,c-1])
        elif action == 'SE':
            self.camino.append((r+1,c-1, mars_map[r+1,c-1]))
            return (c-1,r+1, mars_map[r+1,c-1])

    def cost(self, state, action, next_state):
        if action == 'SE,SW,NE,NW':
            return np.sqrt(2)
        else:
            return 1

    def cost_with_heuristic(self, state, action, next_state):
        # combina el costo de la acción con la heurística del siguiente estado
        return self.cost(state, action, next_state) + self.heuristic(next_state)

    def heuristic(self, state):
        # la heurística es la distancia de Manhattan a la meta
        return abs(state[0] - self.goal_state[0]) + abs(state[1] - self.goal_state[1]) + abs(state[2] - self.goal_state[2])
    
problem = RoverProblem(initial_state=(x_start_escalado, y_start_escalado, z_start), goal_state=(x_end_escalado, y_end_escalado, z_end))
result = astar(problem, graph_search=True)

truepath=[]
path = result.path()
for state in path:
    truepath.append((state[1]))
print(truepath)
distance = 0
for i in range(len(truepath)-1):
    # Calculate the Euclidean distance between consecutive states
    distance += ((truepath[i][0]-truepath[i+1][0])**2 + (truepath[i][1]-truepath[i+1][1])**2 + (truepath[i][2]-truepath[i+1][2])**2)**0.5

print("Distance:", distance*escala)

path_x, path_y, path_z = zip(*truepath)
path_x = list(path_x)
path_y = list(path_y)
for i in range(len(path_x)):
    path_x[i] = path_x[i]*escala
for i in range(len(path_y)):
    path_y[i] = (nr -path_y[i])*escala
x = escala*np.arange(mars_map.shape[1])
y = escala*np.arange(mars_map.shape[0])
X, Y = np.meshgrid(x, y)


fig = px.Figure(data = [px.Surface(x=X, y=Y, z=np.flipud(mars_map), colorscale='hot', cmin = 0, 
                                    lighting = dict(ambient = 0.0, diffuse = 0.8, fresnel = 0.02, roughness = 0.4, specular = 0.2),
                                    lightposition=dict(x=0, y=nr/2, z=0)),
                        
                        px.Scatter3d(x = path_x, y = path_y, z = path_z, name='path', mode='markers',
                                        marker=dict(color=np.linspace(0, 1, len(path_x)), colorscale="Bluered", size=4))],
                
                layout = px.Layout(scene_aspectmode='manual', 
                                    scene_aspectratio=dict(x=1, y=nr/nc, z=max(mars_map.max()/x.max(), 0.2)), 
                                    scene_zaxis_range = [0,mars_map.max()])
                )
fig.show()





