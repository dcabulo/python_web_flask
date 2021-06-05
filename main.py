from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def before_request():
    print("Antes de la peticion")


@app.after_request
def after_request(response):
    print("Despues de peticion")
    return response

@app.route('/')
def index():
    name = "Diego Cabulo"
    is_premium = False
    courses = ['python', 'ruby', 'java', 'javascript']
    return render_template('index.html', user_name=name, is_premium=is_premium, courses=courses)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<user_name>/<last_name>')  #String
def user(user_name, last_name):
    return 'Hola {} {}'.format(user_name, last_name)


@app.route('/datos')
def datos():
    nombre = request.args.get('nombre', '') #dictionary
    return 'Listado de datos => {}'.format(nombre)


if __name__ == '__main__':
    app.run(debug=True, port=9000)

