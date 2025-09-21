import pandas as pd
import random

data = pd.read_csv("two_words.csv")
chain_length = int(input("how long should the chain be?\n"))

# create graph with adjacency list hashmap
graph = {w:[] for w in data["c1"].unique()}
for index, row in data.iterrows():
    first, second = row["c1"], row["c2"]
    graph[first].append(second)
    

def dfs(first, visited, chain, num_chains):
    if num_chains >= chain_length:
        return chain

    visited.add(first)
    for second in graph[first]:
        if second in graph and second not in visited:
            chain.append([first, second])
            return dfs(second, visited, chain, num_chains + 1)
        

chain = None
while not chain: # starting with a random choice might not always have a solution path
    chain = dfs(random.choice(list(graph.keys())), set(), [], 0)
print(chain)
    
