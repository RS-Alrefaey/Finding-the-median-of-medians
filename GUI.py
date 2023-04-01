#----- IMPORTS -----
from tkinter import *
from tkinter import ttk
import time
import statistics
import math

import quicksort
import medianOfmeds
import RadixSort
import selectionSort

#------------------------------------------------------------------------------                
# ----- SET UI WINDOW -----
root = Tk()
root.title("Median Finding Algorithms")
root.minsize(250, 400)
root.config(bg = '#297373')
#------------------------------------------------------------------------------            
# ----- VARIABLES -----
dataChoice = StringVar(value = 'Choose the data')
dataState = StringVar(value = 'Choose the data state')
choice = StringVar(value='Pick your algorithm')
total = StringVar()
median = StringVar()
complexity = StringVar()
data = [1]
n= len(data)

#------------------------------------------------------------------------------
# ----- READ DATA -----
        
def readData():
    select = dataChoice.get() # get the data that have been chosen
    global data, n
    if select == "Data 1":
        with open ('../data/data1.txt', 'r') as d:
            data0 = d.readlines()    #to read the content of the data file
            data= [ x.strip() for x in data0]   #to delete the new line character from the data
            for i in range (len(data)):
                data[i] = int(data[i])
    elif select == "Data 2":
        with open ('../data/data2.txt', 'r') as d:
            data0 = d.readlines()    #to read the content of the data file
            data= [ x.strip() for x in data0]   #to delete the new line character from the data
            for i in range (len(data)):
                data[i] = int(data[i])
    elif select == "Data 3":
        with open ('../data/data3.txt', 'r') as d:
            data0 = d.readlines()    #to read the content of the data file
            data= [ x.strip() for x in data0]   #to delete the new line character from the data
            for i in range (len(data)):
                data[i] = int(data[i])
    n = len(data) # reset the value of n
    state = dataState.get() # get the state of data
    if state == "Sorted": # apply sorting if the state eaual to 'Sorted'
        data.sort()

# ----- MENU FUNCTION -----
def selectedAlgorithm():
    if len(data) == 1 or dataState.get() == 'Choose the data state':
        return
    selected =  choice.get()
    if selected == "Quick Sort" : 
        start = time.time()
        quicksort.quickSort(data, 0, n-1)
        if( (n%2) == 0 ):
            m1 = math.floor((n)/2)
            m2 = math.floor((n-1)/2)
            median.set((data[m1] + data[m2])/2)
        else:
            median.set(data[math.floor((n)/2)])
        total.set( time.time() - start)
        complexity.set("This algorithm takes\n O(n^2) in the worst case")
        
#-----------------------------------------------------------------------------  
    elif selected == "Selection Sort" : 
        start = time.time()
        median.set(selectionSort.Median_Selection_Sort(data))
        total.set( time.time() - start)
        complexity.set("This algorithm takes\n O(n^2) in the worst and best case")
#------------------------------------------------------------------------------
    elif selected == "Radix Sort" : 
        start = time.time()
        RadixSort.radixSort(data)
        if( (n%2) == 0 ):
            m1 = math.floor((n)/2)
            m2 = math.floor((n-1)/2)
            median.set((data[m1] + data[m2])/2)
        else:
            median.set(data[math.floor((n)/2)])
        total.set( time.time() - start)
        complexity.set("This algorithm takes\n O(d(n+k))in the worst case")
#------------------------------------------------------------------------------
    elif selected == "Median of medians" : 
        start = time.time()
        
        if( (n%2) == 0 ):
            x= math.floor((n)/2)
            y=math.floor((n-1)/2)       
            m1 = medianOfmeds.medianOfMedians(data,x)
            m2 = medianOfmeds.medianOfMedians(data,y)
            median.set((m1 + m2)/2)
        else:
            x = medianOfmeds.medianOfMedians(data, n // 2)
            median.set(x)
        total.set( time.time() - start)
        complexity.set("This algorithm takes\n O(n) in the worst case")
        
#------------------------------------------------------------------------------ 
        
# ----- GUI SECTION ------
        
#----- HEADER -----
Label(text = "Median Finding", bg = 'white', fg = '#ff8552', \
      font=('Bauhaus 93',30)).grid(row = 0, column = 0, padx = 5, pady = 15)

# ----- UI SELECTION SECTION -----
#BASE
UI_frame = Frame (root, width = 600, height = 150, bg='#e9d758')
UI_frame.grid(row = 3, column =0, padx = 45, pady = 10)

#TEXT = algorithm
Label(UI_frame, text = "Algorithm", bg='white', fg = '#297373',font=('Comic Sans MS',12)).grid(row =3, column = 0,padx = 15, pady = 10)

#COMBOBOX = select algorithm
algMenu = ttk.Combobox(UI_frame, textvariable = choice, \
          values =['Selection Sort', 'Quick Sort', 'Radix Sort','Median of medians'])
algMenu.grid(row =3, column = 1, padx = 5, pady = 5)

#TEXT = data
Label(UI_frame, text = "Data", bg='white', fg = '#297373',font=('Comic Sans MS',12)).grid(row =5, column = 0,padx = 15, pady = 10)

#COMBOBOX = select data
algMenu = ttk.Combobox(UI_frame, textvariable = dataChoice, \
          values =['Data 1', 'Data 2', 'Data 3'])
algMenu.grid(row =5, column = 1, padx = 5, pady = 5)

#TEXT = data state
Label(UI_frame, text = "Data State", bg='white', fg = '#297373',font=('Comic Sans MS',12)).grid(row =6, column = 0,padx = 15, pady = 10)

#COMBOBOX = select state
algMenu = ttk.Combobox(UI_frame, textvariable = dataState, \
          values =['Sorted', 'Unsorted'])
algMenu.grid(row =6, column = 1, padx = 5, pady = 5)

#TEXT = time
Label(UI_frame, text = "Time", bg='white', fg = '#297373',font=('Comic Sans MS',12)).grid(row =7, column = 0,padx = 15, pady = 10)

#TEXT = Calculated time
Label(UI_frame, textvariable =total).grid(row=7, column=1, sticky='WE', padx=5, pady=10)

#TEXT = the median is
Label(UI_frame, text = "The Median is", bg='white', fg = '#297373',font=('Comic Sans MS',12)).grid(row =8, column = 0,padx = 15, pady = 10)

#TEXT = median value
Label(UI_frame, textvariable = median).grid(row=8, column=1, sticky='WE', padx=5, pady=10)

#BUTTON = start
Button(UI_frame, text="Start", command= lambda:[readData() ,selectedAlgorithm(), write_to_file()], bg='white',fg="#ff8552",height=1, width=5,font=('Comic Sans MS',10))\
.grid(row = 3, column =3, padx = 15, pady = 10)


canvas =Canvas(root, width = 400, height = 150).grid(row = 7, column = 0, padx=5, pady=15)
Label(canvas, textvariable = complexity, fg = '#ff8552',font=('Comic Sans MS',18)).grid(row =7, column = 0,padx = 15, pady = 5)

def write_to_file(): # Store the information of the analysis
    outfile = open('../info.txt', 'a')
    outfile.write('Data: '+dataChoice.get()+'      Data State: '+dataState.get()+'      Algorithm: '
                  + choice.get()+'      Time: ' +total.get()+ '\n')
    outfile.close()

root.mainloop()