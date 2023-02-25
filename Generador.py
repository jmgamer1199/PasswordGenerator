import tkinter as tk
import random
import string

def generate_password():

  password_length = random.randint(8, 12)

  #simbolos = ',.-;:_´ç¨Ç`+^*¡ºª\!"·$%&/()=?¿[]{}'
  
  password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))

  password_text.delete(1.0, tk.END)
  password_text.insert(1.0, password)

root = tk.Tk()
root.title("Generador de contraseñas")
root.geometry("300x100")

password_text = tk.Text(root, width=20, height=1, font=("Helvetica", 14), bg="#FFFFFF", fg="#000000")
password_text.place(x=10, y=10)

generate_button = tk.Button(root, text="Generar contraseña", command=generate_password, font=("Helvetica", 14), bg="#00BFFF", fg="#FFFFFF", relief=tk.GROOVE, activebackground="#000080", activeforeground="#FFFFFF")
generate_button.place(x=10, y=40)

root.mainloop()