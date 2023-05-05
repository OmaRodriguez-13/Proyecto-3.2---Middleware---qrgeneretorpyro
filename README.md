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

### Editor de código (por ejemplo: [Visual Studio Code]
#### Python 3.11.2
#### Pyro4:

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

[![server.png](https://i.postimg.cc/0QMJWNVx/server.png)](https://postimg.cc/TLxwhT8H)

### Cliente

En otra terminal, ejecute [request.py] con alguno de los siguientes comandos:

```bash
py request.py
```

```bash
python request.py
```

En las ventanas siguientes deberá introducir la ip y el puerto del servidor, respectivamente.
[![ip.png](https://i.postimg.cc/CK9SJknZ/ip.png)](https://postimg.cc/cK7pLKmZ)
[![port.png](https://i.postimg.cc/rskc2TJM/port.png)](https://postimg.cc/0Mch7LFB)
[![client.png](https://i.postimg.cc/j5TksSGg/client.png)](https://postimg.cc/67Hhct6n)

## Testeo

### Servidor [server.py]

Introducir la palabra secreta "secretword" a adivinar (sin importar mayúsculas y minúsculas), así como la pistas de ayuda al cliente (principal y secundaria).
[![secretword.png](https://i.postimg.cc/RhjNJhwf/secretword.png)](https://postimg.cc/BPBqdqYQ)
[![principal.png](https://i.postimg.cc/dQ7R3yYh/principal.png)](https://postimg.cc/Th65Hhhx)
[![pista.png](https://i.postimg.cc/Vk5zPmMP/pista.png)](https://postimg.cc/DSV9qVBx)


### Cliente [client.py]

