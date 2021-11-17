from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/sign-up', methods=['POST'])
def sign_up_user():
    error = 0
    btn = request.form['action']  # определяем какая нажата кнопка
    if btn == 'signUp':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        if password != confirm_password:
            error = 1
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        # В перспективе нужно реализовать проверку пароля на ошибки, а также запись пользователя в Базу данных.
        print(email, username, password, confirm_password, first_name, last_name)
        return render_template(
            'registration.html',
            error=error
        )
    elif btn == 'cancel':
        return render_template(
            'registration.html',
            error=error
        )


@app.route('/')
def hello_world():  # put application's code here
    return render_template(
        'registration.html'
    )


if __name__ == '__main__':
    app.run()
