import tkinter as tk

# Decryption function
def decrypt(m, string_text):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    ips2 = ""
    
    for j in string_text:
        if j in idx2:
            idx2 = upper_case.find(j)
            new_idx2 = (idx2 - m) % len(upper_case)
            ips2 += upper_case[new_idx2]
            
        elif j in lower_case:
            idx2 = lower_case.find(j)
            new_idx2 = (idx2 - m) % len(lower_case)
            ips2 += lower_case[new_idx2]
            
        else:
            ips2 += j
    return ips2


# process of shift number
def is_valid_shift(shift):
    return shift.isdigit()

# process of the button 
def decryption():
    string_text = text_entry.get()  
    shift = shift_entry.get() 
    
    if is_valid_shift(shift):  
        m = int(shift)  
        plaintext = decrypt(m, string_text)  
        result_label.config(text=f"Plain Text is: {plaintext}")  
        
    else:  
        error_message = "Please enter a valid number for the shift"  
        result_label.config(text=error_message)  

# the window
window = tk.Tk()
window.title('Decryption')

# label
label1 = tk.Label(window, text="Decrypt your text", fg='black', font=('Times New Roman', 18))
label1.grid(row=0, columnspan=2, pady=25)

#string entry
l1 = tk.Label(window, text="Enter text:", fg='black', font=('Times New Roman', 12))
l1.grid(row=1, column=0, pady=25, padx=50)
text_entry = tk.Entry(window, font=('Times New Roman', 12))
text_entry.grid(row=1, column=1)

#shift number entry
shift_label = tk.Label(window, text="Enter shift:", fg='black', font=('Times New Roman', 12))
shift_label.grid(row=2, column=0, pady=25, padx=50)
shift_entry = tk.Entry(window, font=('Times New Roman', 12))
shift_entry.grid(row=2, column=1)

# button 
button1 = tk.Button(window, text='Decrypt', fg='blue', font=('Times New Roman', 12), command=decryption, relief='raised')
button1.grid(row=3, column=1, pady=25)

#Result
result_label = tk.Label(window, text="", fg='black', font=('Arial', 12))
result_label.grid(row=4, columnspan=2, pady=25)

# Run the main loop
window.mainloop()
