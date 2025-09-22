import hyperdiv as hd
import pickle
import chains

with open("graph.pkl", 'rb') as f:
    graph = pickle.load(f)

chain = chains.generate_chain(8)
guessed_words = [w[0][0] for w in chain]
guessed_words[0] = chain[0][0]
guessed_words[-1] = chain[-1][0]

def main():
    global guessed_words
    with hd.box(
            gap=1,
            padding=1,
            justify="center"
    ):
        print(chain)
        
        for i in range(0, len(guessed_words)):
            with hd.scope(i):
                # hd.text(chain[i][0][0])
                word = guessed_words[i]
                hd.text(word)
        
        text_input = hd.text_input(value="Guess here...")
        state = hd.state(i = 1)
        if state.i == len(chain) - 1:
            # player wins, all words guessed
            pass
        if text_input.value == chain[state.i][0]:
            guessed_words[state.i] = chain[state.i][0]
            print(guessed_words)
            state.i += 1
            text_input.value = ""
        

hd.run(main)
