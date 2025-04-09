import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def states_traversal(states, start_state, end_state, visited, traversal):
    if start_state == end_state:
        traversal.append(start_state)
        return traversal
    
    visited.add(start_state)
    traversal.append(start_state)
    
    for neighboring_state in states[start_state]:
        if neighboring_state not in visited:
            result = states_traversal(states, neighboring_state, end_state, visited, traversal)
            if result:
                return result
    
    traversal.pop()
    return None
        
    



def main():
    # Example usage
    file_path = 'c:/Users/onlyj/Desktop/DSA 2024/Data-Structures-and-Algorithms-in-Python-2024/Graphs/states.json'
    data = read_json_file(file_path)
    # print(data)
    states = data
    start_state = "Oklahoma"
    end_state = "Colorado"
    visited = set()
    traversal = []
    dfs = states_traversal(states, start_state, end_state, visited, traversal)
    print(f"The path from {start_state} to {end_state} is:")
    if dfs:
        print("->".join(dfs))
    
        

if __name__ == "__main__":
    main()