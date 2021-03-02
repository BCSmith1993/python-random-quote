import random
def primary():
   last = 13
   rnd = random.randint(0,last)
   print(This is nifty!)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  primary()
