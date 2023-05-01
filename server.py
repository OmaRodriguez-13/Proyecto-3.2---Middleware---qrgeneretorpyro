import Pyro4
import pyqrcode
from io import BytesIO
import base64

@Pyro4.expose
class QRServer(object):
    @staticmethod
    def generate_qr(url):
        qr = pyqrcode.create(url)
        buffer = BytesIO()
        qr.png(buffer)
        qr_bytes = buffer.getvalue()
        return {'data': base64.b64encode(qr_bytes).decode('ascii'), 'encoding': 'base64'}



ip = Pyro4.socketutil.getInterfaceAddress("192.168.1.101")
daemon = Pyro4.Daemon(host=ip)

qr_server = QRServer()
uri = daemon.register(qr_server, objectId='qr_server')


#messagebox.showinfo("URI del SERVIDOR", f"Servidor listo. URI= {uri}")
print("Servidor listo. URI= ", uri)
daemon.requestLoop()