from flask import Flask, render_template, request
from resources import menuConf
from resources import cardHeaders
from resources import kii
import card

#https://habr.com/ru/post/432466/

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rel;rweq;rke;lrer'
userRole = "user"

@app.route("/")
@app.route("/user")
def user():
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
    global c
    if arr == "ki0":
        card.fillInKII()
        c = card.kiCards[0]
    elif arr == "ki1":
        card.fillInKII()
        c = card.kiCards[1]
    elif arr == "ki2":
        card.fillInKII()
        c = card.kiCards[2]
    elif arr == "ki3":
        card.fillInKII()
        c = card.kiCards[3]
    elif arr == "bs0":
        card.fillInBankSecurity()
        c = card.bsCards[0]
    elif arr == "bs1":
        card.fillInBankSecurity()
        c = card.bsCards[1]
    elif arr == "bs2":
        card.fillInBankSecurity()
        c = card.bsCards[2]
    elif arr == "bs3":
        card.fillInBankSecurity()
        c = card.bsCards[3]
    elif arr == "pd0":
        card.fillInPersonalData()
        c = card.pdCards[0]
    elif arr == "pd1":
        card.fillInPersonalData()
        c = card.pdCards[1]
    elif arr == "pd2":
        card.fillInPersonalData()
        c = card.pdCards[2]
    elif arr == "pd3":
        card.fillInPersonalData()
        c = card.pdCards[3]
    elif arr == "pd4":
        card.fillInPersonalData()
        c = card.pdCards[4]
    elif arr == "pd5":
        card.fillInPersonalData()
        c = card.pdCards[5]
    elif arr == "pd6":
        card.fillInPersonalData()
        c = card.pdCards[6]
    elif arr == "pd7":
        card.fillInPersonalData()
        c = card.pdCards[7]
    elif arr == "pd8":
        card.fillInPersonalData()
        c = card.pdCards[8]
    elif arr == "gr0":
        card.fillInGovRegulation()
        c = card.grCards[0]
    elif arr == "gr1":
        card.fillInGovRegulation()
        c = card.grCards[1]
    elif arr == "gr2":
        card.fillInGovRegulation()
        c = card.grCards[2]
    elif arr == "gr3":
        card.fillInGovRegulation()
        c = card.grCards[3]
    elif arr == "gr4":
        card.fillInGovRegulation()
        c = card.grCards[4]
    elif arr == "gr5":
        card.fillInGovRegulation()
        c = card.grCards[5]
    elif arr == "gr6":
        card.fillInGovRegulation()
        c = card.grCards[6]
    elif arr == "gr7":
        card.fillInGovRegulation()
        c = card.grCards[7]
    elif arr == "s0":
        card.fillInSecret()
        c = card.sCards[0]
    elif arr == "s1":
        card.fillInSecret()
        c = card.sCards[1]
    elif arr == "s2":
        card.fillInSecret()
        c = card.sCards[2]
    elif arr == "s3":
        card.fillInSecret()
        c = card.sCards[3]
    elif arr == "s4":
        card.fillInSecret()
        c = card.sCards[4]
    elif arr == "gd0":
        card.fillInGeneralDocs()
        c = card.gdCards[0]
    elif arr == "gd1":
        card.fillInGeneralDocs()
        c = card.gdCards[1]
    elif arr == "gd2":
        card.fillInGeneralDocs()
        c = card.gdCards[2]
    elif arr == "gam0":
        card.fillInGISandMIS()
        c = card.gamCards[0]
    elif arr == "gam1":
        card.fillInGISandMIS()
        c = card.gamCards[1]
    elif arr == "gam2":
        card.fillInGISandMIS()
        c = card.gamCards[2]
    elif arr == "gam3":
        card.fillInGISandMIS()
        c = card.gamCards[3]
    elif arr == "gam4":
        card.fillInGISandMIS()
        c = card.gamCards[4]
    elif arr == "tc0":
        card.fillInTechnicalControl()
        c = card.tcCards[0]
    elif arr == "tc1":
        card.fillInTechnicalControl()
        c = card.tcCards[1]
    elif arr == "tc2":
        card.fillInTechnicalControl()
        c = card.tcCards[2]
    elif arr == "od0":
        card.fillInOtherDocs()
        c = card.odCards[0]
    elif arr == "od1":
        card.fillInOtherDocs()
        c = card.odCards[1]
    elif arr == "od2":
        card.fillInOtherDocs()
        c = card.odCards[2]
    elif arr == "od3":
        card.fillInOtherDocs()
        c = card.odCards[3]
    elif arr == "od4":
        card.fillInOtherDocs()
        c = card.odCards[4]
    elif arr == "od5":
        card.fillInOtherDocs()
        c = card.odCards[5]
    elif arr == "od6":
        card.fillInOtherDocs()
        c = card.odCards[6]
    elif arr == "od7":
        card.fillInOtherDocs()
        c = card.odCards[7]
    elif arr == "od8":
        card.fillInOtherDocs()
        c = card.odCards[8]
    elif arr == "od9":
        card.fillInOtherDocs()
        c = card.odCards[9]
    return render_template("hrefs.html", menu = menuConf.menuUser, colors = menuConf.colors, card = c)

#возможно потом пригодиться для создания ролей (пользователя и администратора)
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

if __name__ == "__main__":
    app.run(debug = True)
