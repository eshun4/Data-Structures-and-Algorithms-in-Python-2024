"""
Little Cute Cat.

Little CUte kitten loves to write stories in a Github readme document.
One day she is given a list of words, you want to help her to check if
each of these words are present in the readme file.

Sample Input:
document: "little cute cat loves to code in c++, jave & python
words = ["cute cat", "ttle", "cutest", "cat", "quick", "big"]

Sample Output:
True, True, True, False, False
"""

# Build a Prefix Trie

class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}  # Dictionary to store child nodes
        self.is_terminal = False  # Indicates if the node is the end of a word
    
class Trie:
    def __init__(self):
        self.root = Node("")
    
    def insert(self, word):
        temp = self.root    # Start from the root node
        for char in word:
            # If the character is not already a child of the current node, add it
            if char not in temp.children:
                temp.children[char] = Node(char)
            # Move to the child node
            temp = temp.children[char]
        # Mark the last node as terminal to indicate the end of a word
        temp.is_terminal = True

def searchHelper(trie, document, index, dictionary):
    # Get the root of the Trie
    temp = trie.root
    # Iterate through each character and check if it's in the children nodes
    for j in range(index, len(document)):
        char = document[j]
        if char not in temp.children:
            return
        # Move to the next node
        temp = temp.children[char]
        # If the current node is terminal, add the substring to the dictionary
        if temp.is_terminal:
            substring = document[index:j + 1]
            dictionary[substring] = True

def documentSearch(document, words):
    # Create a Trie object and insert all words
    trie = Trie()
    for word in words:
        trie.insert(word)
        
    # Create a dictionary to store found substrings
    dictionary = {}
    # Use the helper function to search for words in the document
    for i in range(len(document)):
        searchHelper(trie, document, i, dictionary)
        
    print(dictionary)





def main():
    """
    Main function to demonstrate the documentSearch function.
    """
    # Sample input
    document = "little cute cat loves to code in c++, java & python"
    words = ["cute cat", "ttle", "cutest", "cat", "quick", "big"]
    
    # Call the documentSearch function and print the result
    documentSearch(document, words)

if __name__ == "__main__":
    main()