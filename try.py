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
        result_label.config(text=f"Cipher Text: {ciphertext}")
        
        copy_button = Button(window, text="Copy", command=lambda: clipboard.copy(ciphertext))
        copy_button.grid(row=3, column=2, pady=5, sticky='nsew')
    else:
        error_label.config(text="Please enter a valid shift (a number).")

def decrease():
    current_value = int(lbl_value["text"])
    lbl_value["text"] = str(current_value - 1)

def increase():
    current_value = int(lbl_value["text"])
    lbl_value["text"] = str(current_value + 1)

window = Tk()
window.title('Caesar Cipher Encryption')
window.geometry("600x250")

label1 = Label(window, text="Encrypt Your Message", fg='black', font=('Arial', 18, 'bold'))
label1.grid(row=0, column=1, pady=10)

l1 = Label(window, text="Enter text:", fg='black', font=('Arial', 12))
l1.grid(row=1, column=0, pady=10)
text1 = Entry(window, font=('Arial', 12), width=40, relief='groove')
text1.grid(row=1, column=1)

shift_label = Label(window, text="Enter shift:", fg='black', font=('Arial', 12))
shift_label.grid(row=2, column=0, pady=10)
lbl_value = Label(master=window, text="0", font=('Arial', 12), width=5, relief='groove')
lbl_value.grid(row=2, column=1, sticky="w")

btn_decrease = Button(master=window, text="-", command=decrease, width=5, relief='groove')
btn_decrease.grid(row=2, column=1, sticky="e")

btn_increase = Button(master=window, text="+", command=increase, width=5, relief='groove')
btn_increase.grid(row=2, column=1, sticky="e", padx=(0, 70))

button1 = Button(window, text='Encrypt', fg='white', bg='blue', font=('Arial', 12), command=on_encrypt, relief='groove')
button1.grid(row=3, column=0, pady=10, sticky='nsew')

result_label = Label(window, text="", font=('Arial', 12), width=40, relief='groove')
result_label.grid(row=3, column=1, pady=10, sticky='nsew')

error_label = Label(window, text="", fg='red', font=('Arial', 10, 'italic'))
error_label.grid(row=4, column=1, pady=5, sticky='nsew')

window.mainloop()
