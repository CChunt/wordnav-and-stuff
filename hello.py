import hyperdiv as hd
import pickle
import chains

with open("graph.pkl", 'rb') as f:
    graph = pickle.load(f)

def main():
    with hd.box(
            gap=1,
            padding=1,
            justify="center"
    ):
        chain = chains.generate_chain(15)
        print(chain)
        hd.text(chain[1][0])
        
        for i in range(1, len(chain) - 1):
            with hd.scope(i):
                hd.text(chain[i][0][0])
                
        hd.text(chain[-1][0])
        

hd.run(main)
