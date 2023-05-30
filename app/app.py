from flask import Flask, render_template
app = Flask(__name__)

# para rutas
@app.route('/')
def index():
  cursos = ['php', 'ruby', 'java', 'c++', 'js']
  data = {
    'titulo':'Aprendiendo Flask',
    'bienvenido': 'Saludos!',
    'cursos': cursos,
    'numero_cursos': len(cursos)
    
  }
  return render_template('index.html', data=data)
  

if __name__ == "__main__":
  app.run(debug=True,port=5000)