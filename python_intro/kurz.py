import httpx
from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

res = httpx.get(url)

rows = res.text.split("\n")
rows[-3]  # od konce
rows[1:3]
# slicing vrátí pole od provku s indexem 1 do prvku s indexem 2 tzn konec není zahrnut

rows = rows[2:-1]
data = {}
for r in rows:
    cols = r.split('|')
    currency = cols[-2]
    rate = cols[-1]
    rate = rate.replace(',', '.')
    rate = float(rate)

    data[currency] = rate

print(data)
pprint(data)


user_amount = float((input("Zadej castku ")))

user_source = "CZK"
user_target = input("zadej cilovou menu ")

result = user_amount / data[user_target]
result = round(result, 3)
print(f"Vysledek je {result} {user_target}.")