from flask import Flask, render_template, request
import json, random, requests
app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        # zipcode = request.form['zipcode']
        pass
    else:
        api_key = '78f727aa66cd91e4a1bede26a7d2e88a'
        getResponse = requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={97201},us&units=imperial&appid={api_key}')
        changeResponse = getResponse.text
        response = json.loads(changeResponse)
        print(response)




    return render_template('index.html', response=response)






# response = requests.get('https://or.water.usgs.gov/non-usgs/bes/skyline_school.rain')
# # print(response.text)
# lines = response.text.split('\n')
# lines = lines[11:] # chop off the junk at the start
# for line in lines:
#     print(line.split())


# # or use regular expressions
# # https://regex101.com/r/QwMfRM/1



# # get all the rain data on the site
# def get_rain_file_urls():
#     response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
#     text = response.text
#     rain_files = re.findall(r'\w+\.rain', text)
#     rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]
#     return rain_files

# def get_rain_data(url):
#     # your code here
#     print(url)
#     pass

# rain_file_urls = get_rain_file_urls()
# for rain_file_url in rain_file_urls:
#     data = get_rain_data(rain_file_url)
#     print(data)

# exit()
