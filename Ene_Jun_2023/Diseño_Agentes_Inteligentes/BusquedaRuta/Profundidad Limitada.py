import numpy as np
from simpleai.search import SearchProblem, limited_depth_first
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
x_end, y_end, z_end = 3150, 6800, mars_map[nr -round(6800 / escala), round(3150 / escala)]
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
result = limited_depth_first(problem, depth_limit = 100, graph_search=True)

if result==None:
    print('No se encontró una solución')