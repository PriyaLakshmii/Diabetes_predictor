from distutils.log import debug
from flask import Flask , render_template , request
import joblib 

app = Flask(__name__)
#load the model
model=joblib.load('diabetes.pkl')

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/data', methods=['post'])
def data():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    result = model.predict([[int(preg), int(plas), int(pres), int(skin), int(test), int(mass), int(pedi), int(age)]])    
    if result[0]==1:
        data='Person is Diabetic'
    else:
        data='Person is not Diabetic'
    print(data)        
    return render_template('input.html', data=data)
    # return render_template('predict.html', data=data)        
    
app.run(host='0.0.0',port=8080) # should be always at the end
#debug=True --any changes made in the code will be automatically updated in the website/browser automatically 
# and we have to just refresh the browser for the changes to be reflected

#http://ec2-52-15-227-58.us-east-2.compute.amazonaws.com:8080/data---link for the website
#https://peaceful-mountain-90959.herokuapp.com/ | https://git.heroku.com/peaceful-mountain-90959.git---heroku links

