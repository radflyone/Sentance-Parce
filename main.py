sentance1 = input("Enter sentance ")
if len(sentance1) > 0:
  sentlist = list(sentance1)
  print('The first letter in the sentance is', sentlist [0])
  print('and the last letter is',sentlist [-1])
  sentset = set(sentance1)
  print('The total unique characters in the sentance are',len(sentset))
else:
  print('You forgot to enter a sentance')
