#making password checking and (storing ig) utility
import random
from tkinter import *
#making a gui to accept password input and return a better password and rate the current password
import re
import pyperclip #for copying the passwords

class Main(Frame):

    
    def __init__(self, master):
        super().__init__(master)

        #writing for gui
        self.password_entry = StringVar(value = "None")
        self.pwd_len = False
        self.pwd_upperchars = False
        self.pwd_lowerchars = False
        self.pwd_spchars = False
        self.pwd_digits = False

        self.strong = False

        #dataset for the random module to pick
        self.spchar_str = "!@#$%^&*|\?/<>~`.,"
        self.lowerchar_str = "abcdefghijklmnopqrstuvwxyz"
        self.upperchar_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digit_str = "1234567890"

        #GUI elements
        self.label_title = Label(master, text = "PASSWORD CHECKING UTILITY", font = ("Courier", "13", "bold"))
        self.label_title.place(x = 20, y = 10)

        self.label_buffer = Label(master, text = "--------------------------------", font = ("Courier", "13", "bold"))
        self.label_buffer.place(x = 0, y = 30)

        self.label_entry = Label(master, text = "Enter the password here to check :", font = ("Courier", "10", "normal"))
        self.label_entry.place(x = 10, y = 60)

        self.input_entry = Entry(master, textvariable = self.password_entry, width = 40, bd = 1)
        self.input_entry.place(x = 20, y = 80)

        self.input_submit = Button(master, text = "Submit", width = 10, height = 1, bd = 2, relief = "ridge", command = self.call_check_pwd)
        self.input_submit.place(x = 20, y = 110)

        self.about_button = Button(master, text ="About", width = 10, height = 1, bd = 2, relief = "ridge", command = self.about_screen)
        self.about_button.place(x = 110, y = 110)

        self.copy_button = Button(master, text ="Copy", width = 5, height = 1, bd = 2, relief = "ridge", command = self.copy_pass)
        self.copy_button.place(x = 200, y = 110)

        self.logs_display = Text(master, height = 9, width = 30)
        self.logs_display.place(x = 20, y = 140)
        self.logs_display.config(state = "disabled")

    def change_text(self, text):
        self.text = text
        self.logs_display.config(state = "normal")
        self.logs_display.delete("1.0", "end")
        self.logs_display.insert("1.0", self.text)
        self.logs_display.config(state = "disabled")

    def check_password(self, password):
        self.password = self.input_entry.get()
        self.suggested_password = ""
        self.string_list = []
        #print(self.password)

        self.regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        self.pwd_len = False
        self.pwd_upperchars = False
        self.pwd_lowerchars = False
        self.pwd_spchars = False
        self.pwd_digits = False

        self.strong = False

        #verifying the length of pwd
        if len(self.password) >= 8:

            self.pwd_len = True

        if any(c.isdigit() for c in self.password):
            self.pwd_digits = True
        if any(c.islower() for c in self.password):
            self.pwd_lowerchars = True
        if any(c.isupper() for c in self.password):
            self.pwd_upperchars = True
        if self.regex.search(self.password) != None:
            self.pwd_spchars = True
            
        if len(self.password) < 8:
            print("password too short")
            self.change_text(text = "Logs : \nThe Password is\ntoo short.")

        if self.pwd_digits == True and self.pwd_lowerchars == True and self.pwd_upperchars == True and self.pwd_spchars == True and self.pwd_len == True:
            print("Password is strong")
            self.strong = True
            self.change_text(text = "Logs : \nNo change required\nPassword is strong.")
            
        if self.strong == False and self.pwd_len == True:
            print("Improve the password")
            #check for the conditionals of rejection of the password and suggest a good password
            
            if self.pwd_digits == False:
                
                print("No digits in your password, add some !!")
                
                for i in self.password:
                    self.string_list.append(i)
                    
                self.random_number = random.randint(0, len(self.password))
                self.string_list.insert(self.random_number, random.choice(self.digit_str))
                #print(self.string_list)
                self.list_string = ''.join(str(j) for j in self.string_list)
                
                self.suggested_password = self.list_string
                self.string_list.clear()
                print(self.suggested_password)
                self.change_text(text = "Logs : \nNo digits in the password\nSuggested Pwd = \n"+self.suggested_password)
                
            if self.pwd_lowerchars == False:
                
                print("No lowercase letters in your password, add some !!")
                
                for i in self.password:
                    self.string_list.append(i)
                    
                self.random_number = random.randint(0, len(self.password))
                self.string_list.insert(self.random_number, random.choice(self.lowerchar_str))
                #print(self.string_list)
                
                self.list_string = ''.join(str(j) for j in self.string_list)
                
                self.suggested_password = self.list_string
                self.string_list.clear()
                print(self.suggested_password)
                self.change_text(text = "Logs : \nNo lowercase letters in the\npassword\nSuggested Pwd = \n"+self.suggested_password)

                
            if self.pwd_upperchars == False:
                
                print("No Upper case characters in your password, add some !!")
                
                for i in self.password:
                    self.string_list.append(i)
                    
                self.random_number = random.randint(0, len(self.password))
                self.string_list.insert(self.random_number, random.choice(self.upperchar_str))
                #print(self.string_list)
                
                self.list_string = ''.join(str(j) for j in self.string_list)
                
                self.suggested_password = self.list_string
                self.string_list.clear()
                print(self.suggested_password)
                self.change_text(text = "Logs : \nNo uppercase letters in the\npassword\nSuggested Pwd = \n"+self.suggested_password)
              
            if self.pwd_spchars == False:
                
                print("No Special Characters in your password, add some !!")
                
                for i in self.password:
                    self.string_list.append(i)
                    
                self.random_number = random.randint(0, len(self.password))
                self.string_list.insert(self.random_number, random.choice(self.spchar_str))
                #print(self.string_list)
                self.list_string = ''.join(str(j) for j in self.string_list)
                
                self.suggested_password = self.list_string
                self.string_list.clear()
                print(self.suggested_password)                
                self.change_text(text = "Logs : \nNo special characters in the\npassword\nSuggested Pwd = \n"+self.suggested_password)
                
    def call_check_pwd(self):
        self.pwd_check = self.input_entry.get()
        print(self.pwd_check)

        self.check_password(password = self.pwd_check)
        
    def copy_pass(self):
        pyperclip.copy(self.suggested_password)

    def about_screen(self):
        
        self.about = Toplevel(self)
        self.about.geometry("300x300")
        self.about.title("About")
        self.about['bg'] = "white"

        self.about_label_title = Label(self.about, text = "ABOUT THE APP AND CREATOR ",bg = "white", font = ("Courier", "13", "bold"))
        self.about_label_title.place(x = 20, y = 10)

##        self.about_label_context = Label(self.about, text = "The app takes in input from the user and treates it as a password , checking it for the necessary conditions it should meet to be a strong password. It shows a step at a time for easy following of procedures. \n \n The creator of this App is a High-Schooler, Dev Joshi, a computer enthusiast and newbie programmer.",bg = "white", font = ("Courier", "10", "normal"))
##        self.about_label_context.place(x = 20, y = 30)

        self.about_textbox = Text(self.about, height = 20, width = 33)
        self.about_textbox.place(x = 10, y = 40)
        self.about_textbox.insert("1.0", "The app takes in input from the\nuser and treates it as a password\nchecking it for the necessary\nconditions it should meet to be astrong password. Since it is\nreally important in this CyberAgeto create strong passwords. \n \n The creator of this App is Dev\nJoshi a High Schooler,\n       a computer enthusiast , \n       and newbie programmer.")
        self.about_textbox.config(state = "disabled")
              



            
root = Tk()
root.geometry("300x300")
root.title("RazorFast-PasswordChecker-By DevJoshi")
root.resizable(0,0)
App = Main(root)

App.mainloop()
        
