from wtforms import Form,StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired


class SubmitForm(Form):
    username = StringField('学号', render_kw={'placeholder': '请输入你的学号'}, validators=[Length(11, 11, message='学号格式错误')])
    password = PasswordField('密码', render_kw={'placeholder': '请输入你的密码'}, validators=[DataRequired(message='密码不能为空')])
    site = StringField('户籍', render_kw={'placeholder': '请输入你的密码户籍'}, validators=[DataRequired(message='户籍不能为空')])
    phone = StringField('手机号', render_kw={'placeholder': '请输入你的密码手机号'}, validators=[Length(11, 11, message='手机号码格式不正确')])
    submit = SubmitField('请确认无误后再提交')