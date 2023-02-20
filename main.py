from flask import Flask, render_template, request
from resources import menuConf
from resources import cardHeaders
from resources import kii

#https://habr.com/ru/post/432466/

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rel;rweq;rke;lrer'
userRole = "user"

@app.route("/")
@app.route("/user")
def user():
    if userRole == "admin":
        return render_template(
                                "userPage.html",
                                KII = cardHeaders.kii,
                                menu = menuConf.menuAdmin,
                                allDocs = cardHeaders.allDocs,
                                secret = cardHeaders.secret,
                                GISandMIS = cardHeaders.GISandMIS,
                                primaryDocs = cardHeaders.primaryDocs,
                                technicalControl = cardHeaders.technicalControl,
                                personalData = cardHeaders.personalData,
                                bankSecurity = cardHeaders.bankSecurity,
                                govRegulation=cardHeaders.govRegulation
                            )
    else:
        return render_template(
                                "userPage.html",
                                KII = cardHeaders.kii,
                                menu = menuConf.menuUser,
                                allDocs = cardHeaders.allDocs,
                                secret = cardHeaders.secret,
                                GISandMIS = cardHeaders.GISandMIS,
                                primaryDocs = cardHeaders.primaryDocs,
                                technicalControl = cardHeaders.technicalControl,
                                personalData = cardHeaders.personalData,
                                bankSecurity = cardHeaders.bankSecurity,
                                govRegulation = cardHeaders.govRegulation
                            )
@app.route("/hrefs/<arr>")
def hrefs(arr):
    if arr == "kii0":
        arr = kii.kii0
    elif arr == "kii1":
        arr = kii.kii1
    elif arr == "kii2":
        arr = kii.kii2
    return render_template("hrefs.html", menu=menuConf.menuAdmin, colors=menuConf.colors, arr=arr)

@app.route("/login", methods = ["POST", "GET"])
def login():
    global userRole
    if userRole == "admin":
        return user()
    else:
        login = None
        password = None
        state = False
        if request.method == "POST":
            login = request.form["login"]
            password = request.form["password"]
            state = True
        else:
            state = False
        if login == "admin" and password == "admin":
            userRole = "admin"
        if userRole != "admin":
            return render_template("login.html", menu = menuConf.menuUser, name = login, password = password, state = state)
        else:
            return user()

@app.route("/info")
def info():
    return render_template("info.html", menu = menuConf.menuUser)

if __name__ == "__main__":
    app.run(debug = True)
