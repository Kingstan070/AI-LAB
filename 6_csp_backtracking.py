# Domain colors
colors = ['Red', 'Blue', 'Green']
# wa    west australia,
# nt    northern territory,
# sa    south australia,
# q     queensland,
# nsw   new south wales,
# v     victoria,
# t     tansmania
variable_states = ['wa', 'nt', 'sa', 'q', 'nsw', 'v','t']
neighbors = {}
neighbors['wa'] = ['nt', 'sa']
neighbors['nt'] = ['wa', 'sa', 'q']
neighbors['sa'] = ['wa', 'nt', 'q', 'nsw', 'v']
neighbors['q'] = ['nt', 'sa', 'snw']
neighbors['nsw'] = ['q', 'sa', 'v']
neighbors['v'] = ['sa', 'nsw']
neighbors['t'] = []
finalstateswithcolor = {}

def gettheColors(state):
    for color in colors:
        if assignColors(state, color):
            return color

def assignColors(state, color):
    for neighbor  in neighbors.get(state):
        color_of_neighbor = finalstateswithcolor.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def main():
    sorted_states = sorted(neighbors.keys(),
                           key=lambda x: len(neighbors.get(x)),
                           reverse=True)
    
    for state in sorted_states:
        finalstateswithcolor[state] = gettheColors(state)

    print("The states with colors are:")
    for state, color in finalstateswithcolor.items():
        print(f'{state}\t-> {color}')

if __name__ == '__main__':
    main()