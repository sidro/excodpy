import requests, random
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "dad"}
)

data = response.json()

list_ = ([a['joke'] for a in [joke for joke in data['results']]])

joke = random.choice(list_)

print(joke)