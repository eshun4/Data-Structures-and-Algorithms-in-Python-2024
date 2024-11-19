# Define the graph using a dictionary
offer_network = {
    'Company_A': set(['Company_B', 'Company_D']),
    'Company_B': set(['Company_A', 'Company_C']),
    'Company_C': set(['Company_B', 'Company_D']),
    'Company_D': set(['Company_A', 'Company_C'])
}

def DFS(offer_network, start_company, visited_offers):
    """
    Function implementing the DFS algorithm to traverse the graph.
    """
    visited_offers.add(start_company)
    print(start_company, end=' --> ')
    
    for partner in offer_network[start_company]:
        if partner not in visited_offers:
            DFS(offer_network, partner, visited_offers)

visited_companies = set()
# Invoke DFS function, starting with 'Company_A'
DFS(offer_network, 'Company_A', visited_companies) 
print('\nVisited companies:', visited_companies) 