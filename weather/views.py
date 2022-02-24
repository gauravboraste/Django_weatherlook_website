from importlib.resources import contents
from django.shortcuts import render,redirect
import requests
import math
import datetime
# Create your views here.


def index(request):
    return render(request, "weather_api/home.html")

val = None
def result(request):
    if request.method == "POST":
       
        city_name = request.POST["city"].lower()
        
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid=f70c947861e71f9a10374d879215247d"
        w_dataset = requests.get(url).json()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=f70c947861e71f9a10374d879215247d"
        dataset = requests.get(url).json()

        # https://api.openweathermap.org/data/2.5/weather?q=goa&appid=f70c947861e71f9a10374d879215247d
        # sea_level=w_dataset["list"][3]["main"]["sea_level"],
        #print(sea_level)
        global val
        def val():
            return city_name
        dt=dataset['wind']["speed"]
        #print(date2)

        da2=dataset['dt']
        date22 = datetime.datetime.fromtimestamp(float(da2))
        print(date22)
        try:
            context = {
            
                "city_name":dataset["name"],
                "city_country":w_dataset["city"]["country"],
                "wind":dataset['wind']["speed"],
                "degree":dataset['wind']["deg"],
                "status":dataset['weather'][0]['description'],
                "status1":w_dataset['list'][1]['weather'][0]['description'],
                "status2":w_dataset['list'][2]['weather'][0]['description'],
                "status3":w_dataset['list'][3]['weather'][0]['description'],
                "status4":w_dataset['list'][4]['weather'][0]['description'],
                "status5":w_dataset['list'][5]['weather'][0]['description'],
                "status6":w_dataset['list'][6]['weather'][0]['description'],




                "cloud":dataset['clouds']['all'],
                'date':date22,
                'date1':w_dataset['list'][1]["dt_txt"],
                'date2':w_dataset['list'][2]["dt_txt"],
                'date3':w_dataset['list'][3]["dt_txt"],
                'date4':w_dataset['list'][4]["dt_txt"],
                'date5':w_dataset['list'][5]["dt_txt"],
                'date6':w_dataset['list'][6]["dt_txt"],


                "temp": round(w_dataset["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(w_dataset["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(w_dataset["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(w_dataset["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(w_dataset["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(w_dataset["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(w_dataset["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(w_dataset["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(w_dataset["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(w_dataset["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(w_dataset["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(w_dataset["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(w_dataset["list"][6]["main"]["temp_max"] -273.0),


                "pressure":w_dataset["list"][0]["main"]["pressure"],
                 
                "humidity":w_dataset["list"][0]["main"]["humidity"],
                "humidity1":w_dataset["list"][1]["main"]["humidity"],
                "humidity2":w_dataset["list"][2]["main"]["humidity"],
                "humidity3":w_dataset["list"][3]["main"]["humidity"],
                "humidity4":w_dataset["list"][4]["main"]["humidity"],
                "humidity5":w_dataset["list"][5]["main"]["humidity"],
                "humidity6":w_dataset["list"][6]["main"]["humidity"],

                "sea_level":w_dataset["list"][0]["main"]["sea_level"],


                "weather":w_dataset["list"][1]["weather"][0]["main"],
                "description":w_dataset["list"][1]["weather"][0]["description"],
                "icon":w_dataset["list"][0]["weather"][0]["icon"],
                "icon1":w_dataset["list"][1]["weather"][0]["icon"],
                "icon2":w_dataset["list"][2]["weather"][0]["icon"],
                "icon3":w_dataset["list"][3]["weather"][0]["icon"],
                "icon4":w_dataset["list"][4]["weather"][0]["icon"],
                "icon5":w_dataset["list"][5]["weather"][0]["icon"],
                "icon6":w_dataset["list"][6]["weather"][0]["icon"],

            }
        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, "weather_api/results.html", context)
    else:
    	return redirect('home')

def previous(request):
        ok = val()
        # print(ok)

      
   
        url = f"https://api.openweathermap.org/data/2.5/weather?q={ok}&appid=f70c947861e71f9a10374d879215247d"
        
        data = requests.get(url).json()
       

        current_time =data["dt"]
        lat=data["coord"]["lat"]
        lon=data["coord"]["lon"]
        dt = datetime.datetime.fromtimestamp(float(current_time))
        # print (current_time)        #print( lat)
        #print( lon)
        url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={current_time}&appid=f70c947861e71f9a10374d879215247d"
        
        w_dataset = requests.get(url).json()
     
        da1=w_dataset['current']['dt']
        daten = datetime.datetime.fromtimestamp(float(da1))
        
        date5=w_dataset['hourly'][6]['dt']
        date1 = datetime.datetime.fromtimestamp(float(date5))
        # print(date5)
        da2=w_dataset['hourly'][5]['dt']
        date2 = datetime.datetime.fromtimestamp(float(da2))
        # print(date1)
        da3=w_dataset['hourly'][4]['dt']
        date3 = datetime.datetime.fromtimestamp(float(da3))
        # print(date2)
        da4=w_dataset['hourly'][3]['dt']
        date4 = datetime.datetime.fromtimestamp(float(da4))
        # print(date3)
        da4=w_dataset['hourly'][2]['dt']
        date5 = datetime.datetime.fromtimestamp(float(da4))
        # print(date4)
        humidity1=w_dataset['hourly'][0]['humidity']
        # print(humidity1)
        
        try:
            check = {
                  "city_name":ok,      
            'date1':date1,
            "wind":w_dataset['current']['wind_speed'],
            "degree":w_dataset['current']['wind_deg'],
            "status":w_dataset['list'][0]['weather'][0]['description'],
            "icon":w_dataset["list"][0]["weather"][0]["icon"],
            "cloud":w_dataset['current']['clouds'],
                'date':daten,
                'date1':date1,
                'date2':date2,
                'date3':date3,
                'date4':date4,
                'date5':date5,
               "humidity1":w_dataset["current"]["humidity"],


               
            }
        except:
            check = {
            "city_name":ok.upper(), 
            'date1':date1,
            "wind":w_dataset['current']['wind_speed'],
            "degree":w_dataset['current']['wind_deg'],
             "status":w_dataset['current']['weather'][0]['description'],
             "cloud":w_dataset['current']['clouds'],
             'date':daten,
                'date1':date1,
                'date2':date2,
                'date3':date3,
                'date4':date4,
                 'date5':date5,
            "temp1":math.floor(w_dataset["hourly"][4]["temp"] -273.0),
            "temp2":math.floor(w_dataset["hourly"][3]["temp"] -273.0),
            "temp3":math.floor(w_dataset["hourly"][2]["temp"] -273.0),
            "temp4":math.floor(w_dataset["hourly"][1]["temp"] -273.0),
            "temp5":math.floor(w_dataset["hourly"][0]["temp"] -273.0),

            "temp": round(w_dataset["current"]["temp"] -273.0),

            "humidity1":w_dataset["hourly"][4]["humidity"],
             "humidity2":w_dataset["hourly"][3]["humidity"],
              "humidity3":w_dataset["hourly"][2]["humidity"],
               "humidity4":w_dataset["hourly"][1]["humidity"],
                "humidity5":w_dataset["hourly"][0]["humidity"],

            "presure1":w_dataset["hourly"][4]["pressure"],
            "presure2":w_dataset["hourly"][3]["pressure"],
            "presure3":w_dataset["hourly"][2]["pressure"],
            "presure4":w_dataset["hourly"][1]["pressure"],
            "presure5":w_dataset["hourly"][0]["pressure"],

               "icon":w_dataset["current"]["weather"][0]["icon"],
               "icon1":w_dataset["hourly"][4]["weather"][0]["icon"],
               "icon2":w_dataset["hourly"][3]["weather"][0]["icon"],
               "icon3":w_dataset["hourly"][2]["weather"][0]["icon"],
               "icon4":w_dataset["hourly"][1]["weather"][0]["icon"],
               "icon5":w_dataset["hourly"][0]["weather"][0]["icon"],

               "status1":w_dataset['hourly'][4]['weather'][0]['description'],
               "status2":w_dataset['hourly'][3]['weather'][0]['description'],
               "status3":w_dataset['hourly'][2]['weather'][0]['description'],
               "status4":w_dataset['hourly'][1]['weather'][0]['description'],
               "status5":w_dataset['hourly'][0]['weather'][0]['description'],
        }

        return render(request, "weather_api/previous.html", check)
   

