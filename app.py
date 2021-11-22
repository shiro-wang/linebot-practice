from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

#表單提交
@app.route('/test/register')
def register():
    return render_template("test/register.html")

#接收表單提交的路由，需要指定methods為POST
@app.route('/result',methods=['POST'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("test/result.html",result=result)

if __name__ == '__main__':
    app.run()