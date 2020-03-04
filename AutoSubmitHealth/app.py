from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from forms import SubmitForm
from addUserToDb import addUser
from autoSubmit import autoSubmit
import warnings

# 这里忽略一些告警输出，例如忽略ssl和对数据库操作时
warnings.filterwarnings("ignore")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = SubmitForm(request.form)
    if request.method == 'POST' and form.validate():
        userDict = {
            'username' : form.username.data,
            'password' : form.password.data,
            'site' : form.site.data,
            'phone' : form.phone.data,
        }
        addUser(userDict)
        flash("数据已经添加，因暂未开放数据修改功能，如填写有误，请联系管理员更改")
    return render_template("forms.html", form=form)


@app.route('/submit/<token>',methods = ['GET'])
def submit(token):
    if token == '246c2276a9790a3f875d808835cbba91':
        if autoSubmit():
            return '自动提交完成！'
    else:
        return 'Token错误'


if __name__ == '__main__':
    app.run(debug=True)