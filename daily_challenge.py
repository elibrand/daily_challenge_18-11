birthyear = input("What year were you born in?")

age = 2019 - int(birthyear)

candle = (str(age)[-1])

candles = int(candle) * "i"

cake = ("         ___" + candles + "___\n" +
     """         |:H:a:p:p:y:|
       __|___________|__
      |^^^^^^^^^^^^^^^^^|
      |:B:i:r:t:h:d:a:y:|
      |                 |
      ~~~~~~~~~~~~~~~~~~~\n""")

if int(birthyear) % 4 is 0:

	print(cake * 2)
else:
	print(cake)

