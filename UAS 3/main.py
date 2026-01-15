from flask import Flask, render_template, request, redirect
from parkir import Parkir

app = Flask(__name__)
parkir = Parkir()

@app.route("/", methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        p = request.form["pilihan"]

        if p == "1":
            return render_template("masuk.html")

        elif p == "2":
            return redirect("/keluar")

        elif p == "3":
            return render_template(
                "parkir.html",
                data=parkir.aktif()
            )

        elif p == "4":
            return render_template(
                "pendapatan.html",
                motor=parkir.pendapatan_motor,
                mobil=parkir.pendapatan_mobil
            )

        elif p == "5":
            return redirect("/analisis")

        elif p == "6":
            return "<pre>Program selesai</pre>"

    return render_template("menu.html")

@app.route("/proses-masuk", methods=["POST"])
def proses_masuk():
    data = parkir.masuk(
        request.form["plat"],
        request.form["jenis"],
        request.form["merek"]
    )
    return render_template("masuk.html", data=data)

@app.route("/keluar")
def keluar():
    if len(parkir.aktif()) == 0:
        return render_template("keluar.html", status="kosong")

    return render_template("keluar.html", status="siap")

@app.route("/proses-keluar", methods=["POST"])
def proses_keluar():
    plat = request.form["plat"]
    data = parkir.keluar(plat)

    if data is None:
        if len(parkir.aktif()) == 0:
            return render_template("keluar.html", status="kosong")

        return render_template("keluar.html", status="tidak_ditemukan")

    return render_template("keluar.html", status="berhasil", data=data)

@app.route("/analisis")
def analisis():
    data = parkir.analisis()
    return render_template("analisis.html", data=data)


app.run(debug=True)
