from tkinter import *
import clipboard

#process
def decrypt(m, string_text):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    
    ips = ""
    
    for j in string_text:
        if j in uppercase:
            idx = uppercase.find(j)
            new_idx = (idx - m) % len(uppercase)
            ips += uppercase[new_idx]
        elif j in lowercase:
            idx = lowercase.find(j)
            new_idx = (idx - m) % len(lowercase)
            ips += lowercase[new_idx]
        else:
            ips += j
            
    return ips

#check the  shift number
def is_valid_shift(shift):
    return shift.isdigit()

#-
def decrease():
    current_value = int(lbl_value["text"])
    lbl_value["text"] = str(current_value - 1)

#+
def increase():
    current_value = int(lbl_value["text"])
    lbl_value["text"] = str(current_value + 1)

#result and decrytion button
def decryption():
    string_text = text_entry.get()
    shift = lbl_value["text"]
    
    if is_valid_shift(shift):
        m = int(shift)
        plaintext = decrypt(m, string_text)
        result_label.config(text=f"{plaintext}")
        copy_button = Button(window, text="Copy Result", command=copy_result)
        copy_button.grid(row=5, column=1, pady=10)
        
    else:
        error_label.config(text="Warning! Please enter a positive whole number for shift")


def copy_result():
    clipboard.copy(result_label["text"])

#window
window = Tk()
window.title('Caesar Cipher Decryption')
window.geometry("500x300")
window.configure(bg='orange')

#introduction
label1 = Label(window, text="Decrypt Message", fg='black',bg='orange', font=('Stencil', 25, 'bold'))
label1.grid(row=0, column=1, pady=10)

#string
l1 = Label(window, text="Enter text: ", fg='black', bg='orange', font=('Arial', 12,'bold'))
l1.grid(row=1, column=0, pady=10)
text_entry = Entry(window, font=('Arial', 12), width=40, relief='groove')
text_entry.grid(row=1, column=1)

# Shift number
shift_label = Label(window, text="Shift:", fg='black', bg='orange', font=('Arial', 12,'bold'))
shift_label.grid(row=2, column=0, pady=10)
lbl_value = Label(master=window, text="0", bg='orange', font=('Arial', 12), relief='groove')
lbl_value.grid(row=2, column=1, pady=10)

# decrement
btn_decrease = Button(window, text="-", command=decrease, bg='green', font=('Arial', 12,'bold'), relief='groove')
btn_decrease.grid(row=2, column=1, sticky="e", padx=(0, 70))

# Increment
btn_increase = Button(window, text="+", command=increase, bg='green', font=('Arial', 12,'bold'), relief='groove')
btn_increase.grid(row=2, column=1, sticky="e")

# button
button1 = Button(window, text='Decrypt', fg='white', bg='blue', font=('Arial', 12), command=decryption, relief='raised')
button1.grid(row=3, column=1, pady=10)

# result 
result_label = Label(window, text="", fg='black', bg='orange', font=('Arial', 12))
result_label.grid(row=4, column=1, pady=10)

# Copy
copy_button = Button(window, text="", fg='black', bg='orange', font=('Arial', 12))
copy_button.grid(row=5, column=1, pady=10)

#warning
error_label = Label(window, text="", fg='red', bg='orange',font=('Arial', 10, 'italic'))
error_label.grid(row=5, column=1, pady=5, sticky='nsew')

window.mainloop()
