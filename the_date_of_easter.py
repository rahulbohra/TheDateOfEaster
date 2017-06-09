year = raw_input("Enter the year : ")
year = int(year)

a = year % 19
#A print "A = ", a

b = year / 100
#A print "B = ", b

c = year % 100
#A print "C = ", c

d = b / 4
#A print "B = ", d

e = b % 4
#A print "E = ", e

f = (b + 8) / 25
#A print "F = ", f

g = (b - f + 1) / 3
#A print "G = ", g

h = ((19 * a) + b - d -g + 15) % 30
#A print "H = ", h

i = c / 4
#A print "I = ", i

k = c % 4
#A print "K = ", k

l = (32 + (2 * e) + (2 * i) - h - k) % 7
#A print "L = ", l

m = (a + (11 * h) + (22 * l)) / 451
#A print "M = ", m

n = (h + l - (7 * m) + 114) / 31
#A print "Month (N) = ", n

p = (h + l - (7 * m) + 114) % 31
#A print "P = ", p

day = p + 1
#A print "Day = ", day

easterDay = str(day) + " - " + str(n) + " - " + str(year)
print "Easter Sunday : ", easterDay
