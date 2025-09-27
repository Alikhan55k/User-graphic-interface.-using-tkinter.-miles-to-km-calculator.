import tkinter
window = tkinter.Tk()
window.minsize(250, 100)
entry_form = tkinter.Entry(window)
label1=tkinter.Label(window, text="Miles")
label2=tkinter.Label(window, text="is Equal to")
label3=tkinter.Label(window, text="0")
label4=tkinter.Label(window, text="Km")
def calculate():
    entry = entry_form.get()
    entry=int(entry)*1.60934
    label3.configure(text=entry)
button=tkinter.Button(window, text="Calculate", command=calculate)
entry_form.grid(column=1, row=2)
label1.grid(column=2, row=2)
label2.grid(column=0, row=3)
label3.grid(column=1, row=3)
label4.grid(column=2, row=3)
button.grid(column=1, row=4)






window.mainloop()