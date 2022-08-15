# Sahko.tk data fetch thingamabob for Jukeboyy.
###############################################

# Import some libraries
import requests
import json
import tkinter as tk # We define new namespace for tkinter and call it tk


# Class for storing pricedata
class pricedata:
    now = 0
    min = 0
    max = 0
    avg = 0
    avg_28 = 0


# Function to get site data, parse it and set it to tk variables.
def getdata():

    # Get data from sahko.tk
    response = requests.get("https://sahko.tk/")
    datahtml = response.content.decode("utf-8") # Convert bytes formatted response to string.

    # Scrape all the relevant data from the raw html

    startpos = datahtml.find("t= ") # Get the position where the raw json string starts
    endpos = datahtml.find(";$(") # Get the position where the raw jsno string ends
    datajson = json.loads(datahtml[startpos+3:endpos]) # Parse the string to json object.

    # Place the data to pricedata class (You can technically skip this step and place the values directly where you want it, but I chose to use this)
    pricedata.now = datajson['now']
    pricedata.min = datajson['min']
    pricedata.max = datajson['max']
    pricedata.avg = datajson['avg']
    pricedata.avg_28 = datajson['avg_28']

    # Set data to tkvariables. tkvariables are used to update the tk labels. These are variables specific to tk library.
    tkvarnow.set(pricedata.now)
    tkvarminmax.set(pricedata.min + " / " + pricedata.max)
    tkvaravg.set(pricedata.avg)
    tkvaravg_28.set(pricedata.avg_28)



## Start and define TK window

# Main Window
main = tk.Tk() # Declare new window
main.geometry("300x200") # Set window size
main.title('sahko.tk') # Set window title
main.resizable(0, 0) # Force window to fixed size


# Define tk textvariables. These are tkvariables used to update the lables dynamically
tkvarnow = tk.StringVar()
tkvarminmax = tk.StringVar()
tkvaravg = tk.StringVar()
tkvaravg_28 = tk.StringVar()


# Place items to main window. Items are placed in grid. Grid geometry is not defined.

# Price now
now_label = tk.Label(main, text="Now: ")
now_label.grid(column=0, row=0, padx=5, pady=5)

now_data = tk.Label(main, textvariable=tkvarnow)
now_data.grid(column=1, row=0, padx=5, pady=5)

# Price min/max
minmax_label = tk.Label(main, text="Min/Max: ")
minmax_label.grid(column=0, row=1, padx=5, pady=5)

minmax_data = tk.Label(main, textvariable=tkvarminmax)
minmax_data.grid(column=1, row=1, padx=5, pady=5)

# Price avg
avg_label = tk.Label(main, text="Avg 7: ")
avg_label.grid(column=0, row=2, padx=5, pady=5)

avg_data = tk.Label(main, textvariable=tkvaravg)
avg_data.grid(column=1, row=2, padx=5, pady=5)

# Price avg_28
avg_28_label = tk.Label(main, text="Avg 28: ")
avg_28_label.grid(column=0, row=3, padx=5, pady=5)

avg_28_data = tk.Label(main, textvariable=tkvaravg_28)
avg_28_data.grid(column=1, row=3, padx=5, pady=5)


# Get new prices button. This button calls the getdata function which gets the data from sahko.tk and updates the labels with the data.
get_data_button = tk.Button(main, text="Get data", command=getdata)
get_data_button.grid(column=1, row=4, padx=5, pady=5)


# Start mainloop for window main.
main.mainloop()
