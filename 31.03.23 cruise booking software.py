#import library
from tkinter import *
import tkinter.messagebox as box

#define the subroutine
   
def calculate():
 
 
    if  itinerary.get() == destination_list[0]:
        total = 2400 * no_passengers.get()
       
    if itinerary.get() == destination_list[1]:
       total = 3800*no_passengers.get()
       
    if itinerary.get() == destination_list[2]:
       total = 4800*no_passengers.get()
       
    if itinerary.get()== destination_list[3]:
       total = 2000*no_passengers.get()
   
    if itinerary.get() == destination_list[4]:
       total = 3000*no_passengers.get()

    if itinerary.get() == destination_list[5]:
       total = 3500*no_passengers.get()

    print(total)
    box.showinfo("Total is: ", total)

    nameinfo = name_of_pass.get()
    no_travellers = no_passengers. get()
    destinations =itinerary.get()
    selected_dates=travel_dates.get()

   
    Summ = "Hello "+ str(nameinfo)+ "," "\n" "You are querying for " +str(no_travellers)+ " passengers. Your destination is: "+ str(destinations)+ "\n" "Your trip dates are: "+ str(selected_dates)+ ". Total cost is: £ "+str(total)
    myLabel = Label(window, text= str(Summ))
    myLabel.pack()

    cust_file = open("custinfo.txt","a")
    cust_file.write(nameinfo + str(no_travellers) + destinations + selected_dates + str(total)+"\n")
    cust_file.close()
    print("Customer info added to the file!")
               

def confirm():
    myLabel1= Label(window, text="Your place is reserved! Have a nice trip!")
    myLabel1.pack()

#define the top container
    
window = Tk()

window.geometry("800x500")

window.configure(background = "light blue")
window.title("Welcome to Bluefin Holidays")

frame = Frame(window, width=700, height=500)
frame.pack()
frame.place(anchor="center", relx=0.5, rely=0.5)

titleframe =LabelFrame(frame, text= "Get a Quote and Reserve")
titleframe.grid(row=0, column=1, sticky="w",padx="30",pady = "30")


#create variables

no_passengers=IntVar(window)
   
itinerary = StringVar(window)

travel_dates= StringVar(window)

name_of_pass= StringVar(window)


itinerary.set("Select a destination")
travel_dates.set("Select date")


destination_list=["Caribbean- £2400 pp","Australia- £3800pp","Japan- £4800pp","Meditterenian - £2000pp","South Africa- £3000pp","South America- £3500pp"]
chosen_date=["12-24th Jan", "12-24th Feb", "12-24th March", "12-24th April", "12-24th May", "12-24th June","12-24th July","12-24th Aug","12-24th Sept","12-24th Oct","12-24th Nov","12-24th Dec"]

#5.1-create the widgets and place on the grid 

passengers = Label(titleframe, text="No of Passengers").grid(row=1, column = 0, sticky ="w", padx="20")
selected_passengr = Entry(titleframe,textvariable= no_passengers ).grid(row=1,column=1,sticky="e", padx="20")

names = Label(titleframe, text="Name/ Surname").grid(row=7,column=0,sticky="w", padx="20")
name = Entry(titleframe, textvariable= name_of_pass).grid(row =7,column=1,sticky="e", padx="20")

destination = Label(titleframe, text="Destination").grid(row=2,column=0,sticky="w", padx="20")
destination_options =OptionMenu(titleframe,itinerary,*destination_list).grid(row=2,column=1,sticky="e", padx="20")

dateselected= Label(titleframe, text="Date").grid(row=3,column=0,sticky="w", padx="20")
selected_dates=OptionMenu(titleframe,travel_dates,*chosen_date).grid(row=3,column=1,sticky="e", padx="20")

                         
confirm_button = Button(titleframe, text= "Confirm Reservation", command=confirm).grid(row=12,column=1,sticky="e", padx="35")
calculate_button=Button(titleframe, text="Calculate", command=calculate).grid(row=9, column=1, sticky="e", padx="35")
           


#7-call the mainloop methods on the top container

window.mainloop()
