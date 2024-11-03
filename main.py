from flask import Flask,request


app = Flask(__name__) # Create a flask app instance,Trying to create wrapper with help of flask, converting entire function to a flask



@app.route('/')  #set of rules
def helloworld():
    return "Hello World"



@app.route('/sudh')  #set of rules
def helloworld1():
    return "Hello World1"

@app.route('/user')  #set of rules
def print_user():
    data = request.args.get("name")
    return f"{data}"


if __name__ == '__main__':
    app.run(debug = True)   


