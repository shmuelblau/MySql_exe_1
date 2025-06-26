from flask import Flask , render_template ,redirect, request
from DAL.Eagle_DAL import Eagle_DAL
from Models.Agent import Agent

app = Flask(__name__)
dal = Eagle_DAL()


@app.route('/')
def home():

    data = dal.Select()
    
    return render_template('index.html' , data=data )

@app.route('/add' , methods=['POST']) 
def add():
    info = request.form.get('inpo')
    new = Agent.from_post_request(info)
    dal.add(new)
    return redirect("/")


@app.route('/edit' , methods=['POST']) 
def edit():
    info = request.form.get('inpo')
    new = Agent.from_post_request(info)
    dal.edit(new)
    return redirect("/")


@app.route('/delete' , methods=['POST']) 
def delete():
    info = request.form.get('inpo')
    new = Agent.from_post_request(info)
    dal.delete(new)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)