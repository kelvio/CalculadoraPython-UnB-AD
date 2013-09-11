from views.window import Window;

import gtk
        

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    window = Window();        
    gtk.main()
