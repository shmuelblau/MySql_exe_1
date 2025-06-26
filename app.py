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
    new = Agent.from_post_request(request.form)
    dal.add(new)
    return redirect("/")


@app.route('/edit' , methods=['POST']) 
def edit():
    new = Agent.from_post_request(request.form)
    dal.edit(new)
    return redirect("/")


@app.route('/delete' , methods=['POST']) 
def delete():
    agent_id = request.form.get('id')
    agent = Agent(id=agent_id)
    dal.delete(agent)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
