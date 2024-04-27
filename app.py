from flask import Flask, render_template, request 
import requests, json
from serpapi import GoogleSearch
import google.generativeai as genai

genai.configure(api_key="AIzaSyCORZjVKNWJWiZ7arHPIqKK8XNfLF879Ao")

model = genai.GenerativeModel('gemini-pro')
app = Flask(__name__, static_folder='static', template_folder='templates')

hotel_names = []


@app.route('/', methods = ['GET', 'POST'])
def index():
    global hotel_names 
    results = {}
    checkin = ''
    checkout = ''
    if request.method == 'POST' and request.form.get('button1') == 'submit':

        text = request.form.get('loc', '')
        checkin = request.form.get('checkin', '')
        checkout = request.form.get('checkout', '')

        if(text == "" or checkin == "" or checkout == ""):
            return render_template('index.html', error = True)
        params = {
            "api_key": "c1fed33f43014632d06b27c4a7808bede13b4be6bb258dc774f3ea5d30b6ccf9",
            "engine": "google_hotels",
            "q": text,
            "hl": "en",
            "gl": "us",
            "check_in_date": checkin,
            "check_out_date": checkout,
            "currency": "USD"
        }

        if text == "clear":
            return render_template('index.html', loc = "")

        search = GoogleSearch(params)
        results = search.get_dict()
        hotel_names = []

        for brand in results.get('brands', []):
            hotel_names.append(brand['name'])
            for child_brand in brand.get('children', []):
                hotel_names.append(child_brand['name'])


        for property_data in results.get('properties', []):
            hotel_names.append(property_data['name'])

            """
    At the command line, only need to run once to install the package via pip:

    $ pip install google-generativeai
    """


    # Set up the model
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
        }

        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        ]


        model = genai.GenerativeModel(model_name="gemini-pro",
                                    generation_config=generation_config,
                                    safety_settings=safety_settings)

        convo = model.start_chat(history=[])

        response = convo.send_message("Please make a numbered list of five tourist activities that are most relevant in " + text + ". For each tourist activity, please give a brief description of the activity in ten words or less. Do not bold the titles of the tourist activities.")
        activities = [x for x in (convo.last.text).split("\n") if x != ""]
        print(activities)

        if response != "this is not a real location":
            return render_template('index.html', loc = hotel_names[0:15], Gemini = activities)
    return render_template('index.html', loc = "")

@app.route('/about', methods = ['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/hotels/<string:name>')
def hotels(name):

    
    return render_template('hotels.html', name = name)
if __name__ == '__main__':
    app.run(debug=True)