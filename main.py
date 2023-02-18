from flask import Flask, render_template, url_for, request, flash

path = "this"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'rel;rweq;rke;lrer'
menu = [
    {'name': 'User page', 'href': '/'},
    {'name': 'Info', 'href': '/info'},
    {'name': 'Feedback', 'href': '/feedback'},
    {'name': 'Go to admin', 'href': '/login'}
]
kii = [
    {"name": "Основные документы", "href": "https://getbootstrap.com/docs/5.1/utilities/opacity/"},
    {"name": "Связь             ", "href": ".html"},
    {"name": "Госсопка          ", "href": ".html"}
]
bankSecurity =[
    {"name": "               Стандарты банка РФ", "href": ".html"},
    {"name": "Криптография                     ", "href": ".html"},
    {"name": "ГОСТы по безопасности            ", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"}
]
personalData =[
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"},
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"}
]
technicalControl =[
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"},
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"}
]
primaryDocs =[
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"}
]
GISandMIS =[
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"},
    {"name": "Основные документы", "href": ".html"}
]
secret =[
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"},
    {"name": "Основные документы", "href": ".html"}
]
allDocs =[
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"},
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"},
    {"name": "Основные документы", "href": ".html"},
    {"name": "Обеспечение безопасности", "href": ".html"},
    {"name": "Блокировка нарушителей", "href": ".html"},
    {"name": "Нормативно-правовые акты банка РФ", "href": ".html"}
]
@app.route("/")
@app.route("/user")
def user():
    return render_template(
                            "userPage.html",
                            KII = kii,
                            menu = menu,
                            allDocs = allDocs,
                            secret = secret,
                            GISandMIS = GISandMIS,
                            primaryDocs = primaryDocs,
                            technicalControl = technicalControl,
                            personalData = personalData,
                            bankSecurity = bankSecurity
                        )

@app.route("/info")
def info():
    return render_template("info.html", menu = menu)

@app.route("/login")
def login():
    return render_template("login.html", menu = menu)

@app.route("/feedback", methods = ["POST", "GET"])
def feedback():
    username = None
    number = None
    if request.method == 'POST':
        username = request.form['username']
        number = request.form['number']
        flash(f'name: {username}, number: {number}')
    return render_template("feedback.html", menu = menu, name = username, number = number)

"""
    для отладки можно создавать тестовый контекст без запуска сервера
"""
'''
with app.test_request_context():
    print(url_for('info'))
'''

if __name__ == "__main__":
    app.run(debug = True)
