"""
Suffix Tries
A suffix trie is a 
type of trie that is used to store all the
suffixes of a given string.
It is particularly useful for tasks such as substring
search and pattern matching.

"""

# Build a Suffix Trie
class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}  # Dictionary to store child nodes
        self.is_terminal = False  # Indicates if the node is the end of a word
    
class SuffixTrie:
    def __init__(self):
        self.root = Node("")
    
    def insert_helper(self, word):
        temp = self.root    # Start from the root node
        for char in word:
            # If the character is not already a child of the current node, add it
            if char not in temp.children:
                temp.children[char] = Node(char)
            # Move to the child node
            temp = temp.children[char]
        # Mark the last node as terminal to indicate the end of a word
        temp.is_terminal = True
    
    def insert(self, word):
        # pick all substrings from (i, n) and insert them into the trie
        for i in range(len(word)):
            self.insert_helper(word[i:])
            

    def search(self, word):
        # Start from the root node
        temp = self.root
        for char in word:
            # If the character is not found in the children, return False
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
    # Create a SuffixTrie object
    suffix_trie = SuffixTrie()
    
    # Insert words into the SuffixTrie
    words = ["banana", "bandana", "an"]
    for word in words:
        suffix_trie.insert(word)
    
    # Search for substrings in the SuffixTrie
    search_words = ["ana", "ban", "na", "dana"]
    for word in search_words:
        print(f"Searching for '{word}': {suffix_trie.search(word)}")
    
    # Check for prefixes in the SuffixTrie
    prefixes = ["ba", "an", "band"]
    for prefix in prefixes:
        print(f"Checking prefix '{prefix}': {suffix_trie.starts_with(prefix)}")

if __name__ == "__main__":
    main()