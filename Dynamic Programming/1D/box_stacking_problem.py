"""
Box Stacking Problem

We are given an array of boxes. Each box is represented
using 3 integers denoting height, width, depth of the box. 

Our goal is to stack up the boxes and maximise the total height of the stack.

You can't rotate any boxes. i.e. integers in each box must
represent [width, depth, height] at all times. The

A box must have strictly smaller width, depth and height of the
than any other box below it.

"""

def canPlace(box1, box2):
    # Check if box2 can be placed on top of box1
    return box1[0] > box2[0] and box1[1] > box2[1] and box1[2] > box2[2]

def box_stacking(boxes):
    # sorting 
    boxes.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    
    # get the length of n
    n = len(boxes)
    # create the dp array
    dp = [0] * (n + 1)
    # fill in the dp array
    for i in range(0, n):
        dp[i] = boxes[i][2] # height of the ith box
    
    # iterate through the boxes array
    for i in range(1, n):
        for j in range(0, i):
            # check if the box can be stacked on top of the other box
            if canPlace(boxes[j], boxes[i]):
                # get current height 
                current_height = boxes[i][2]
                if (dp[j] + current_height) > dp[i]:
                    # update the dp array with the maximum height
                    dp[i] = dp[j] + current_height

    max_height = 0
    # iterate through the dp array to get the maximum height
    for i in range(0, n):
        max_height = max(max_height, dp[i])
    # return the maximum height of the stack
    return max_height

def main():
    # Example 1:
    boxes = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [2, 2, 1], [4, 4, 5]]
    print(f"Maximum height of the stack: {box_stacking(boxes)}")

if __name__ == "__main__":
    main()