from tkinter import *      # importing libraries 
import clipboard

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
    shift = lbl_value["text"]

    if is_valid_shift(shift): 
        n = int(shift)    # n is the shift value
        ciphertext = encryption(stringtext, n)   #encrypting the text
        print(f"Cipher Text is: {ciphertext}")    # display the output on the terminal 
        result_label.config(text=f"{ciphertext}")   # display the output on the the window
        
        copy_button = Button(window, text="Copy", command=lambda: clipboard.copy(ciphertext))
        copy_button.grid(row=6, column=2, pady=5, sticky='nsew')
        
    else: # for not having n as a digit 
        error_message = "Please enter a valid number for the shift"
        print(error_message)
        result_label.config(text=error_message)
        
# Function to decrease the value
def decrease():
    current_value = int(lbl_value["text"])
    lbl_value["text"] = str(current_value - 1)

# Function to increase the value
def increase():
    current_value = int(lbl_value["text"])
    lbl_value["text"] = str(current_value + 1)

# the gui layout 

window = Tk()
window.title('Encryption')
window.geometry("600x400")

label1 = Label(window, text=" Hide your message ", fg='black', font=('Harlow Solid Italic',25))
label1.grid(row=0, column=1, pady=30)

l1 = Label(window, text="Enter text:", fg='black', font=('Cooper Black',12))
l1.grid(row=1, column=0, pady=25, padx=50)
text1 = Entry(window, font=('Times New Roman',12),bg="green",fg="white",relief='groove',)
text1.grid(row=1, column=1,sticky="e")

shift_label = Label(window, text="Enter shift:", fg='black', font=('Cooper Black',12))
shift_label.grid(row=2, column=0, pady=10, padx=50)

# Create the decrease button
to_decrease = Button(master=window, text="-", command=decrease,bg="green",fg="white",relief='groove')
to_decrease.grid(row=2, column=1,sticky="e" )

# Create the label to display the shift value
lbl_value = Label(master=window, text="0")
lbl_value.grid(row=2, column=2, sticky="w")

# Create the increase button
btn_increase = Button(master=window, text="+", command=increase,bg="green",fg="white",relief='groove')
btn_increase.grid(row=2, column=3 , sticky="e")

button1 = Button(window, text='Encrypt', fg='white',bg='blue', font=('Arial', 12), command=on_encrypt ,relief='groove')
button1.grid(row=3, column=1, pady=5,sticky='nsew')

result_label = Label(window, text="", font=('Elephant',15),bg="black",fg="white")
result_label.grid(row=6, column=1, pady=5, sticky='nsew')

window.grid_columnconfigure(1, weight=0, minsize=50)


window.mainloop()
