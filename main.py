
from flask import Flask, render_template, request
from dati import dabut_rindinas, pierakstit_klat

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/teksts")
def te():
    return render_template("index.html")

@app.route("/saraksts")
def saraksts():
   saraksts = ["toms", "stankveics", "top"]
   bildes = ["https://cdn.motor1.com/images/mgl/7ZmbmJ/s3/audi-rs7-by-abt.jpg", "https://cdn.motor1.com/images/mgl/28Jxk/s1/4x3/fully-loaded-audi-rs7-sportback.webp", "https://media.ed.edmunds-media.com/mercedes-benz/gle-class/2024/oem/2024_mercedes-benz_gle-class_4dr-suv_amg-gle-53_fq_oem_1_815.jpg" ]
   kopejais_saraksts = [] 
   faila_rindas = dabut_rindinas()
   for rindas in faila_rindas:
       elements = rindas.split(", ")
       kopejais_saraksts.append(elements)

    
   return render_template("saraksts.html",vardi = saraksts, bildes = bildes, garums = len(saraksts), visi = kopejais_saraksts) 



@app.route("/info", methods=['POST', 'GET'])
def info():
    if request.method == "POST":
        rinda=""
        nosaukums= request.form["nosaukums"]
        adrese=request.form["adrese"]
        rinda= nosaukums + ", " + adrese
        pierakstit_klat(rinda)
    return render_template ("info.html")
    

if __name__ == '__main__':
    app.run(port = 5000)

print ("sveiki")