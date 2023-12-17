def main():
    rooms = {'A':0, 'B':0}
    cost = 0
    print("---------------VACUUM CLEARNER WORLD---------------\n")
    print("[1] for dirt\n[2] for clean\n")
    
    #getting the status of the rooms
    for i in rooms.keys():
        rooms[i] = int(input(f'Enter the status of {i} :'))
    print()
    
    #checking for dirt and cleaning the rooms
    for i in rooms.keys():
        if (rooms[i] == 1):
            print(f'[-] Room {i} is dirty... cleaning...')
            rooms[i] = 0
            print(f'[*] Room {i} is now cleaned.')
            cost = cost + 1
        else:
            print(f'[!] Room {i} is already clean.')
    
    print(f'Total Cost is {cost}\n')

if __name__ == '__main__':
    main() #for running the main function