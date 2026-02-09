from flask import Flask, render_template, request
from core.services import isi_biodata
from core.constants import biodata

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def biodata_view():
    if request.method == "POST":
        isi_biodata(
            request.form["nama"],
            request.form["tempat_lahir"],
            request.form["tanggal_lahir"],
            request.form["jenis_kelamin"],
            request.form.getlist("hobi")  
        )
        return render_template("biodata.html", biodata=biodata)

    return render_template("biodata.html", biodata={})

if __name__ == "__main__":
    app.run(debug=True)
