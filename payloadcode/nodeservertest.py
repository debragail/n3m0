# run test node.js server
import requests

r2 = requests.get('http://localhost:6069/ingredients', timeout=60)
print(r2.text)

r=requests.post('http://localhost:6069/ingredients',data={'id':'boop','text':'beep'}, timeout=60)
print(r.text)

r2 = requests.get('http://localhost:6069/ingredients', timeout=60)
print(r2.text)
