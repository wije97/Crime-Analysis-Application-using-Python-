from tkinter import *
from tkinter.ttk import Style


window = Tk()
style = Style(window)

heading = Frame(master=window, height=80, bg='blue')
heading.pack(fill=X)

#heading
heading_lbl = Label(master=window, text="Crime Frequency Analysis 2020 vs 2021", font = ("arial", 15, "bold"),fg='white', bg='blue', padx = 20).place(x=90,y=20)

rb_crime_type = StringVar(window, "All types")
rb_year = StringVar(window, "2020")
rb_place = StringVar(window, "Southwales")
rb_year_analyze = StringVar(window, "2020")
rb_analyze_type = StringVar(window, "Crime type")

def ShowCrime():
    crime = rb_crime_type.get()
    return crime

def ShowYear():
    return rb_year.get()

def ShowPlace():
    return rb_place.get()


def func_get_bar_Chart():
    selected_crime = ShowCrime()
    selected_year = ShowYear()
    selected_city = ShowPlace()

    #print(selected_crime + " " + selected_year + " " + selected_city)


def radio_buttons():

    crimes = [("All Types", "All types"), ("Anti-Social Behaviour", "Anti-Social Behaviour"), ("Violence and Sexual Offences", "Violence and Sexual Offences"), ("Public Order", "Public Order"), ("Criminal Damage and Arson", "Criminal Damage and Arson"), ("Shoplifting", "Shoplifting"), ("Vehicle Crime", "Vehicle Crime"),
            ("Drugs", "Drugs"), ("Burglary", "Burglary"),("Possession of Weapons", "Possession of Weapons"),("Robbery", "Robbery"), ("Bicycle Theft", "Bicycle Theft"), ("Theft from the Person", "Theft from the Person"), ("Other Theft", "Other Theft"), ("Other Crime", "Other Crime")]

    years = [("2020", "2020"), ("2021", "2021")]

    places = [("Southwales", "Southwales"), ("WestYorkshire", "WestYorkshire")]

    analyze_type = [("Crime Type", "Crime type"), ("Month", "month")]

    #add crime types radio buttons
    label1 = Label(master=window, text="Choose Crime Type",font = ("arial", 8, "bold"), bg="light blue", width=50, padx = 20).place(x=10,y=90)
    i = 10
    j = 120
    for type, val in crimes:
        if j == 280:
            j=120
            i+= 190
        Radiobutton(window, text=type, padx = 20, font = ("arial", 8, "bold"), variable=rb_crime_type, command=ShowCrime, value=val).place(x=i,y=j)
        j += 20

    #add year radio buttons
    label2 = Label(master=window, text="Choose Year", font = ("arial", 8, "bold"), bg="light blue", width=15, padx = 20).place(x=420,y=90)
    i = 420
    j = 120
    for year, val in years:
        Radiobutton(window, text=year, padx = 20, font = ("arial", 8, "bold"), variable=rb_year, command=ShowYear, value=val).place(x=i,y=j)
        j += 20

    #add city radio buttons
    label3 = Label(master=window, text="Choose City", font = ("arial", 8, "bold"), bg="light blue",width=15, padx = 20).place(x=420,y=180)
    i = 420
    j = 210
    for place, val in places:
        Radiobutton(window, text=place, padx = 20, font = ("arial", 8, "bold"), variable=rb_place, command=ShowPlace, value=val).place(x=i,y=j)
        j += 20

    label3_2 = Label(master=window, text="Choose Analyze Type", font=("arial", 8, "bold"), bg="light blue", width=15, padx=20).place(x=30, y=410)
    i = 30
    j = 440
    for type, val in analyze_type:
        Radiobutton(window, text=type, padx=20, font=("arial", 8, "bold"), variable=rb_place, command=ShowPlace, value=val).place(x=i, y=j)
        j += 20

    label3_3 = Label(master=window, text="Choose Year", font=("arial", 8, "bold"), bg="light blue", width=15, padx=20).place(x=240, y=410)
    i = 240
    j = 440
    for year, val in years:
        Radiobutton(window, text=year, padx=20, font=("arial", 8, "bold"), variable=rb_place, command=ShowPlace, value=val).place(x=i, y=j)
        j += 20


def add_butons():

    #add chart buttons
    label4 = Label(master=window, text="Choose Chart to Analyze", font = ("arial", 8, "bold"), bg="light green",width=73, padx = 20).place(x=10,y=300)
    btn_bar = Button(window, text="Bar", width=17, fg="black", padx=3, command=func_get_bar_Chart, pady=3).place(x=10,y=330)
    btn_pie = Button(window, text="Pie", width=17, fg="black", padx=3, pady=3).place(x=150,y=330)
    btn_line = Button(window, text="Line", width=17, fg="black", padx=3, pady=3).place(x=290,y=330)
    btn_line = Button(window, text="Density Map", width=17, fg="black", padx=3, pady=3).place(x=430, y=330)

    #add chart buttons
    label5 = Label(master=window, text="Choose Year to Analyze Crime Rate between Both Cities", font = ("arial", 8, "bold"), bg="yellow",width=73, padx = 20).place(x=10,y=380)
    btn_2020 = Button(window, text="Bar Chart", width=17, fg="black", padx=3, pady=3).place(x=430,y=410)
    btn_2021 = Button(window, text="Line Chart", width=17, fg="black", padx=3, pady=3).place(x=430,y=450)


radio_buttons()
add_butons()

quit = Button(window, text="Quit", width=17, fg="red", command=quit, padx=3, pady=3).place(x=430, y=500)

window.title('Crime Analysis')
window.geometry("580x555")
window.mainloop()
