from tkinter import *
import clipboard

def encryption(stringtext, n):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    
    ips = ""
    
    for i in stringtext:
        if i.isupper():
            idx = uppercase.index(i)
            new_idx = (idx + n) % 26
            ips += uppercase[new_idx]
        elif i.islower():
            idx = lowercase.index(i)
            new_idx = (idx + n) % 26
            ips += lowercase[new_idx]
        else:
            ips += i
            
    return ips

def is_valid_shift(shift):
    return shift.isdigit()

def on_encrypt():
    stringtext = text1.get()
    shift = lbl_value["text"]

    if is_valid_shift(shift):
        n = int(shift)
        ciphertext = encryption(stringtext, n)
        result_label.config(text=f"{ciphertext}")
        
        # Ensure the copy button appears only after encryption
        copy_button = Button(window, text="Copy Result", command=copy_result)
        copy_button.grid(row=5, column=1, pady=10)
    else:
        error_label.config(text="Please enter a valid shift (positive and Whole number).")

def decrease():
    current_value = int(lbl_value["text"])
    lbl_value["text"] = str(current_value - 1)

def increase():
    current_value = int(lbl_value["text"])
    lbl_value["text"] = str(current_value + 1)

# Copy the result
def copy_result():
    clipboard.copy(result_label["text"])

#window
window = Tk()
window.title('Caesar Cipher Encryption')
window.geometry("500x300")
window.configure(bg='yellow')

#1st line
label1 = Label(window, text="Encrypt Message", fg='black',bg='yellow', font=('Stencil', 25, 'bold'))
label1.grid(row=0, column=1, pady=10)

#string entry
l1 = Label(window, text="Enter text: ", fg='black',bg='yellow', font=('Arial', 12,'bold'))
l1.grid(row=1, column=0, pady=10)
text1 = Entry(window, font=('Arial', 12), width=40, relief='groove')
text1.grid(row=1, column=1)

#shift number
shift_label = Label(window, text="Shift:", fg='black',bg='yellow', font=('Arial', 12,'bold'))
shift_label.grid(row=2, column=0, pady=10)
lbl_value = Label(master=window, text="0", bg='yellow',font=('Arial', 12), relief='groove')
lbl_value.grid(row=2, column=1, pady=10)

#decrement
btn_decrease = Button(window, text="-",bg="green" ,command=decrease, font=('Arial', 12,'bold'))
btn_decrease.grid(row=2, column=1, sticky="e", padx=(0, 70))

#increment
btn_increase = Button(window, text="+", bg="green" ,command=increase, font=('Arial', 12,'bold'))
btn_increase.grid(row=2, column=1, sticky="e")

#button
button1 = Button(window, text='Encrypt', fg='light blue', bg='blue', font=('Arial', 12), command=on_encrypt, relief='raised')
button1.grid(row=3, column=1, pady=10)

#result
result_label = Label(window, text="", fg='black',bg='yellow', font=('Arial', 12))
result_label.grid(row=4, column=1, pady=10)

#error label
error_label = Label(window, text="", fg='red', bg='yellow',font=('Arial', 10, 'italic'))
error_label.grid(row=5, column=1, pady=5, sticky='nsew')



window.mainloop()
