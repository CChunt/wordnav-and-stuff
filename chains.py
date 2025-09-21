import pandas as pd
import random
import pickle

data = pd.read_csv("two_words.csv")

# create graph with adjacency list hashmap
graph = {w:[] for w in data["c1"].unique()}
for index, row in data.iterrows():
    first, second = row["c1"], row["c2"]
    graph[first].append(second)
    
# cache graph by pickling data
output = open('graph.pkl', 'wb')
pickle.dump(graph, output)
    
def dfs(first, visited, chain, max_length):
    if len(chain) >= max_length:
        return chain

    visited.add(first)
    for second in graph[first]:
        if second in graph and second not in visited:
            chain.append([first, second])
            return dfs(second, visited, chain, max_length)
        
def generate_chain(chain_length):
    chain = None
    while not chain: # starting with a random choice might not always have a solution path
        chain = dfs(random.choice(list(graph.keys())), set(), [], chain_length)
    print(chain)
    return chain

if __name__ == "__main__":
    chain_length = int(input("how long should the chain be?\n"))
    print(generate_chain(chain_length))
    
