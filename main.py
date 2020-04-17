import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

def extract_page():
  countries = []
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  trs = soup.tbody.find_all("tr")

  for tr in trs:
    tds = tr.find_all("td")

    if tds[2].text == "":
      continue

    countries.append({
      "name": tds[0].text.capitalize(),
      "currency_code": tds[2].text
    })

  return countries

def choose_country():
  try:
    index = int(input("#: "))
    if index >= 0 and index < len(countries):
      print(f"You choose {countries[index]['name']}")
      print(f"The currency code is {countries[index]['currency_code']}")
    else:
      print("Choose a number from the list.")
      choose_country()
  except:
    print("That wasn't a number.")
    choose_country()

def main():
  print("Hello! Please choose select a country by number:")
  
  for i, country in enumerate(countries):
    print(f"# {i} {country['name']}")
  
  choose_country()
  
countries = extract_page()

main()