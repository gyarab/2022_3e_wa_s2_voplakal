import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]

def convert_from_czk():   
    user_amount = input("Zadej částku v CZK: ")
    user_amount = float(user_amount)
    user_curr = input("Zadej cílovou měnu: ")
    if data.get(user_curr) == None:
        print("Tato měna není k dispozici.\n")
        return
    result = user_amount / data[user_curr]
    result = round(result, 2)

    print(f"Vysledna castka je {result} {user_curr}")
    
def convert_to_czk(curr_in):
    if data.get(curr_in) == None:
        print("Tato měna není k dispozici.\n")
        return
    user_amount_in = input("Zadej částku v "+curr_in+": ")
    user_amount_in = float(user_amount_in)

    result = user_amount_in * data[curr_in]
    result = round(result, 2)

    print(f"Vysledna castka je {result} CZK.")

data = {}

for r in rows:
    cols = r.split("|")
    amount = cols[-3]
    curr = cols[-2]
    rate = cols[-1]
    rate = rate.replace(",", ".")
    rate = float(rate) / float(amount)
    data[curr] = rate

while True:
    user_curr_in = input("Zadejte vstupní měnu:")
    if user_curr_in == "CZK":
        convert_from_czk()
    else:
        convert_to_czk(user_curr_in)
    print("\n")