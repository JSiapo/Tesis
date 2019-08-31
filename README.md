# Automatización del test de Machover

## Alumnos:
-  Baltodano Beltrán, Massiel Estela.
-  Siapo Rodríguez, José Luis O.


Teoria de la aplicación del test aqui.

Teoria de tecnologia usada aqui.

## Requerimientos


``` python
python -m venv venv
source venv/bin/activate #only unix
venv\Scripts\activate #only windows
python -m pip install --upgrade pip #Update pip
pip install -r requirements.txt
```
## Descargar data

``` python
python libs/download.py arg1 arg2
```
**arg1**: link train images

**arg2**: link validation images