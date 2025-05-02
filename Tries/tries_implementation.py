"""
Trie data structure implementation in Python.
A Trie (pronounced as "try") is a tree-like 
data structure that is used to store a dynamic
set of strings, where the keys are usually strings.
It is particularly useful for tasks such as autocomplete 
and spell checking.
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
    
    def search(self, word):
        # Start from the root node    
        temp = self.root
        for char in word:
            # If the character is not fo    und in the children, return False
            if char not in temp.children:
                return False
            # Move to the child node
            temp = temp.children[char]
        # Return True if the last node is terminal, indicating the word exists in the Trie
        return temp.is_terminal
    
    def starts_with(self, prefix):
        # Start from the root node
        temp = self.root
        for char in prefix:
            # If the character is not found in the children, return False
            if char not in temp.children:
                return False
                # Move to the child node
            temp = temp.children[char]
        # Return True if we reach here, indicating the prefix exists in the Trie
        return True


def main():
    # Create a Trie object
    trie = Trie()
    
    # Insert words into the Trie
    words = ["hello", "hell", "heaven", "heavy"]
    for word in words:
        trie.insert(word)
    
    # Search for words in the Trie
    search_words = ["hello", "hell", "heaven", "heavy", "helloo"]
    for word in search_words:
        if trie.search(word):
            print(f"{word} is present in the Trie")
        else:
            print(f"{word} is not present in the Trie")

if __name__ == "__main__":
    main()