import Pyro4
import urllib.request
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, filedialog
from tkinter import *
import io
from PIL import Image
from PIL import ImageTk

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
        self.url_label = tk.Label(self.root, text="Enter URL:")
        self.url_entry = tk.Entry(self.root)
        self.generate_button = tk.Button(self.root, text="Generate QR Code", command=self.generate_qr_code)
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
            qr_code_bytes = self.qr_server.generate_qr_code(url)
            #qr_code_bytes = qr_code_dict['image_bytes']
        except:
            messagebox.showerror("Error", "No se pudo generar el código QR")
            return

         # Convertir los datos de la imagen en un objeto PhotoImage de Tkinter y mostrarla
        #qr_code_bytes = qr_data['image_bytes']
        img = Image.open(io.BytesIO(qr_code_bytes))
        img.show()
        img.save("qr_client.png")


        photo_image = ImageTk.PhotoImage(img)
        self.image_label.configure(self.image_frame,image=photo_image)
        self.image_label.image = photo_image
    '''
    def generate_qr_code(self):
        self.url = self.url_entry.get()
        if not self.url:
            messagebox.showerror("Error", "Por favor introduzca una URL")
            return
        
        #try:
            self.qr_code = self.qr_server.generate_qr_code(self.url)
            
        #except:
            messagebox.showerror("Error", "No se pudo generar el código QR")
            return

         # Convertir los datos de la imagen en un objeto PhotoImage de Tkinter y mostrarla
        #img = PIL.Image.open(io.BytesIO(self.qr_code))
        qr_bytes = self.qr_server.generate_qr_code(self.url)   # solicitamos al servidor que genere el código QR
        qr_image = Image.open(io.BytesIO(qr_bytes))
        qr_photo = ImageTk.PhotoImage(qr_image)

        self.image_label.config(image=qr_photo)
        self.image_label.image = qr_photo
    '''

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
