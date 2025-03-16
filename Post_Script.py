import requests

# API endpoint
url = 'http://127.0.0.1:5000/'

# Path to test image
files = {'file': open(r'C:\Users\amuqt\Work Drive\Learning\Flask_Apps\Parse_Equation\Test samples\Sample2.jpg                                                           ', 'rb')}

# Sending POST request
response = requests.post(url, files=files)

# Output response
print(response.json())
