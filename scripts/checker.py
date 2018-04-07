import requests, json

url = "http://localhost:8000/api"
d_input = input("Enter Data to Predict :- ")
data = {'Data' : d_input}
r = requests.post(url, json=data)
print('Prediction :- {}'.format(r.json()['results'][0]))
