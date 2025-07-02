import tkinter as tk
from tkinter import messagebox
import os
from main import WebAutomatn


class WebAutomateApp():

    def __init__(self,root_i):
        #define the widgets for the gui 
        self.root = root_i
        self.root.title("Web Automation Tool")
        self.web_automatn = WebAutomatn()
        
        #Creating a log in frame
        self.loginframe = tk.Frame(self.root)
        self.loginframe.pack(padx=10, pady=10)

        tk.Label(self.loginframe, text="Username ").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(self.loginframe)
        self.username_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(self.loginframe, text="Password ").grid(row=1, column=0, sticky="w")
        self.password_entry = tk.Entry(self.loginframe)
        self.password_entry.grid(row=1, column=1, sticky="ew")

        #Creating submission frame
        self.submsnframe = tk.Frame(self.root)
        self.submsnframe.pack(padx=10, pady=10)

        tk.Label(self.submsnframe, text="Full Name ").grid(row=0, column=0, sticky="w")
        self.fullname_entry = tk.Entry(self.submsnframe)
        self.fullname_entry.grid(row=0, column=1, sticky="ew")

        tk.Label(self.submsnframe, text="Email ").grid(row=1, column=0, sticky="w")
        self.email_entry = tk.Entry(self.submsnframe)
        self.email_entry.grid(row=1, column=1, sticky="ew")

        tk.Label(self.submsnframe, text="Current Address ").grid(row=2, column=0, sticky="w")
        self.curr_addr_entry = tk.Entry(self.submsnframe)
        self.curr_addr_entry.grid(row=2, column=1, sticky="ew")

        tk.Label(self.submsnframe, text="Permanent Address ").grid(row=3, column=0, sticky="w")
        self.perm_addr_entry = tk.Entry(self.submsnframe)
        self.perm_addr_entry.grid(row=3, column=1, sticky="ew")


        #Create frame for the submit and close buttons
        self.buttons_frame = tk.Frame()
        self.buttons_frame.pack(padx=10, pady=10)
        
        self.submit_button = tk.Button(self.buttons_frame, text="Submit", command=self.submit_data).grid(row=4, column=0, sticky="w", padx=5)
        self.close_button = tk.Button(self.buttons_frame, text="Close browser", command=self.close_browser).grid(row=4, column=1, sticky="e", padx=5)


    def submit_data(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        fullname = self.fullname_entry.get()
        email = self.email_entry.get()
        curr_address = self.curr_addr_entry.get()
        perm_address = self.perm_addr_entry.get()
        
        self.web_automatn.login(username_i=username, password_i=password)
        self.web_automatn.fill_form(fullname_i=fullname, email_i=email, currentaddress_i=curr_address, permaddress_i=perm_address)
        self.web_automatn.download()


    #not closing from close button
    def close_browser(self):
        print("closing...")
        self.web_automatn.close()
        messagebox.showinfo("browser closed","""The browser window was closed succesfully!
                            Please close the program by clicking the 'x' icon.""")
    

    # def cleandir(self):
    #     if os.path.exists("sampleFile.jpeg"):
    #         os.remove("sampleFile.jpeg")



MyRoot = tk.Tk()
MyWebAutoApp = WebAutomateApp(MyRoot)

MyRoot.mainloop()