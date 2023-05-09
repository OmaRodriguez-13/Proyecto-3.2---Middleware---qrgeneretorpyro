# [PROYECTO 3.2: MIDDLEWARE QRGENERETORPYRO]
 
## Instalación

### Source code

Descargar el zip que contiene los archivos fuente del proyecto.

### Vía git 

```bash
git clone https://github.com/OmaRodriguez-13/Proyecto-3.2---Middleware---qrgeneretorpyro
```

## Guía Rápida

### Requerimientos

- Importante: Conexión a la misma red.
- Desactivar Firewall de Windows para evitar cualquier error de conexión.
- MySQL Workbench 8.0 CE.
- Editor de código (por ejemplo: [Visual Studio Code]).
- Python 3.11.2

#### Pyro4
```bash
pip install pyro4
```
#### pyqrcode:
```bash
pip install pyqrcode
```

#### base64:
```bash
pip install base64
```

#### Pillow:
```bash
pip install Pillow
```

### Instrucciones de uso

Cambie la linea 17 del archivo [server.py] por la ip de su equipo "servidor".

[![line17.png](https://i.postimg.cc/y8q3dHgM/line17.png)](https://postimg.cc/ykP8Q2Tj)

Si no conoce su dirección ip de su equipo, puede usar el siguiente comando en cmd.

```bash
ipconfig
```

## Ejecución

### Servidor

Abra un terminal y ejecute [qrgeneretor.py] con alguno de los siguiente comandos:

```bash
py qrgeneretor.py
```

```bash
python qrgeneretor.py
```

El servidor devolverá la URI creada.

[![qrgeneretor.png](https://i.postimg.cc/xTGbFd16/qrgeneretor.png)](https://postimg.cc/Yh99vMgF)

### Cliente

En otra terminal, ejecute [request.py] con alguno de los siguientes comandos:

```bash
py request.py
```

```bash
python request.py
```

En las ventanas siguientes deberá introducir la ip y el puerto del servidor, respectivamente.

[![ip.png](https://i.postimg.cc/cC0dKdGJ/ip.png)](https://postimg.cc/BLYrk96W)

[![port.png](https://i.postimg.cc/bNZBQKYY/port.png)](https://postimg.cc/crNhWk8P)

[![request.png](https://i.postimg.cc/J0kdWk2D/request.png)](https://postimg.cc/303ZXd7Y)

## Testeo

### Servidor [qrgeneretor.py]

Dejar en ejecución el servidor hasta que se desee.


### Cliente [request.py]

[![gui.png](https://i.postimg.cc/7hZtfRhz/gui.png)](https://postimg.cc/5YDSrnw9)

El usuario deberá introducir una URL o cualquier texto (alfanúmerico) que desee para poder generar el código QR que se mostrará en su interfaz.

[![codigo.png](https://i.postimg.cc/90sPCg7C/codigo.png)](https://postimg.cc/wRcRkV2G)

Las imágenes (códigos QR) se irán almacenando en la memoria del equipo cliente.

[![memory.png](https://i.postimg.cc/tR8mXBys/memory.png)](https://postimg.cc/YjfxRfv7)
