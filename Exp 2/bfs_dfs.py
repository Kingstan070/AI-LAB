def bfs(graph, startnode, endnode, visited=[], queue=[]):
    if startnode not in graph.keys():
        print("[!] Invalid start node entered!!")
    queue.append(startnode)
    visited.append(startnode)
    while queue:
        node = queue.pop()
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                if i == endnode:
                    print("[*] Element found\n[*] Path is ", visited)
                    return
    print("[!] Endnode not found!")

def dfs(graph, startnode, endnode, visited=[], queue=[]):
    if startnode not in graph.keys():
        print("[!] Invalid start node entered!!")
    queue.append(startnode)
    visited.append(startnode)
    while queue:
        node = queue.pop(0)
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                if i == endnode:
                    print("[*] Element found\n[*] Path is ", visited)
                    return
    print("[!] Endnode not found!")

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