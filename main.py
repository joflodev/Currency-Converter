import tkinter as tk
from tkinter import *
#hi
class Currency_lables:
    def __init__(self, root):
        self.root = root
        self.root.title("Converter")
        self.wanted_currency =StringVar(value="Choose currency?")
        self.chosen_currency =StringVar(value="Choose currency?")
        self.currency =["USD", "S-Franken", "R-Rubel", "Pfund"]
        # Label
        self.label = tk.Label(root, text=self.chosen_currency)
        self.label.grid(row=1, column=0, columnspan=2)

        # Entry-Feld
        self.entry = tk.Entry(root)
        self.entry.grid(row=0, column=0, rowspan=2)


        self.chosen_dropdown = tk.Label(root, text="Euro")
        self.chosen_dropdown.grid(row=2, column=0,columnspan=2)

        self.wanted_dropdown = OptionMenu(root, self.wanted_currency, *self.currency)
        self.wanted_dropdown.grid(row=2, column=3,columnspan=2)

        self.button = tk.Button(root, text="MLT",command=self.MLT)
        self.button.grid(row=3,columnspan=3)
        self.button.config(height=1, width=10)
        # Label für Ausgabe
        self.output_label = tk.Label(root, text="")
        self.output_label.grid(row=1, column=3, columnspan=2)
        self.anzeigen()
    def MLT(self):
        #print("lisa")
        #print(self.wanted_currency.get())
        if self.wanted_currency.get()== "Choose currency?":
            self.wanted_currency.set("Währung auswähle")  # Changes selection to "USD"

        else:      
            self.wanted_currency.set("Choose currency?")
    def anzeigen(self):
        
        if self.entry.get():
            #print(self.wanted_currency.get())
            amount= float(self.entry.get())
            if self.wanted_currency.get()=="USD":   
                self.output_label.config(text=f"{amount*1.13} {self.wanted_currency.get()}")
            if self.wanted_currency.get()=="S-Franken":   
                self.output_label.config(text=f"{amount*0.94} {self.wanted_currency.get()}")
            if self.wanted_currency.get()=="R-Rubel":   
                self.output_label.config(text=f"{amount*89.96} {self.wanted_currency.get()}")
            if self.wanted_currency.get()=="Pfund":
                self.output_label.config(text=f"{amount*0.84} {self.wanted_currency.get()}")            
        else:
            self.output_label.config(text="")
        self.root.after(1000,self.anzeigen)
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")

    
    gui = Currency_lables(root)
    root.mainloop()

