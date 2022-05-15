from flask import render_template
#主網頁
def index():
    return render_template('index.html') 

#內科response

def gm():
    return render_template('一般內科.html')

def gi():
    return render_template('消化內科.html')

def air():
    return render_template('過敏風濕免疫內科.html')

def nephro():
    return render_template('腎臟內科.html')

def meta():
    return render_template('內分泌新陳代謝科.html')

def ho():
    return render_template('血液腫瘤科.html')

def cv():
    return render_template('心臟內科.html')

def cm():
    return render_template('胸腔內科.html')
        










