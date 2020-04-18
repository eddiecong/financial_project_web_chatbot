import http.client

conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "5f728b6756msh8dddad515ae5b37p14463cjsnad2a940fff4b"
    }

conn.request("GET", "/query?symbol=TSLA&function=GLOBAL_QUOTE", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))