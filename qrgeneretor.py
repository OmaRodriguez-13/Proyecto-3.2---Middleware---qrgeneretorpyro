import Pyro4
from Pyro4 import socketutil
import pyqrcode
from tkinter import messagebox
from io import BytesIO
import base64

@Pyro4.expose
class QRCodeServer:
    def generate_qr_code(self, url):
        qr = pyqrcode.create(url)
        buffer = BytesIO()
        qr.png(buffer)
        qr_bytes = buffer.getvalue()
        return {'data': base64.b64encode(qr_bytes).decode('ascii'), 'encoding': 'base64'}
    
ip = socketutil.getIpAddress("su_ip") #Cambiar por la ip del equipo servidor
daemon = Pyro4.Daemon(host=ip)

qr_server = QRCodeServer()
uri = daemon.register(qr_server, objectId='qr_server')


messagebox.showinfo("URI del SERVIDOR", f"Servidor listo. URI= {uri}")
print("Servidor listo. URI= ", uri)
daemon.requestLoop()
