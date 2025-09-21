import hyperdiv as hd

def main():
    hd.markdown(
        """
        # Made a freakign website
        ## The world's **greatest** website
        ---
        * has bullet points
        * multiple bullet points
        """
    )

    hd.checkbox("<- check this if website made", checked=True)
    hd.button("World's greatest button")

hd.run(main)
