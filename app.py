from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/output1",methods=['POST'])
def output():
    if request.method=='POST':
        message1 = request.form['uname']
        message2 = request.form['psw']
    return render_template('output.html',msg=[message1,message2])


if __name__ == '__main__':
    app.run(debug=True)