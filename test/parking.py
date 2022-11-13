from flask import Flask
from flask import request
import requests

app = Flask(__name__)
PARKING_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6ImgxMjlyYjlxOGYiLCJ0b2tlbiI6eyJpdiI6IjhjNjM0NGFmZjc4NDIyODdhZGZkYjcxOWUzMzdkYWE2IiwiY29udGVudCI6IjNhZGQyNzI1ZDBkZmNjMDZkYTRkZmQ0OGQ0M2YwODEyYzg2OTNiN2Y1YWNkYTYzNmQ5YzM0MmFkYzVmNDVkMjJiOGVlMzU4YzNhMzQzNmY5Y2I1OTM0NTEzNzE0NDhhOTVhN2M0YjhkMjlmOTBmYjA0ZWRlYTJhZmZlOTcwNjY0NThjYzZiZDk1N2U3YjRmMjgxMTE4NTRkNTc5YjBlYTY2NDI0NzgwN2Y3ZDIyOWRlY2UyYTFiZGQwMzY0ZjI0MjY0MTJmOGJkZjBmMTJmMzIwM2IwZTMxZTdkNzZlYjRiOWIzZjc1MjViYmMwNGFiYmM3ZTVhYTE4YTRiODhlNTUxMmQzOGVhZDAyZTZhZWQ5YTQwZGE2OTM4MjA2Y2I5MmI1YTJiNTNlYmNjNzMyODI3NmQ2NWUxYzIxY2NkMWE0NmMwY2UxNGNjNmVlYzViNTYyZGYwYjMyMzI5Y2M0MjI3YmQzZmQxNDUyZWE0MWYyYTljOWNkZDAyMmI0ODI5M2E2ZGE1MjRkN2FiMzI3Y2I4MTcwNDhmYmQ0YWJhNmRjMzViMmE0ZDEyNzUwZThjMmJkMzY0YTUwMmMyOTNlYzljM2VlNmNiMmNiODlkMDBkMzRiMTRmYzdiYTFmNTE5YTdhZmNjMTdlOTUxMDRmOWY5ZWU5NjgzZWM4NDg3MzQ2NWFlNGMwN2Q4NzQyOTkzOTE3ZWJlZTUwM2JlMjcyODY2OGVjZmEwZWRlZGY0MDgxNTI4MjVmYzg2NzExYTYyZWU5ZGE0ZmExOTgzNDkzZmM2YTAxYTAxMzFhODk4M2E0ZjcxODA0ZjA3NjUyNWFlOTNiOTlhMTg3NmRmYzVlYmViZjEyMGE4NzdkNDllZjdmMWFiYjQ3In0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI4YzYzNDRhZmY3ODQyMjg3YWRmZGI3MTllMzM3ZGFhNiIsImNvbnRlbnQiOiIyZmY3MWMwMGMzYTFjYzVjZGQ2ZWRjNjRiNTMwMmIxNmY3NTQzYzdhNWFjYjg2Mjk4YWU1NjdjYmZkZDQ3YjQyZGFmNDFiZGYyMDFhMjBkZGU2NDAxNzZmIn0sImp0aSI6IjVlZDgzNDM0LTJkZWYtNDZlZS1iMTc1LTYxM2YzYTg0ZGY3NiIsImlhdCI6MTY2ODI5NTc2MCwiZXhwIjoxNjY4Mjk5MzYwfQ.RO3ad18pBl_xkwSzGuigun3tmhW8gMuaMZ5XkbObBwQ"


@app.route('/')
def index():
    return 'Web App with Python Flask!'


@app.route('/offStreetParking')
def offStreetParking():
    #INFORMATION RECEIVED
    #Coordinates (Latitude, Longitude)
    #Total Spaces
    #Distance
    #isOpen
    #Rates
    
    url = "https://api.iq.inrix.com/lots/v3"
    params = {
        'point' : request.args.get('point'),
        'radius' : 150, 
        'limit' : 10
    }
    headers = {
        'Authorization': 'Bearer {}'.format(PARKING_TOKEN)
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.text)
    return response.json() 

@app.route('/onStreetParking')
def onStreetParking():
    #INFORMATION RECEIVED
    #Coordinates of meters
    #Distances
    #isOpen
    #Rates
    
    url = "https://api.iq.inrix.com/blocks/v3"
    params = {
        'point' : request.args.get('point'),
        'radius' : 50, #shorter range because on-street parking & from INRIX API explorer
        'limit' : 10
    }
    headers = {
        'Authorization': 'Bearer {}'.format(PARKING_TOKEN)
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.text)
    return response.json() 


app.run(host='0.0.0.0', port=81)
