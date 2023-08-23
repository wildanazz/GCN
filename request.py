import requests

url = "http://localhost:7071/api/nn"

payload = {}
files = [
    ('data', ('facebook.npz', open(
        "C://Users//Wildan Aziz//OneDrive//Documents//Dev//45616756-GCN//data//facebook.npz", 'rb'), 'application/octet-stream'))
]
headers = {}

response = requests.request(
    "POST", url, headers=headers, data=payload, files=files)

print(response.text)
