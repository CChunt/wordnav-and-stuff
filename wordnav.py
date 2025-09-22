import hyperdiv as hd
import pickle
import chains

with open("graph.pkl", 'rb') as f:
    graph = pickle.load(f)

chain = chains.generate_chain(chain_length=10,
                              allow_duplicates=False)
guessed_words = [w[0][0] for w in chain]
guessed_words[0] = chain[0][0]
guessed_words[-1] = chain[-1][0]

def main():
    color = "#01261b"
    global guessed_words
    with hd.box(
            gap=1,
            padding=1,
            justify="center",
            background_color=color,
            grow=True,
            min_height="25vh",
    ):
        print(chain)
        hd.text(
            "wordnav",
            font_size="2x-large",
            text_align="center",
            padding = 1,
        )
        
        for i in range(0, len(guessed_words)):
            with hd.scope(i):
                word = guessed_words[i]
                hd.text(
                    word,
                    font_size="large",
                    text_align="start"
                )

        text_input = hd.text_input(
            placeholder="Guess here...",
            font_family="mono",
            font_style="italic",
            autofocus=True
        )
        
        state = hd.state(i = 1)
        if state.i == len(chain) - 1:
            # player wins, all words guessed
            pass
        if text_input.value == chain[state.i][0]:
            guessed_words[state.i] = chain[state.i][0]
            print(guessed_words)
            state.i += 1
            text_input.value = ""

        hd.box(
            background_color=color,
            grow=True,
            min_height="50vh"
        )
        

hd.run(main)
