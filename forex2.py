from bs4 import BeautifulSoup
import sys
from forex_python.converter import CurrencyRates

class Error(Exception):
    pass

class BadCurrencyPair(Error):
    pass

def position_size(conversion, quote):
    risk = float(input("Enter amount you are risking: "))
    pips = float(input("Enter the amount of pips you are willing to risk: "))
    lot_size = float(input("Enter the value per pip (this will be based on lot size): "))
    if quote == "JPY":
        lot_size = lot_size*100
    if quote != "USD":
        adjusted_rate=risk*conversion
    else:
        position = float(risk/(pips*lot_size))
    if (lot_size == .10 or (lot_size/10 == 1 and quote == "JPY")):
        print ("\nyou should buy %f micro lots"%position)
    elif (lot_size == 1 or (lot_size == 100 and quote == "JPY")):
        print ("\nyou should buy %f mini lots"%position)
    elif (lot_size == 10 or (lot_size == 1000 and quote == "JPY")):
        print("\nyou should buy %f standard lots"%position)
    else:
        print("\nyou should quit trading forex...")

def menu():
    c = CurrencyRates()
    while True:
        print("\nType 'Q' or 'Quit' at any time to exit the program.")
        curreny_pair = input("What currency pair are you trading(enter as 'Base Pair'/'Quote Pair'): ").upper()
        if curreny_pair in ['Q', 'QUIT']:
            print("\nGood luck out there!")
            sys.exit(0)
        try:
            base, quote = curreny_pair.split('/')
            conversion = float(c.convert(base, quote, 1))
            position_size(conversion, quote)
        except:
            print("The currency pair you entered can't be found...")



if __name__=="__main__":
  menu()
