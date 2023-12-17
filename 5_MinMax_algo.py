# Define constants for maximum and minimum values
MAX, MIN = 1000, -1000
# Minimax function for finding the optimal value in a search tree
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    #Terminating condition: 
    # If the maximum depth is reached, return the value of the current node
    if depth == 4:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN
        # For maximizing player, initialize best as the minimum value
        for i in range(0, 2):
            # Recur for left and right children
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val) # Update best with the maximum value
            alpha = max(alpha, best) # Update alpha with the maximum value
            if beta <= alpha:
                # Alpha-Beta Pruning: If beta is less than or equal to alpha, 
                # break the loop
                break 
        print("best value of max player-->",best)
        return best # Return the best value found so far for the maximizing player
    else:
        best = MAX
        # For minimizing player, initialize best as the maximum value
        for i in range(0, 2):
            # Recur for left and right children
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val) # Update best with the minimum value
            beta = min(beta, best) # Update beta with the minimum value
            if beta <= alpha:
                # Alpha-Beta Pruning: If beta is less than or equal to alpha, 
                # break the loop
                break 
        print("best value of min player-->",best) 
        return best # Return the best value found so far for the minimizing player

# Driver code
if __name__ == "__main__":
    #values = [3, 5, 6, 9, 1, 2, 0, -1]
    values= [10,5,7,11,12,8,9,8,5,12,11,12,9,8,7,10]
    # Call the minimax function with initial parameters and print the result
    print("The optimal value is:", minimax(0, 0, True, values, MIN, MAX))
