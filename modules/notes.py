from .funcs import *
console = Console(theme=myTheme)

def menu_notes_main():
    b = -1
    while not b==0:
        MARKDOWN = """
                    :arrow_forward:   Welcome Work Manager admin panel :
                    :arrow_forward:   Notes Menu :

                        :one:        Show all notes
                        :two:        Show the n last notes
                        :three:        Show notes for a specific date
                        :four:        Add a note
                        :five:        Update a note
                        :six:        Remove a note
                        :zero:        Back
                """
        console.print(MARKDOWN)
        b = int(get_selection())
    return b