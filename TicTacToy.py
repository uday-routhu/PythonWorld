'''
Created on Dec 20, 2016

@author: uday
'''
from Tkinter import *
from tkMessageBox import *

class TicTacToy(object):
    '''
    classdocs
    '''
    
    def __init__(self, master):
        master.title('tic tac toe')
        self.button1 = Button(master,text = "1",width = 5,command = self.one_num)
        self.button1.grid(row = 1,column = 0)
        self.button2 = Button(master,text = "2",width = 5,command = self.two_num)
        self.button2.grid(row = 1,column = 1)
        self.button3 = Button(master,text = "3",width = 5,command = self.three_num)
        self.button3.grid(row = 1,column = 2)
        self.button4 = Button(master,text = "4",width = 5,command = self.four_num)
        self.button4.grid(row = 2,column = 0)
        self.button5 = Button(master,text = "5",width = 5,command = self.five_num)
        self.button5.grid(row = 2,column = 1)
        self.button6 = Button(master,text = "6",width = 5,command = self.six_num)
        self.button6.grid(row = 2,column = 2)
        self.button7 = Button(master,text = "7",width = 5,command = self.seven_num)
        self.button7.grid(row = 3,column = 0)
        self.button8 = Button(master,text = "8",width = 5,command = self.eight_num)
        self.button8.grid(row = 3,column = 1)
        self.button9 = Button(master,text = "9",width = 5,command = self.nine_num)
        self.button9.grid(row = 3,column = 2)
    
    def one_num(self):
        var = 1
        who = raw_input("Please enter who is clicking now x or y:")
        if who in ('x','X'):
            user_one.insert(len(user_one),var)
            self.button1.configure(bg = "red")
            if len(user_one) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button1.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0)   
            
        
    def two_num(self):
        who = raw_input("Please enter who is clicking now x or y:")
        var = 2
        if who in ('x','X'):
            self.button2.configure(bg = "red")
            user_one.insert(len(user_one),var)
            if len(user_one) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button2.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0)   
            
    def three_num(self):
        who = raw_input("Please enter who is clicking now x or y:")
        var = 3
        if who in ('x','X'):
            self.button3.configure(bg = "red")
            user_one.insert(len(user_one),var)
            if len(user_one) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button3.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0)   
            
        
    def four_num(self):
        who = raw_input("Please enter who is clicking now x or y:")
        var = 4
        if who in ('x','X'):
            self.button4.configure(bg = "red")
            user_one.insert(len(user_one),var)
            if len(user_one) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button4.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0) 
        
    def five_num(self):
        who = raw_input("Please enter you is clicking now x or y:")
        var = 5
        if who in ('x','X'):
            self.button5.configure(bg = "red")
            user_one.insert(len(user_one),var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button5.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0) 
    
    def six_num(self):
        who = raw_input("Please enter who is clicking now x or y:")
        var = 6
        if who in ('x','X'):
            self.button6.configure(bg = "red")
            user_one.insert(len(user_one),var)
            if len(user_one) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button6.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0) 
        
    def seven_num(self):
        who = raw_input("Please enter who is clicking now x or y:")
        var = 7
        if who in ('x','X'):
            self.button7.configure(bg = "red")
            user_one.insert(len(user_one),var)
            if len(user_one) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button7.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0) 
    
    def eight_num(self):
        who = raw_input("Please enter who is clicking now x or y:")
        var = 8
        if who in ('x','X'):
            self.button8.configure(bg = "red")
            user_one.insert(len(user_one),var)
            if len(user_one) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button8.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0) 
        
    def nine_num(self):
        who = raw_input("Please enter who is clicking now x or y:")
        var = 9
        if who in ('x','X'):
            self.button9.configure(bg = "red")
            user_one.insert(len(user_one),var)
            if len(user_one) == 3:
                winning_user(self)
            else:
                pass
        elif who in ('y','Y'):
            self.button9.configure(bg = "blue")
            user_two.insert(len(user_two), var)
            if len(user_two) == 3:
                winning_user(self)
            else:
                pass
        else:
            exit(0) 
        
    
    def clear_dashboard(self,winning_user):
        if winning_user == "X" | winning_user == "Y":
            print ("Clear the dash board ")
        else:
            print ("restart the game")
            
    
#@staticmethod     
def winning_user(self):
    winng_chances = ([1,2,3],[3,2,1],[1,4,7],[7,4,1],[3,6,9],[9,6,3],[1,5,9],[9,5,1],[3,5,7],[7,5,3],[7,8,9],[9,8,7])
    if user_one in winng_chances:
        answer("X won the game")
        exit(0)
    elif user_two in winng_chances:
        answer("Y won the game")
        exit(0)
    #elif user_one not in winng_chances and user_two not in winng_chances:
    #    pass
    else:
        answer("draw the match")

def answer(val):
        showinfo("Result"," "+ val )
        
#Main Methos 
root = Tk()
user_one = []
user_two = []
obj = TicTacToy(root)
Button(text='Answer', command=answer)
root.mainloop()
