from flask import Flask,request , render_template
import pickle

app = Flask(__name__)


@app.route('/')

def hello_world():
      return render_template('login.html')

database= {'Shariq' : 'Shariq@123' , 'Ali':'Ali012' , 'Umer':'umyl998'}

@app.route('/form_login' , methods=['POST'])

def login():
      name1 = request.form('Name')
      pwd = request.form('pwd')
      phone = request.form('Phone')
      city = request.form('City')
      messages = request.form('Message')
      
      if name1 not in database:
            return render_template('login.html' , info='Wrong Username')
      else:
            if database[name1] != pwd:
                    return render_template('login.html' , info='Wrong Password')
            else:
                    return render_template('wlcome.html' , name= name1)
            
if __name__ == '__main__':
      app.run()