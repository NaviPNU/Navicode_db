import requests
import pandas as pd

#response = requests.get("http://172.20.173.52:5000/coord_type", params={"navicode": '3232'})
#response = requests.get("http://172.20.173.52:5000/get_coord_static", params={"navicode": '1111'})
#response = requests.get("http://172.20.173.52:5000/get_coord_dynamic", params={"navicode": '3232',"latitude":'35.825591' ,"longitude": '128.754325'})
response = requests.post("http://172.20.173.52:5000/add_coord_location",json={"name": '가야정', "navicode": '2222', "latitude":'35.823307', "longitude": '128.756087', "type": '2'})
print(response.json())
