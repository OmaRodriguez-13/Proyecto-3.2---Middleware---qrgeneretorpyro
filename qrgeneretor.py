import Pyro4
import qrcode
from tkinter import messagebox
from PIL import ImageTk

@Pyro4.expose
class QRCodeServer:
    def generate_qr_code(self, url):
        img = qrcode.make(url)
        img.save("qr.png")
        with open("qr.png", "rb") as f:
            qr_code_bytes = f.read()
        return qr_code_bytes
    '''
    def generate_qr_code(self, url):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=url)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr.png")
        with open("qr.png", "rb") as f:
            qr_code = f.read()
            return qr_code
    '''
ip = Pyro4.socketutil.getInterfaceAddress("192.168.43.187")
daemon = Pyro4.Daemon(host=ip)

qr_server = QRCodeServer()
uri = daemon.register(qr_server, objectId='qr_server')


messagebox.showinfo("URI del SERVIDOR", f"Servidor listo. URI= {uri}")
print("Servidor listo. URI= ", uri)
daemon.requestLoop()
