import hyperdiv as hd
import pickle
import chains

with open("graph.pkl", 'rb') as f:
    graph = pickle.load(f)

chain = chains.generate_chain(chain_length=10, allow_duplicates=False)

def main():
    color = "#01261b"
    firsts = [c[0] for c in chain]
    guessed_list = [False for _ in range(len(chain))]    
    state = hd.state(words=firsts,
                     guessed=guessed_list,
                     current=1)
    
    def reset_chain():
        chain = chains.generate_chain(chain_length=10, allow_duplicates=False)
        print(chain)
        firsts = [c[0] for c in chain]
        guessed_list = [False for _ in range(len(chain))]
        state.words = firsts
        state.guessed = guessed_list
        state.current = 1
                
    with hd.box(
            gap=1,
            padding=10,
            justify="center",
            background_color=color,
            grow=True,
            min_height="25vh",
    ):
        hd.text(
            "wordnav",
            font_size="2x-large",
            text_align="center",
            padding = 1,
        )

        hd.text(state.words[0], font_size="large", text_align="start")
        for i in range(1, len(state.words) - 1):
            with hd.scope(i):
                text_color = "red-500" if i == state.current else "neutral-1000"
                string = state.words[i] if state.guessed[i] else state.words[i][0]
                hd.text(
                    string,
                    font_size="large",
                    font_color=text_color,
                    text_align="start",
                )
        hd.text(state.words[-1], font_size="large", text_align="start")
            

        
        text_input = hd.text_input(placeholder="Guess here...")
        if state.current == len(chain) - 1: # player wins, all words guessed
            pass
        if text_input.value == state.words[state.current]:
            #words[curr.i] = chain[curr.i][0]
            state.guessed[state.current] = True
            state.current += 1
            text_input.value = ""

        if hd.button("Reset Chain").clicked:
            reset_chain()
            print(state.guessed)

        hd.box(
            background_color=color,
            grow=True,
            min_height="50vh"
        )
        

hd.run(main)
