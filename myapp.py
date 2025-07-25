import requests

re = requests.get(url="http://localhost:8000/api/tasks/")
data = re.json()

print(data)