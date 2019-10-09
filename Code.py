#This method uses 'Zeller's Rule'
#Formula=K+[(13*M-1)/5]+D+[D/4]+[C/4]-2*C
#Where K is the day of the month 
#Where M is month number. Adjustments done in code(Here month starts from March so 1st month is march & last month is feb)
#Where D is the last 2 digit of the year
#Where C is the first 2 digit of the year
#The remainder after dividing F by 7 decides the day ie 0 for sunday, 1 for monday..
#In equation decimals are ignored

#Taking Date, Month & Year Input
k = int(input('Enter the DATE: '))
m = int(input('Enter the MONTH NUMBER: '))
year = str(input('Enter the Year: '))

#Splitting the year into C & D (For calculation purposes)
c = int(year[:2])
d = int(year[2:])

#Adjusting M for calculation purposes
if m==1:
	m = 11
elif m==2:
	m = 12
else:
	m = m-2

#Adjusting D
if m>10:
	d = d-1

#Formula execution
f = k + ((13*m-1)//5) + d + (d//4) + (c//4) - (2*c)

#Finding day
day = f%7

#Printing the day
if day==0:
	print('Sunday')
elif day==1:
	print('Monday')
elif day==2:
	print('Tuesday')
elif day==3:
	print('Wednasday')
elif day==4:
	print('Thursday')
elif day==5:
	print('Friday')
elif day==6:
	print('Saturday')
