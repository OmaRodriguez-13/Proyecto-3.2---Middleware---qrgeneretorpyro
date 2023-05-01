import Pyro4
import urllib.request
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, filedialog
from tkinter import *
from io import BytesIO
from PIL import Image
from PIL import ImageTk
import base64

class Interfaz:
    def __init__(self, uri):
        self.qr_server = Pyro4.Proxy(uri)

        self.root = tk.Tk()
        self.root.title("QR CODE GENERETOR")
        # self.root.iconbitmap('urna.ico')
        self.root.geometry('390x300')

        # Hacer que la ventana no sea redimensionable
        self.root.resizable(False, False)

        # Crear entrada de URL y botón para generar el código QR
        self.url_label = tk.Label(self.root, text="Introduce la URL:")
        self.url_entry = tk.Entry(self.root)

        self.url_entry.focus_set()
        self.generate_button = tk.Button(self.root, text="Generar Código QR", command=self.generate_qr_code)
        self.url_label.pack()
        self.url_entry.pack(fill=tk.X, padx=5)
        self.generate_button.pack(pady=5)

        # Crear y empaquetar el contenedor de imagen
        self.image_frame = tk.Frame(self.root)
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()
        self.image_frame.pack(pady=5)

    # Método para generar el código QR
    def generate_qr_code(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Por favor introduzca una URL")
            return
        
        try:
            # Obtener los bytes del código QR del servidor
            qr_bytes = self.qr_server.generate_qr_code(url)
        except:
            messagebox.showerror("Error", "No se pudo generar el código QR")
            return

         # Convertir los datos de la imagen en un objeto PhotoImage de Tkinter y mostrarla
        print(qr_bytes, type(qr_bytes))

        qr_data = qr_bytes['data']
        qr_encoding = qr_bytes['encoding']

        # Decodificar los datos utilizando la codificación especificada
        if qr_encoding == 'base64':
            qr_data = base64.b64decode(qr_data)
        # Abrir la imagen utilizando los datos decodificados
        img = Image.open(BytesIO(qr_data))

        # Redimensionar la imagen a 200x200 píxeles
        img = img.resize((200, 200))

        # Guardar la imagen en el sistema del cliente
        with open(f"qr_client_{url}.png", "wb") as f:
            img.save(f)    

        #Mostrar la imagen en el label
        photo_image = ImageTk.PhotoImage(img)
        self.image_label.config(image=photo_image)
        self.image_label.image = photo_image
   
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

if __name__ == "__main__":
    interfaz = Interfaz(uri)
    interfaz.root.mainloop()
