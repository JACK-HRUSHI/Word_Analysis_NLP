from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import time

window=Tk()
window.geometry("700x350")
window.configure(bg="lightcyan")
window.title("Word Analysis")

def execute():
    global str
    def tense(x):
        t = {
            's': 'simple-present',
            'ing': 'present-continuous',
            'ed': 'simple-past',
            'ies': 'simple-present',
            'iness': 'simple-present'
        }
        tense = t[x]
        return tense

    def category():
        pass

    def lemmatization_morphological_analysis(x, y):
        str = x
        count = y
        list = ['best', 'worst']
        word = {
            'best': 'good',
            'worst': 'bad'
        }
        for i in list:
            if str == i:
                out.insert(END,"\nIt's a type of Lemmatization")
                ok="\nRoot word is " + word[str]
                out.insert(END,ok)
                count = 1

        if count == 0:
            if str == 'stop':
                exit()
            elif len(str) == 1:
                out.insert(END,"\nError...")
                out.insert(END,"\nEntered correct word...")
            else:
                out.insert(END,"\nYou have entered root word only !")
                ok1="\nSo, root word is " + str
                out.insert(END,ok1)
                out.insert(END,"\nEntered word is Singular")
                ok2="\nIt's Tense is " + "simple-present"
                out.insert(END,ok2)
                # out.insert("It\'s Category is ", category())

    def inflectional_morphological_analysis(x, y):
        str = x
        count = y
        # List of suffix
        list = ['ies', 'iness', 'ing', 'ed', 's', 'iance', 'ied', 'ial', 'ize', 'ier', 'iest', 'ily', 'iage', 'iful', 'iment']

        # List of suffixes for Dervational Morphological Analysis
        # dlist = ['iance', 'ied', 'ial', 'ize', 'ier', 'iest', 'ily', 'iage', 'iful', 'iment']

        for i in list:
            length = len(i)
            word = str[0:-length]
            suffix = str.removeprefix(word)

            if suffix == i:
                if i == 'ies' or i == 'iness' or i == 'iance' or i == 'ied' or i == 'ial' or i == 'ize' or i == 'ier' or i == 'iest' or i == 'ily' or i == 'iage' or i == 'iful' or i == 'iment':
                    out.insert(END, "\nIt's a type of Derivational Morphological Analysis")
                    # out.insert("It's a type of Derivational Morphological Analysis")
                    root = str.removesuffix(suffix)
                    root = root + 'y'
                    nok="\nRoot word is " + root
                    out.insert(END,nok)
                    # out.insert("Root word is " + root)
                    count = 1
                    ok3="\nIt's Tense is "+ tense(suffix)
                    out.insert(END,ok3)
                    # out.insert("It\'s Category is ", category())
                    if suffix == 's':
                        out.insert(END,"\nEntered word is Plural")
                    else:
                        out.insert(END,"\nEntered word is Singular")
                    break
                else:
                    out.insert(END, "\nIt's a type of Inflectional Morphological Analysis")
                    # out.insert("It's a type of Inflectional Morphological Analysis")
                    root = str.removesuffix(i)
                    ok4="\nRoot word is " + root
                    out.insert(END,ok4)
                    count = 1
                    ok5="\nIt's Tense is "+ tense(suffix)
                    out.insert(END,ok5)
                    # out.insert("It\'s Category is ", category())
                    if suffix == 's':
                        out.insert(END,"\nEntered word is Plural")
                    else:
                        out.insert(END,"\nEntered word is Singular")

        if count == 0:
            lemmatization_morphological_analysis(str, count)

    def main():
        str= enterword.get()
        #str = input("Enter your word here : ")  # Take input from user
        str = str.lower()
        count = 0
        inflectional_morphological_analysis(str, count)
    # messagebox.showinfo("showinfo", "Successful!")
    out.insert(END,main())

def Clear():
    enterword.delete(0,"end")
    out.delete(1.0,"end")

titlelabel = Label(window,text="Morphological Analysis",font=("Times New Roman",20,"bold","underline"),bg="lightcyan")
titlelabel.place(x=218,y=20)

wordlabel = Label(window,text="Enter your word :",font=("Times New Roman",12,"bold"),bg="lightcyan")
wordlabel.place(x=200,y=75)

enterword=Entry(window,bd=5,width=29)
enterword.place(x=330,y=75)

runBtn=Button(window,text="Run",bd = '4',height= 1, width=18,command = execute)
runBtn.place(x=210,y=115)

clearBtn=Button(window,text="Clear",bd = '4',height= 1, width=18,command = Clear)
clearBtn.place(x=360,y=115)

out=Text(window,bd=5, height = 6, width = 55)
out.place(x=140,y=165)

mainloop()