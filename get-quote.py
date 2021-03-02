def primary():
   print(This is nifty!)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[0])

if __name__== "__main__":
  primary()
