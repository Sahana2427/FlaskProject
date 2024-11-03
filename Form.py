from flask import Flask,request,jsonify,render_template

app = Flask(__name__)

# Function so that User should be able to see index.html


@app.route("/")# Give url at which someone can access it , / means port number to access url
def show_form():
    return render_template("index.html") #renders html file

@app.route("/check_password",methods=['POST']) # same
def check_password():
    name = request.form.get("Username")
    password = request.form.get("Password")
    print({name},{password})
    return "Username and Password received successfully"

if __name__ == "__main__":
    app.run(host ="0.0.0.0",port = 5000)