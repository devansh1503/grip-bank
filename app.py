from pydoc import render_doc
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from pyrsistent import inc
import pymongo

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/banking"
#mongo = PyMongo(app)
#customer_collection = mongo.db.costumer
#histor = mongo.db.history
myclient = pymongo.MongoClient("mongodb+srv://devansh1503:bandd007@cluster0.irh8e.mongodb.net/banking?retryWrites=true&w=majority")

mydb = myclient["banking"]
customer_collection = mydb["costumer"]
histor = mydb["history"]

@app.route('/')
def home():
    customer = (customer_collection.find())
    history = (histor.find())
    return render_template('index.html', dab=customer, his=history)


@app.route("/transfer", methods=['GET'])
def show_data():
    if request.method == 'GET':
        name = request.args.get("cus")
        amt = request.args.get("num")
    if name != "" and amt != "":
        history = histor.insert_one(
        {"name": name, "amount": amt })
        customer_collection.update_one({'name':name},{"$inc":{'balance':int(amt)}})
    return home()
@app.route("/delete")
def delete():
    histor.drop()
    return home()


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
