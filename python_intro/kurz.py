import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def convert_from_czk():   
    user_amount = input("Zadej částku v CZK: ")
    user_amount = float(user_amount)
    user_curr = input("Zadej cílovou měnu: ")
    if data.get(user_curr) == None:
        print(f"{bcolors.FAIL}Tato měna není k dispozici{bcolors.ENDC}\n")
        return
    result = user_amount / data[user_curr]
    result = round(result, 2)

    print(f"Vysledna castka je {bcolors.BOLD}{bcolors.OKGREEN}{result} {user_curr}{bcolors.ENDC}")
    
def convert_to_czk(curr_in):
    if data.get(curr_in) == None:
        print(f"{bcolors.FAIL}Tato měna není k dispozici{bcolors.ENDC}\n")
        return
    user_amount_in = input("Zadej částku v "+curr_in+": ")
    user_amount_in = float(user_amount_in)

    result = user_amount_in * data[curr_in]
    result = round(result, 2)

    print(f"Vysledna castka je {bcolors.BOLD}{bcolors.OKGREEN}{result} CZK.{bcolors.ENDC}")

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