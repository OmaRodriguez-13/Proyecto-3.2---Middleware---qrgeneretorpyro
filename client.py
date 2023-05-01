import Pyro4
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from io import BytesIO
import  base64

server_ip = simpledialog.askstring(
    "Dirección IP del servidor", "Ingrese la dirección IP del servidor:")
if server_ip is None:
    # Si el usuario cancela el diálogo, salir del programa
    exit()

server_port = simpledialog.askstring(
    "Dirección IP del servidor", "Ingrese el puerto del servidor:")
if server_port is None:
    # Si el usuario cancela el diálogo, salir del programa
    exit()
uri = f"PYRO:qr_server@{server_ip}:{server_port}"

messagebox.showinfo("URI del SERVIDOR", uri)
print("URI del SERVIDOR", uri)
qr_server = Pyro4.Proxy(uri)

root = tk.Tk()

def generate_qr():
    url = url_entry.get()
    qr_bytes = qr_server.generate_qr(url)
    print(qr_bytes, type(qr_bytes))

    qr_data = qr_bytes['data']
    qr_encoding = qr_bytes['encoding']

     # Decodificar los datos utilizando la codificación especificada
    if qr_encoding == 'base64':
        qr_data = base64.b64decode(qr_data)

    qr_image = Image.open(BytesIO(qr_data))

    with open("qr_answer.png", "wb") as f:
        qr_image.save(f)
        
    
    photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=photo)
    qr_label.image = photo
    

url_entry = tk.Entry(root)
url_entry.pack()
generate_button = tk.Button(root, text="Generate QR", command=generate_qr)
generate_button.pack()
qr_label = tk.Label(root)
qr_label.pack()




root.mainloop()
