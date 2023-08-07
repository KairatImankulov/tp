import requests
from PIL import Image
from io import BytesIO

r = requests.get('https://img5.lalafo.com/i/posters/original/c8/55/8e/b53f0fc1fbc4c8e3dae649bdd1.jpeg')

image = Image.open(BytesIO(r.content))
image.save("example.jpg","jpeg")

r = requests.get('https://jsonplaceholder.typicode.com/users')
print(r.status_code)
print(r.text)