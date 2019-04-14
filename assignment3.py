Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=range(30)
>>> for n in x :
	if n % 3==0 and n % 5==0:
		print(" {} fizzbuzz.".format(n))
	elif n % 3 ==0:
		print(" {} fizz .".format(n))
	elif n % 5 ==0 :
		print(" {} buzz.".format(n))

		
 0 fizzbuzz.
 3 fizz .
 5 buzz.
 6 fizz .
 9 fizz .
 10 buzz.
 12 fizz .
 15 fizzbuzz.
 18 fizz .
 20 buzz.
 21 fizz .
 24 fizz .
 25 buzz.
 27 fizz .
>>> 
>>> 
>>> def sum(a,b):
	answer=a+b
	return answer

>>> sum(38,12)
50
>>> def wholenumberdivision (b,c):
	answer =b//c
	return answer

>>> wholenumberdivision (900,253)
3
>>> def division (c,d):
	answer =c/d
	return answer

>>> division (234,81)
2.888888888888889
>>> def subtract (d,e):
	answer = d-e
	return answer

>>> subtract (90,56)
34
>>> 
>>> def modulus (e,f):
	answer=e%f
	return answer

>>> modulus (67,9)
4
>>> def multiply (f,g):
	answer =f*g
	return answer

>>> multiply (50,40)
2000
>>> def exponent (g,h):
	answer = g **h
	return answer

>>> exponent (324,45)
94302989232555928047705241328053749499365872523618269727709077263035464860282807412703313112341152866410245914624
>>> def percentage (h,j):
	answer = (h/j)*100
	return answer

>>> percentage (26,50)
52.0
>>> 
