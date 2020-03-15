from AutoSubmitFlag import AutoSubmitFlag
from AutoAttack import AutoAttack

flags = AutoAttack('attack.json').aoe()
submit = AutoSubmitFlag('config.json')
for flag in flags:
    submit.submitFlag(1,flag) # 第一个参数为题目编号，第二个参数为提交的flag