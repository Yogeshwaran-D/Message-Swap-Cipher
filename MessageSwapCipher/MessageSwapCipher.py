from tkinter import messagebox, simpledialog, Tk

def getEvenLetters(message):
    evenLetters=[]
    for index in range(0,len(message),2):
        evenLetters.append(message[index])
    return evenLetters

def getOddLetters(message):
    oddLetters=[]
    for index in range(1,len(message),2):
        oddLetters.append(message[index])
    return oddLetters

def swapLetters(message):
    swapedLetters=[]
    if len(message)%2 :
        message+='x'
    evenLetters=getEvenLetters(message)
    oddLetters=getOddLetters(message)
    for index in range(0,len(message)//2):
        swapedLetters.append(oddLetters[index])
        swapedLetters.append(evenLetters[index])   
    return "".join(swapedLetters)

def getTask():
    task=simpledialog.askstring("Task","Do you want to encrypt or decrypt ?")
    return task

def getMessage():
    message=simpledialog.askstring("Message","Enter the secret message : ")
    return message

root=Tk()
while True :
    task=getTask().lower()
    if task == "encrypt":
        message=getMessage()
        encrypted=swapLetters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    elif task == "decrypt":
        message=getMessage()
        decrypted=swapLetters(message)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break
root.mainloop()
