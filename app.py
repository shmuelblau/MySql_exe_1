from flask import Flask , render_template ,redirect, request
from DAL.Eagle_DAL import Eagle_DAL

app = Flask(__name__)
dal = Eagle_DAL()


@app.route('/')
def home():

    data = dal.Select()
    
    return render_template('index.html' , data=data )

@app.route('/add' , methods=['POST']) 
def add():
    inpo = request.form.get('inpo')
    
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)