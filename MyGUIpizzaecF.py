import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self._main_window = tkinter.Tk()
        self._main_window.title('Pizza Order')

        # frames
        self._top_frame = tkinter.Frame(self._main_window)
        self._mid_frame = tkinter.Frame(self._main_window)
        self._mid_frame2 = tkinter.Frame(self._main_window)
        self._mid_frame3 = tkinter.Frame(self._main_window)
        self._mid_frame4 = tkinter.Frame(self._main_window)
        self._bottom_frame = tkinter.Frame(self._main_window)

        self.build_name()  # start name order
        self.build_button()  # options with buttons and labels for user

        # run window
        self._top_frame.pack()
        self._mid_frame.pack()
        self._mid_frame2.pack()
        self._mid_frame3.pack()
        self._mid_frame4.pack()
        self._bottom_frame.pack()
        tkinter.mainloop()

    def build_name(self):
        self._prompt_label = tkinter.Label(self._top_frame, text='Name:')
        self._name_entry = tkinter.Entry(self._top_frame, width=10)
        self._prompt_label.pack(padx=(15, 0), pady=15, side="left")
        self._name_entry.pack(padx=15, pady=15, side="left")

    def build_button(self):
        self._radio_var = tkinter.IntVar()  # obj crust
        self._radio_var.set(0)

        self._radio_var2 = tkinter.IntVar()  # obj sauce
        self._radio_var2.set(0)

        self._radio_var4 = tkinter.IntVar()  # obj size
        self._radio_var4.set(0)

        # crust, radio buttons 1 2 3
        self._prompt_radio_label = tkinter.Label(self._mid_frame, text='Pick one of the three crust:')
        self._prompt_radio_label.pack(side="top", anchor="center")
        self._rb1 = tkinter.Radiobutton(self._mid_frame, text="Thin", variable=self._radio_var, value=1)
        self._rb2 = tkinter.Radiobutton(self._mid_frame, text="Regular", variable=self._radio_var, value=2)
        self._rb3 = tkinter.Radiobutton(self._mid_frame, text="Deep Dish", variable=self._radio_var, value=3)
        self._rb1.pack(side='left', anchor="w")
        self._rb2.pack(side='left', anchor="w")
        self._rb3.pack(side='left', anchor="w")

        # sauces, radio buttons 4 5 6
        self._prompt_radio_label = tkinter.Label(self._mid_frame2, text='Pick one of the three sauces:')
        self._prompt_radio_label.pack(side="top", anchor="center")
        self._rb4 = tkinter.Radiobutton(self._mid_frame2, text="Regular", variable=self._radio_var2, value=4)
        self._rb5 = tkinter.Radiobutton(self._mid_frame2, text="BBQ", variable=self._radio_var2, value=5)
        self._rb6 = tkinter.Radiobutton(self._mid_frame2, text="Alfredo", variable=self._radio_var2, value=6)
        self._rb4.pack(side='left', anchor="w")
        self._rb5.pack(side='left', anchor="w")
        self._rb6.pack(side='left', anchor="w")

        # toppings, checkbox buttons 1 2 3
        self._cb_var1 = tkinter.IntVar()
        self._cb_var2 = tkinter.IntVar()
        self._cb_var3 = tkinter.IntVar()
        self._cb_var4 = tkinter.IntVar()
        self._cb_var5 = tkinter.IntVar()
        self._cb_var1.set(0)
        self._cb_var2.set(0)
        self._cb_var3.set(0)
        self._cb_var4.set(0)
        self._cb_var4.set(0)
        self._prompt_checkbox_label = tkinter.Label(self._mid_frame3, text='Pick any of the following toppings:')
        self._prompt_checkbox_label.pack(side='top', anchor="center")
        self._cb1 = tkinter.Checkbutton(self._mid_frame3, text="Pepperoni", variable=self._cb_var1)
        self._cb2 = tkinter.Checkbutton(self._mid_frame3, text="Sausage", variable=self._cb_var2)
        self._cb3 = tkinter.Checkbutton(self._mid_frame3, text="Onions", variable=self._cb_var3)
        self._cb4 = tkinter.Checkbutton(self._mid_frame3, text="Olives", variable=self._cb_var4)
        self._cb5 = tkinter.Checkbutton(self._mid_frame3, text="Mushroom", variable=self._cb_var5)
        self._cb1.pack(side='left', anchor="w")
        self._cb2.pack(side='left', anchor="w")
        self._cb3.pack(side='left', anchor="w")
        self._cb4.pack(side='left', anchor="w")
        self._cb5.pack(side='left', anchor="w")

        # sizes, radio buttons 7 8 9
        self._prompt_radio_label = tkinter.Label(self._mid_frame4, text='Pick one of the three crust:')
        self._prompt_radio_label.pack(side="top", anchor="center")
        self._rb7 = tkinter.Radiobutton(self._mid_frame4, text="Small", variable=self._radio_var4, value=7)
        self._rb8 = tkinter.Radiobutton(self._mid_frame4, text="Medium", variable=self._radio_var4, value=8)
        self._rb9 = tkinter.Radiobutton(self._mid_frame4, text="Large", variable=self._radio_var4, value=9)
        self._rb7.pack(side='left', anchor="w")
        self._rb8.pack(side='left', anchor="w")
        self._rb9.pack(side='left', anchor="w")

        # buttons for bottom frame
        self._order_button = tkinter.Button(self._bottom_frame, text="Order", command=self.order)
        self._quit_button = tkinter.Button(self._bottom_frame, text="Quit", command=self._main_window.destroy)

        self._order_button.pack(side='left', pady=15, padx=15)
        self._quit_button.pack(side='left', padx=(0, 15))

    def order(self):
        # including errors
        # get name of order
        customer = self._name_entry.get()
        # if no entered name, error
        if len(customer) == 0:
            tkinter.messagebox.showwarning("", "Name not entered")
        # if numbers in name box, error
        elif customer.isnumeric():
            tkinter.messagebox.showerror("", "Please enter a valid name")
        # if no crust selected, error
        elif self._radio_var.get() == 0:
            tkinter.messagebox.showwarning("", "Please select a crust")
        # if no sauce selected, error
        elif self._radio_var2.get() == 0:
            tkinter.messagebox.showwarning("", "Please select a sauce")
        # Not even one of the sizes is chosen, issue just an alert
        elif self._radio_var4.get() == 0:
            tkinter.messagebox.showwarning("", "Please select a size")
        else:   # calculated code starts here
            total_cost = 10
            if self._radio_var4.get() == 8:
                total_cost += 1.50
            elif self._radio_var4.get() == 9:
                total_cost += 3.00
            if self._cb_var1.get() == 1:
                total_cost += 0.50
            if self._cb_var2.get() == 1:
                total_cost += 0.50
            if self._cb_var3.get() == 1:
                total_cost += 0.50
            if self._cb_var4.get() == 1:
                total_cost += 0.50
            if self._cb_var5.get() == 1:
                total_cost += 0.50

            tkinter.messagebox.showinfo("Order Received",
                                        f"Thank you {self._name_entry.get()}, we have received your pizza order!\n"
                                        f"You Selected: {self.print_crust_names()}, "
                                        f"{self.print_sauce_names()}, {self.print_toppings_names()}"
                                        f" and {self.print_size_names()}.\n"
                                        f"The Total Price is ${total_cost:.2f}.\n")

    # print user selected options
    def print_crust_names(self):
        message = ""
        any_selected = False
        if self._radio_var.get() == 1:
            any_selected = True
            message += "Thin Crust"
        if self._radio_var.get() == 2:
            any_selected = True
            message += "Regular Crust"
        if self._radio_var.get() == 3:
            any_selected = True
            message += "Deep Dish Crust"
        if not any_selected:  # if still false
            message += "No crust selected"
        return f"{message}"

    def print_sauce_names(self):
        message = ""
        any_selected = False
        if self._radio_var2.get() == 4:
            any_selected = True
            message += "Regular Sauce"
        if self._radio_var2.get() == 5:
            any_selected = True
            message += "BBQ Sauce"
        if self._radio_var2.get() == 6:
            any_selected = True
            message += "Alfredo Sauce"
        if not any_selected:  # if still false
            message += "No sauce selected"
        return f"{message}"

    def print_toppings_names(self):
        message = ""
        any_selected = False
        if self._cb_var1.get() == 1:
            any_selected = True
            message += "Pepperoni,"
        if self._cb_var2.get() == 1:
            any_selected = True
            message += "Sausage,"
        if self._cb_var3.get() == 1:
            any_selected = True
            message += "Onions,"
        if self._cb_var4.get() == 1:
            any_selected = True
            message += "Olives,"
        if self._cb_var5.get() == 1:
            any_selected = True
            message += "Mushroom,"
        if not any_selected:  # if still false
            message += "No toppings"
        return f"{message}"

    def print_size_names(self):
        message = ""
        any_selected = False
        if self._radio_var4.get() == 7:
            any_selected = True
            message += "Small Size"
        if self._radio_var4.get() == 8:
            any_selected = True
            message += "Medium Size"
        if self._radio_var4.get() == 9:
            any_selected = True
            message += "Large Size"
        if not any_selected:  # if still false
            message += "No size selected"
        return f"{message}"
