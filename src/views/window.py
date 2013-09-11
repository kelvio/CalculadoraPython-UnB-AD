'''
Created on 09/09/2013

@author: kelvio
'''

import pygtk
pygtk.require('2.0')
import gtk

class Window(gtk.Window):

    def __init__(self):
        # create a new window
        super(Window, self).__init__()
        
        self.connect("destroy", gtk.main_quit)
        self.set_size_request(250,380)
        self.set_position(gtk.WIN_POS_CENTER)        
                            
        self.set_resizable(False)
        self.set_title("Calculadora")
        
        self.connect("destroy",gtk.main_quit) #window is connected with 'destroy' signal,
        #window is closed when we press 'close x' at top right corner
                                                        
        self.table = gtk.Table(6,4,False) # a table is created with 6 rows and 4 columns
        self.add(self.table)      # a table is added to the window     

        self.entry = gtk.Entry()      # text entry is created
        self.table.attach(self.entry,0,4,0,1)  #attached to the table

        self.button = gtk.Button("Fechar")      #buttons are created
        self.table.attach(self.button,0,1,1,2)  #attached to the table 
        self.button.connect("clicked",gtk.main_quit)#the application gets terminated when we click on the close button

        self.button = gtk.Button("CE")
        self.table.attach(self.button,1,2,1,2)

        self.button = gtk.Button("Clr")
        self.table.attach(self.button,2,3,1,2)
        self.button.connect("clicked", self.clear)

        self.button = gtk.Button("%")
        self.table.attach(self.button,3,4,1,2)
        self.button.connect("clicked",self.print_buttonText,"%")

        self.button = gtk.Button("7")
        self.table.attach(self.button,0,1,2,3)
        self.button.connect("clicked",self.print_buttonText,"7")

        self.button = gtk.Button("8")
        self.table.attach(self.button,1,2,2,3)
        self.button.connect("clicked",self.print_buttonText,"8")

        self.button = gtk.Button("9")
        self.table.attach(self.button,2,3,2,3)
        self.button.connect("clicked",self.print_buttonText,"9")

        self.button = gtk.Button("/")
        self.table.attach(self.button,3,4,2,3)
        self.button.connect("clicked",self.print_buttonText,"/")
        
        self.button = gtk.Button("4")
        self.table.attach(self.button,0,1,3,4)
        self.button.connect("clicked",self.print_buttonText,"4")

        self.button = gtk.Button("5")
        self.table.attach(self.button,1,2,3,4)
        self.button.connect("clicked",self.print_buttonText,"5")

        self.button = gtk.Button("6")
        self.table.attach(self.button,2,3,3,4)
        self.button.connect("clicked",self.print_buttonText,"6")

        self.button = gtk.Button("*")
        self.table.attach(self.button,3,4,3,4)
        self.button.connect("clicked",self.print_buttonText,"*")
        
        self.button = gtk.Button("1")
        self.table.attach(self.button,0,1,4,5)
        self.button.connect("clicked",self.print_buttonText,"1")        
        
        self.button = gtk.Button("2")
        self.table.attach(self.button,1,2,4,5)
        self.button.connect("clicked",self.print_buttonText,"2")

        self.button = gtk.Button("3")
        self.table.attach(self.button,2,3,4,5)
        self.button.connect("clicked",self.print_buttonText,"3")

        self.button = gtk.Button("-")
        self.table.attach(self.button,3,4,4,5)
        self.button.connect("clicked",self.print_buttonText,"-")

        self.button = gtk.Button("0")
        self.table.attach(self.button,0,1,5,6)
        self.button.connect("clicked",self.print_buttonText,"0")

        self.button = gtk.Button(".")
        self.table.attach(self.button,1,2,5,6)
        self.button.connect("clicked",self.print_buttonText,".")

        self.button = gtk.Button("=")
        self.table.attach(self.button,2,3,5,6)        
        self.button.connect("clicked",self.calculate)

        self.button = gtk.Button("+")
        self.table.attach(self.button,3,4,5,6)
        self.button.connect("clicked",self.print_buttonText,"+")        

        self.show_all()
                    
    def print_buttonText(self,widget,operand):
        self.entry.insert_text(operand,position = 20)
        
    def clear(self, widget):
        self.entry.set_text("")
        
    def calculate(self, widget):
        print("Calculando resultado:" + self.entry.get_text());