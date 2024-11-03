""" To generate API key go to my weather app and sign in 
open weather map -- API --One call API 3.0
To expose my data to others  """

from flask import Flask , render_template, request
import requests 

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("Weather.html")

@app.route("/weatherapp",methods = ['POST' , "GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"# u won't get data if u hit this api link so should pass parameter 
    #So pass parameter
    #https://api.openweathermap.org/data/2.5/weather?q=london&units=metric&appid=9d64a799c76f46d8e162a47b4b83e915

# Try to call url1 you will get error because it is paid API and also observer that u need to pass only one parameter
    """url1 = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
    apikey = ""
    data1 = requests.get(url1,params={"appid":apikey})
    print(data1)"""

    param = {
        'q':request.form.get("city"),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')
        }
    response = requests.get(url,params=param)
    data = response.json()
    return f"data : {data}"

if __name__ == '__main__':
    app.run(debug=True)

