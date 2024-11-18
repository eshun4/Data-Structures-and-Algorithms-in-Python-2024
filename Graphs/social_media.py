"""
Social Media.
"""

# Let's consider a different graph for 5 people: A: 0, B: 1, C: 2, D: 3, E: 4
# A is friends with B and C
# B is friends with A, C and D
# C is friends with A, B and E
# D is friends with B
# E is friends with C

# Number of people
n = 5
users = ['A', 'B', 'C', 'D', 'E']

# Initialize the adjacency matrix
M = [[0] * n for _ in range(n)]

# Map the relationships
# A
M[0][1] = M[0][2] = 1
# B
M[1][0] = M[1][2] = M[1][3] = 1
# C
M[2][0] = M[2][1] = M[2][4] = 1
# D
M[3][1] = 1
# E
M[4][2] = 1

# Print the Graph
for row in range(n):
    print(M[row])

# Suggest friends for each user, avoiding cases where users are suggested to be friends with themselves
for i in range(n):
    for j in range(n):
        if i != j:
            if M[i][j] == 0 and any(M[i][k] and M[k][j] for k in range(n)):
                print(
                    f"Based on the mutual friends, "
                    f"User {users[i]} and User {users[j]} may know each other."
                )