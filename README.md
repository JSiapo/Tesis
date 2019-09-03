# Automatización del test de Machover

## Alumnos:
-  Baltodano Beltrán, Massiel Estela.
-  Siapo Rodríguez, José Luis O.


Teoria de la aplicación del test [aqui](https://gitlab.com/JSiapo/tesis/raw/develop/Tesis/Informe/Tesis.pdf).

Teoria de tecnologia usada aqui.

## Requerimientos

### Linux
``` python
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip #Update pip
pip install -r requirements.txt
```

### Windows

``` python
pip install virtualenv
virtualenv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip #Update pip
pip install -r requirements.txt
```

## Descargar data

``` python
python libs/download.py arg1 arg2
```
**arg1**: link train images

**arg2**: link validation images

## Ejecutar Jupyter notebook

``` bash
jupyter notebook
```

Para abrir notebooks de carpeta analytics

## Ejecutar LablelImg

``` bash
labelImg
```