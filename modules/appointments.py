from .funcs import *
console = Console(theme=myTheme)

def menu_appointments_main():
    b = -1
    while not b==0:
        MARKDOWN = """
                    :arrow_forward:   Welcome Work Manager admin panel :
                    :arrow_forward:   Appointments Menu :
                    
                        :one:        Show all appointments
                        :two:        Show the future appointments
                        :three:        Show appointment for a specific date
                        :four:        Add an appointment
                        :five:        Update an appointment
                        :six:        Remove an appointment
                        :zero:        Back
                """
        console.print(MARKDOWN)
        b = int(get_selection())
    return b