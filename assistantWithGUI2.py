'''
Copyright (c) 2021, Matt Michalik
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 
d

'''



from tkinter import *
import wikipedia
import wolframalpha


def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    output.insert(END,myquestion(entered_text))
    
    


#QUESTION TO BE FED INTO TEXT BOX
def myquestion(text):
# personal assistant first attempts to find an answer at Wolfram Wlpha
# if unsuccessful, it then tries Wikipedia.
# if unsuccessful at Wikipedia, it throws an exception.
    try:
            app_id = "X5PGP4-H589RLP945"
            client = wolframalpha.Client(app_id)
            res = client.query(text)
            answer = next(res.results).text
            print ("Answered by Wolfram Alpha")
            return (answer)

    except:     
            try:
                print ("answered by Wikipedia")
                return(wikipedia.summary(text, sentences = 2))
            except Exception as e:
                return (f' Error, exception: {e}')



window = Tk()
window.title("Personal Assistant")
window.configure(background="black")
window.geometry("800x600")


Label(window, text="Enter Question: ", bg="black", fg="white").grid(row=1, column=0, sticky=W)
#text box
textentry = Entry(window, width=20)
textentry.grid(row=2, column=0,sticky=W)

#Submit Button
Button(window, text="Submit", width=6,command=click).grid(row=3, column=0, sticky=W)
Label(window, text="Response: ", bg="black", fg="white").grid(row=4, column=0, sticky=W)

#output text box
output = Text(window, width=75, height=6)
output.grid(row=5,column=0, sticky=W)

#result = myquestion(mytext)


window.mainloop()
