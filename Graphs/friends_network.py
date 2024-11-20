"""
Friends network.
"""

# Defining an empty dictionary to represent the Adjacency List of our graph
friends_network = {}

# Add vertices to our graph by adding keys to our dictionary
friends_network["John"] = [] 
friends_network["Emma"] = []  
friends_network["Sam"] = []

# Display the adjacency list with created vertices (will have no edges yet)
print(f"The Graph after adding vertices: {friends_network}")

# Adding an edge between two vertices simply involves appending to their corresponding lists in the dictionary
friends_network["John"].append("Emma")
friends_network["Emma"].append("John") # Because this is a bidirectional friend network (if John is a friend of Emma, then Emma is also a friend of John)

# Add additional edges
friends_network["Emma"].append("Sam")
friends_network["Sam"].append("Emma") # Mutual friendship
friends_network["John"].append("Sam")
friends_network["Sam"].append("John") # Mutual friendship

# Display the adjacency list after the edges have been added
print(f"The Graph after adding edges: {friends_network}")

# If we want to assess if an edge exists between two vertices,
# We just have to check if one vertex is in the list of the other vertex

edge_exists = "Sam" in friends_network["John"] 
print(f"There exists an edge between John and Sam: {edge_exists}") # Expect True

edge_exists = "John" in friends_network["Emma"] 
print(f"There exists an edge between Emma and John: {edge_exists}") # Expect True

# Add a new vertex and edge
friends_network["Sarah"] = [] 
friends_network["Sarah"].append("Sam")
friends_network["Sam"].append("Sarah")

print(f"The Graph after adding Sarah and her friendship with Sam: {friends_network}")