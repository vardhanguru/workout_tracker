import requests
import os
from datetime import datetime
headers={
    "x-app-id":os.environ.get("APP_ID"),
    "x-app-key":os.environ.get("API_KEY"),

}
today_date=datetime.now()

param={
 "query":"ran 3 miles and walked for 3km.",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}
urls="https://trackapi.nutritionix.com/v2/natural/exercise"
respone=requests.post(url=urls,json=param,headers=headers)
bearer_headers = {
"Authorization": os.environ.get("TOKEN")
}
for result in respone.json()['exercises']:
    payload = {
        "workout": {
            "date": today_date.strftime("%d/%m/%y"),
            "time": today_date.strftime("%H:%M:%S"),
            "exercise": result['user_input'].title(),
            "duration": result['duration_min']
        }
    }
    sheet_respone=requests.get(url= os.environ["SHEET_ENDPOINT"],headers=bearer_headers)
    print(sheet_respone.json())
    pos_res=requests.post(url= os.environ["SHEET_ENDPOINT"],json=payload,headers=bearer_headers)
    pos_res.raise_for_status()
    print(pos_res.json())