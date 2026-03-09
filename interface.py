
from email.mime import message
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from LFSR_Encryption import LFSR_encryption
from LFSR_Decryption import LFSR_decryption

is_enhancement = False
is_baseline = False

def decryption_function():
    global is_baseline, is_enhancement
    if is_baseline:
        print("Baseline decryption selected")
        with open(r"C:\Users\LTC\Desktop\FileProject\encryption_project2\encrypted_baseline.txt", "r", encoding="utf-8") as file:
            content = file.read()
        seed = content[0]
        ciphertext = content[1:] 
        decryptor = LFSR_decryption(seed, ciphertext, type="baseline")
        message = decryptor.decryption_message()
    else:
        print("Enhancement decryption selected")
        with open(r"C:\Users\LTC\Desktop\FileProject\encryption_project2\encrypted_enhancement.txt", "r", encoding="utf-8") as file:
            content = file.read()
        seed = content[0]
        ciphertext = content[1:]
        decryptor = LFSR_decryption(seed, ciphertext, type="enhancement")
        message = decryptor.decryption_message()
    entry_secretMsg_decryption.config(state="normal")
    entry_secretMsg_decryption.delete(0, tk.END)
    entry_secretMsg_decryption.insert(0, message)
    entry_secretMsg_decryption.config(state="readonly")
    print("Seed:", seed)
    print("Ciphertext:", ciphertext)
    print("Decrypted message:", message)
    return

def encryption_function():
    global is_baseline, is_enhancement
    message = entry_Msg_encryption.get()
    if is_baseline:
        print("Baseline encryption selected")
        print("Message to encrypt:", message)
        encryptor = LFSR_encryption(message, type="baseline")
        encryptor.encryption_message()
    else:
        print("Enhancement encryption selected")
        print("Message to encrypt:", message)
        encryptor = LFSR_encryption(message, type="enhancement")
        encryptor.encryption_message()
    return

def selected_type(type):
    global is_baseline, is_enhancement
    entry_secretMsg_decryption.config(state="normal")
    entry_secretMsg_decryption.delete(0, tk.END)
    entry_secretMsg_decryption.config(state="readonly")
    entry_Msg_encryption.delete(0, tk.END)
    if type == "enhancement":
        is_baseline = False
        is_enhancement = True   
    else:
        is_baseline = True
        is_enhancement = False
    return

def show_frame(frame, type=None):
    if type is not None:
        selected_type(type)
    frame.tkraise()

root = tk.Tk()
root.title("My First GUI")

bg_image = Image.open("C:\\Users\\LTC\\Desktop\\FileProject\\encryption_project1\\background.jpg")
bg_image = bg_image.resize((700, 500), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

home_frame = tk.Frame(root)
seconde_frame = tk.Frame(root)
encryption_frame = tk.Frame(root)
decryption_frame = tk.Frame(root)
for frame in (home_frame, seconde_frame, encryption_frame, decryption_frame):
    background_label = tk.Label(frame, image=bg_photo)
    background_label.image = bg_photo 
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    frame.place(x=0, y=0, relwidth=1, relheight=1)

# Home Frame
btn_baseline_frame = tk.Button(home_frame, text="Baseline Stream Cipher Implementation", bg="lightblue", fg="black", activebackground="#4682B4",
    font=("Arial", 16, "bold"), width=32, height=1, command=lambda: show_frame(seconde_frame, type="baseline"))
btn_baseline_frame.place(x=250, y=190)

btn_enhancements_frame = tk.Button(home_frame, text="Proposed Enhancements", bg="lightblue", fg="black", activebackground="#4682B4", 
    font=("Arial", 16, "bold"), width=32, height=1, command=lambda: show_frame(seconde_frame, type="enhancement"))
btn_enhancements_frame.place(x=250, y=240)

# Seconde Frame
btn_home_frame_Seconde = tk.Button(seconde_frame, text="Back to Home", bg="lightblue", fg="black", activebackground="#4682B4",
    font=("Arial", 8, "bold"), width=10, height=1, command=lambda: show_frame(home_frame))
btn_home_frame_Seconde.place(x=20, y=20)

btn_encryption_frame = tk.Button(seconde_frame, text="Encryption", bg="lightblue", fg="black", activebackground="#4682B4",
    font=("Arial", 16, "bold"), width=20, height=1, command=lambda: show_frame(encryption_frame))
btn_encryption_frame.place(x=370, y=190)

btn_decryption_frame = tk.Button(seconde_frame, text="Decryption", bg="lightblue", fg="black", activebackground="#4682B4", 
    font=("Arial", 16, "bold"), width=20, height=1, command=lambda: show_frame(decryption_frame))
btn_decryption_frame.place(x=370, y=240)

# Baseline & Enhancements - Encryption
btn_home_frame_emb = tk.Button(encryption_frame, text="Back", bg="lightblue", fg="black", activebackground="#4682B4",
    font=("Arial", 8, "bold"), width=10, height=1, command=lambda: show_frame(seconde_frame))
btn_home_frame_emb.place(x=20, y=20)

label_Msg_encryption = tk.Label(encryption_frame, text="Message:", bg="lightblue", fg="black", font=("Arial", 12, "bold"), width=22)
label_Msg_encryption.place(x=400, y=170)
entry_Msg_encryption = tk.Entry(encryption_frame, bg="lightblue", fg="black", font=("Arial", 11), width=28)
entry_Msg_encryption.place(x=400, y=200)

button_chooseFile_encryption = tk.Button(encryption_frame, text="encryption", bg="lightblue", fg="black", activebackground="#4682B4",
    font=("Arial", 15, "bold"), width=18, height=1, command=lambda: encryption_function())
button_chooseFile_encryption.place(x=400, y=290)

# Baseline & Enhancements - Decryption
btn_home_frame_decryption = tk.Button(decryption_frame, text="Back", bg="lightblue", fg="black", activebackground="#4682B4",
    font=("Arial", 8, "bold"), width=10, height=1, command=lambda: show_frame(seconde_frame))
btn_home_frame_decryption.place(x=20, y=20)

button_chooseFile_decryption = tk.Button(decryption_frame, text="Decrypt", bg="lightblue", fg="black", activebackground="#4682B4",
    font=("Arial", 15, "bold"), width=18, height=1, command=lambda: decryption_function())
button_chooseFile_decryption.place(x=400, y=170)

label_secretMsg_decryption = tk.Label(decryption_frame, text="Plaintext:", bg="lightblue", fg="black", font=("Arial", 12, "bold"), width=22)
label_secretMsg_decryption.place(x=400, y=280)
entry_secretMsg_decryption = tk.Entry(decryption_frame, bg="lightblue", fg="black", font=("Arial", 11), width=28)
entry_secretMsg_decryption.place(x=400, y=310)

show_frame(home_frame)
root.geometry("700x500")
root.mainloop()