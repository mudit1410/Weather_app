from flask import Flask,render_template,request
import requests


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        city_name = request.form['cityname']
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=fa7af243b6c88cdaafecf69f5e03c054'
        response =requests.get(url.format(city_name)).json()
        temp = response['main']['temp']
        weather = response['weather'][0]['main']
        min_temp=response['main']['temp_min']
        max_temp=response['main']['temp_max']
        icon = response['weather'][0]['icon']
        
        return render_template('index.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,icon=icon,city_name=city_name)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)