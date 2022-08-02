# from funcs import *
from modules.projects import *
from modules.todo import *
from modules.notes import *
from modules.appointments import *
"""
                    # Welcome Work Manager admin panel :
                    
                        :one: To-Do List
                        :two: Appointments
                        :three: Notes
                        :four: Projects 
                        :zero: Exit
                """

if __name__=="__main__":
    clear()
    initiate()
    #login()
    clear()
    a = -1
    while not a==0:
        main_menu()
        a = int(get_selection())
        clear()
        if a==1:
            menu_todo_main()
        if a==2:
            menu_appointments_main()
        if a==3:
            menu_notes_main()
        if a==4:
            menu_projects_main()
        clear()