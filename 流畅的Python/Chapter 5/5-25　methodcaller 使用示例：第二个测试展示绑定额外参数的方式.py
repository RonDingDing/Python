from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
 

print(upcase(s))
#'THE TIME HAS COME'
hiphenate = methodcaller('replace', ' ', '-')
print(hiphenate(s))
#'The-time-has-come'
