from tkinter import *      # importing libraries 

def encryption(stringtext, n):    # here the stringtext is the sentence of word to be shifted by n times to be encrypted
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #defining capital letters
    lowercase = 'abcdefghijklmnopqrstuvwxyz' #defining small letters 
    
    ips = "" # an empty string to store the sentence <ips means input string>
    
    for i in stringtext: #looping through each string <c is the item or character in the sentence>
        
        if i.isupper(): # for the text being upper
            idx = uppercase.index(i) # finding the index <idx is index number>
            new_idx = (idx + n) % 26 # increasing the index with the shift number
            ips += uppercase[new_idx] #storing it in the ips string 
            
        elif i.islower(): # for the character being in lower case 
            idx = lowercase.index(i) 
            new_idx = (idx + n) % 26
            ips += lowercase[new_idx] 
            
        else:  # if any other character like whitespace or symbol just ass and store to string 
            ips += i
            
    return ips #return the result 
    

def is_valid_shift(shift): # function to check if the shift is right or not 
    return shift.isdigit() # checking if the shift input is a digit 

def on_encrypt():  # the process of the encrypt button 
    stringtext = text1.get()
    shift = shift_entry.get()

    if is_valid_shift(shift): 
        n = int(shift)    # n is the shift value
        ciphertext = encryption(stringtext, n)   #encrypting the text
        print(f"Cipher Text is: {ciphertext}")    # display the output on the terminal 
        result_label.config(text=f"Cipher Text is: {ciphertext}")   # display the output on the the window
        
    else: # for not having n as a digit 
        error_message = "Please enter a valid number for the shift"
        print(error_message)
        result_label.config(text=error_message)

# the gui layout 

window = Tk()
window.title('Encryption')

label1 = Label(window, text=" Hide your message \n Encrypt it so that NOBODY finds out ", fg='black', font=('Algerian',24))
label1.grid(row=0, columnspan=2, pady=30)

l1 = Label(window, text="Enter text:", fg='black', font=('Times New Roman',12))
l1.grid(row=1, column=0, pady=25, padx=50)
text1 = Entry(window, font=('Times New Roman',12))
text1.grid(row=1, column=1)

shift_label = Label(window, text="Enter shift:", fg='black', font=('Times New Roman',12))
shift_label.grid(row=2, column=0, pady=25, padx=50)
shift_entry = Entry(window, font=('Times New Roman',12))
shift_entry.grid(row=2, column=1)

button1 = Button(window, text='Encrypt', fg='white',bg='blue', font=('Arial', 12), command=on_encrypt ,relief='groove')
button1.grid(row=3, column=1, pady=25)

result_label = Label(window, text="", fg='black', font=('Arial', 25))
result_label.grid(row=4, columnspan=2, pady=25)



window.mainloop()
