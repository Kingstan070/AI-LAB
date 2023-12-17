def bfs(graph, s_node, e_node,v=[], q=[]):
    if s_node not in graph:
        print('[!] Startnode not found in the graph')
        return
    
    q.append(s_node)
    v.append(s_node)
    while q:
        node = q.pop()
        for i in graph[node]:
            if i not in v:
                q.append(i)
                v.append(i)
                if i == e_node:
                    print('[*] End node found!')
                    print(f'[>] Path followed is {v}')
                    return
    print('[!] Node not found!')
    print(f'[>] Path followed is {v}')
    return


def dfs(graph, s_node, e_node,v=[], q=[]):
    if s_node not in graph:
        print('[!] Startnode not found in the graph')
        return
    
    q.append(s_node)
    v.append(s_node)
    while q:
        node = q.pop(0)
        for i in graph[node]:
            if i not in v:
                q.append(i)
                v.append(i)
                if i == e_node:
                    print('[*] End node found!')
                    print(f'[>] Path followed is {v}')
                    return
    print('[!] Node not found!')
    print(f'[>] Path followed is {v}')
    return

def main():
    graph = {'A': ['B','C'],
            'B' : ['D','E','A'],
            'C' : ['A','F'],
            'D' : ['B'],
            'E' : ['B','G','H'],
            'F' : ['C'],
            'G' : ['E'],
            'H' : ['E']}
    s_node = input("[>] Enter the startnode: ")
    e_node = input("[>] Enter the end node : ")
    print("\n-----Breadth-First Search-----\n")
    bfs(graph, s_node, e_node)
    print("\n-----Depth-First Search-----\n")
    dfs(graph, s_node, e_node)

if __name__ == '__main__':
    main()