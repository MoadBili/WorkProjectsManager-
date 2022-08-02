from .funcs import *
console = Console(theme=myTheme)

def menu_todo_main():
    b = -1
    while not b==0:
        MARKDOWN = """
                    :arrow_forward:   Welcome Work Manager admin panel :
                    :arrow_forward:   To Do List Menu :
                    
                        :one:        Show all items
                        :two:        Show a project's to-do list items
                        :three:        Add a to-do item
                        :four:        Remove a to-do item
                        :five:        Update a to-do item
                        :zero:        Back
                """
        console.print(MARKDOWN)
        b = int(get_selection())
    return b