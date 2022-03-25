from flask import Flask, url_for, redirect, render_template, request,jsonify
import pyodbc




app = Flask(__name__, template_folder='static')

@app.route("/index")
def home():
  return render_template("index.html")
@app.route("/login" , methods=["POST","GET"])
def checklogin():
  connection = pyodbc.connect('Driver={SQL Server};' 'Server=QENI\FG;' 'Database=Consulting;' 'Trusted_connection=yes;')
  cursor = connection.cursor()
  if request.method=="POST":
   Usr = request.form['nm']
   pasw = request.form['psw']
   cursor.execute('select *From LoginC where Username=? and password=?', (Usr, pasw))
   rows=cursor.fetchall()
   if(len(rows)>=1):
       data=cursor.execute('select *From PersonalityInformation where UserName=?', Usr)
       return render_template("table.html", data=data)

   else:
    return render_template("login.html")
  return render_template("BasLogin.html")
@app.route("/insert" ,methods=["POST","GET"])
def insert():
    if request.method=="POST":
        insert = request.form['checkboxvalue']
        print(insert)
        msg ='Data Inserted Successfully'
    else:
         msg = 'Invalid'
    return jsonify(msg)
@app.route("/create")
def regi():
    return render_template("table.html")

@app.route("/login2",methods=["POST","GET"])
def login2():
   if request.method =="POST":
       Usr = request.form['nm']
       if Usr == "admin":
           return render_template("table.html")
    
       else:
        return render_template("BasLogin.html")

   return render_template("BasLogin.html")
@app.route('/<gm>')
def game(gm):
    return f"<h1>{gm}<h1>"

if __name__=="__main__":
 app.run(debug=True)
