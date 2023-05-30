# fundamentos de flask 
## creando un entorno virtual
```bash 
virtualenv -p python3 env 
```
## activar el entorno virtual 
en mac
```bash 
source env/bin/activate
```
en windows 
```bash 
.\env\Scripts\activate
```
una vez activado deberia aparecer (env) al inicio el nombre de la ruta de tu terminal. 
## para ver la lista de paquetes que tengo instalado verificar con lo siguiente: 
```bash
pip list
```
## instalando flask 
```bash 
pip install flask
```

## creamos nuestra carpeta y dentro un archivo python

## para depuración 
```py
if __name__ == "__main__":
  app.run(debug=True,port=5000)
```

## correr el proyecto, primero ubicarse dentro de la carpeta app que tiene el archio app.py
```bash 
cd app 
```
seguido
```bash
python3 app.py
```

https://www.youtube.com/watch?v=-1DmVCPB6H8

