from .funcs import *
from .vars import *

console = Console(theme=myTheme)

def add_project():
    df = pd.read_parquet(projects_dir+"table.parquet")
    title = input("Project Title : ")
    while title in df.Title.unique():
        title = input("Project already exists, give another title  : ")
    
    desc = input("Description : ")
    dep = input("Departement : ")
    check  = False
    while not check:
        check = True
        console.print("""
                        :arrow_forward:   Choices:
                        :one:        :repeat:   Ongoing
                        :two:        :white_check_mark:   Completed
                        :three:        :x:   Canceled

                        """)
        status_t = int(input("Enter your choice : "))

        while not status_t:
            console.print("""
                        :arrow_forward:   Choices:
                        :one:        :repeat:   Ongoing
                        :two:        :white_check_mark:   Completed
                        :three:        :x:   Canceled

                        """)
            status_t = int(input("Enter your choice : "))
        if status_t==1:
            status= "Ongoing"
        elif status_t==2:
            status= "Completed" 
        elif status_t==3:
            status= "Canceled"
        else:
            check = False
            console.print("False Input, try again",style="bad")        

    path = projects_dir+"textfiles/"
    id = df.id.max()+1
    f = open(path+str(id)+".txt", "w+")
    f.write(desc)
    f.close()
    d = {
            "id" : id,
            "Title" : title,
            "Description" : str(id)+".txt",
            "Status" : status,
            "Departement" : dep,
        }
    df = df.append(d,ignore_index=True)
    check = get_confirmation("Add the new project to the database")
    if check:
        df.to_parquet(projects_dir+"table.parquet")
        console.print(":heavy_check_mark: Operation Done : Porject Added to the database !!n",style="good")
        time.sleep(3)
    else:
        console.print(":x: Operation Canceled !!",style="warning")
        time.sleep(3)


def show_projects():
    df = pd.read_parquet(projects_dir+"table.parquet")
    table = Table(title="Projects List")
    table.add_column("Title", justify="center",style="white", no_wrap=True)
    table.add_column("Description", justify="center",style="white")
    table.add_column("Department", justify="center", style="white")
    table.add_column("Status", justify="center", style="white")
    for i in range(df.shape[0]):
        f = open(projects_dir+"textfiles/"+df.iloc[i].Description, "r")
        table.add_row(df.iloc[i].Title,f.read(),df.iloc[i].Departement,df.iloc[i].Status)
        f.close()
    console = Console()
    console.print(table)

    print()
    print()
    input("Press Enter if you want to go back : ")

def menu_projects_main():
    clear()
    b = -1
    while not b==0:
        clear()
        MARKDOWN = """
                    :arrow_forward:   Welcome Work Manager admin panel :
                    :arrow_forward:   Projects Menu :
                    
                        :one:        Show all projects
                        :two:        Add a project
                        :three:        Update a project
                        :four:        Remove a project
                        :zero:        Back
                """
        console.print(MARKDOWN)
        b = int(get_selection())
        if b==1:
            show_projects()
        elif b==2:
            add_project()
    return b
