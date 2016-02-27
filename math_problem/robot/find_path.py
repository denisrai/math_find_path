import sys

"""
    46B E59 EA C1F 45E 63

    899 FFF 926 7AD C4E FFF

    E2E 323 6D2 976 83F C96

    9E9 A8B 9C1 461 F74 D05

    EDD E94 5F4 D1D D03 DE3

    89 925 CF9 CA0 F18 4D2
"""

TEST = {1:{1:"46B", 2:"E59", 3:"EA",  4:"C1F", 5:"45E", 6:"63"},
        2:{1:"899", 2:"FFF", 3:"926", 4:"7AD", 5:"C4E", 6:"FFF"},
        3:{1:"E2E", 2:"323", 3:"6D2", 4:"976", 5:"83F", 6:"C96"},
        4:{1:"9E9", 2:"A8B", 3:"9C1", 4:"461", 5:"F74", 6:"D05"},
        5:{1:"EDD", 2:"E94", 3:"5F4", 4:"D1D", 5:"D03", 6:"DE3"},
        6:{1:"89",  2:"925", 3:"CF9", 4:"CA0", 5:"F18", 6:"4D2"},}

def generate_graph(matrix):
    graph = {}
    # import pdb; pdb.set_trace()
    for x_key, x_value in matrix.items():
        for y_key, y_value in x_value.items():

            if(y_value in graph.keys()):
                y_value = y_value + '_' + str(graph.keys().count(y_value)+1)

            graph[y_value] = {}
            try:
                graph[y_value][matrix[x_key][y_key+1]] = int(matrix[x_key][y_key+1], 16)
            except KeyError:
                # import pdb; pdb.set_trace()
                pass

            try:
                graph[y_value][matrix[x_key+1][y_key]] = int(matrix[x_key+1][y_key], 16)
            except KeyError:
                # import pdb; pdb.set_trace()
                pass
    return graph
            
def shortest_path(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]

    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxint)
            try:
                tentativedist = distances[start] + graph[start][neighbor]
            except:
                distances[start] = 0
                tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxint)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return shortest_path(graph,closestnode,end,visited,distances,predecessors)