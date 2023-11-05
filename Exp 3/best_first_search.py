graph = {'Arad': [['Sibiu',253],['Timisoara',329],['Zerind',374]],
            'Sibiu': [['RimnicuVilcea',193],['Arad',366],['Fagarus',176],['Oradea',380]], 
            'Rimnicu Vilcea': [['Sibiu',253],['Pitesti',100]], 
            'Pitesti': [['Craiova',160],['Rimicu Vilcea',193],['Bucharest',0]], 
            'Fagarus': [['Sibiu',253],['Bucharest',0]],
            'Timisoara': [['Arad',366],['Lugoj',274]],
            'Zerind': [['Arad',366],['Ordea',380]], 'Oradea': [['Sibiu',253]]
}

def main():
    print("Choose the start point:")
    for index, city in enumerate(graph.keys(), 1):
        print(f'{index}. {city}')
    
    start = list(graph.keys())[int(input('Enter the index of city: '))-1]
    best_fs(start)

def best_fs(startnode, explored=[], frontier=[]):
    if startnode not in graph.keys():
        print("[!] Invalid start node entered!!")
    child = graph[startnode]
    frontier.extend(child)
    explored.append(startnode)
    while frontier:
        #sorting the frontier list
        frontier.sort(key = lambda t: t[1])
        next_stop = frontier.pop(0)

        if next_stop[1] == 0:
            explored.append(next_stop)
            print('[*] Destination arrived')
            print(f'[*] Explored List: {explored}')
            return
        else:
            child = graph[next_stop[0]]
            frontier.extend(child)
            explored.append(next_stop)
    print('[!] Destination not found!')
    return


if __name__ == '__main__':
    main()