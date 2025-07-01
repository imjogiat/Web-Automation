import tkinter as tk
import os


class WebAutomateApp():

    def __init__(self,root_i):
        #define the widgets for the gui 
        self.root = root_i
        self.root.title("Web Automation Tool")
        
        #Creating a log in frame
        self.loginframe = tk.Frame(self.root)
        self.loginframe.pack(padx=10, pady=10)

        tk.Label(self.loginframe, text="Username ").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self.loginframe).grid(row=0, column=1, sticky="ew")

        tk.Label(self.loginframe, text="Password ").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self.loginframe).grid(row=1, column=1, sticky="ew")

        #Creating submission frame
        self.submsnframe = tk.Frame(self.root)
        self.submsnframe.pack(padx=10, pady=10)

        tk.Label(self.submsnframe, text="Full Name ").grid(row=0, column=0, sticky="w")
        self.fullname_entry = tk.Entry(self.submsnframe).grid(row=0, column=1, sticky="ew")

        tk.Label(self.submsnframe, text="Email ").grid(row=1, column=0, sticky="w")
        self.email_entry = tk.Entry(self.submsnframe).grid(row=1, column=1, sticky="ew")

        tk.Label(self.submsnframe, text="Current Address ").grid(row=2, column=0, sticky="w")
        self.curr_addr_entry = tk.Entry(self.submsnframe).grid(row=2, column=1, sticky="ew")

        tk.Label(self.submsnframe, text="Permanent Address ").grid(row=3, column=0, sticky="w")
        self.perm_addr_entry = tk.Entry(self.submsnframe).grid(row=3, column=1, sticky="ew")

        #Create frame for the submit and close buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(padx=10, pady=10)
        
        self.submit_button = tk.Button(self.buttons_frame, text="Submit").grid(row=4, column=0, sticky="w")
        self.close_button = tk.Button(self.buttons_frame, text="Close").grid(row=4, column=1, sticky="e")


    def submit_data(self):
        pass


    def close_browser(self):
        pass




MyRoot = tk.Tk()
MyWebAutoApp = WebAutomateApp(MyRoot)
MyRoot.mainloop()