#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str.split('language')[0]
str = str[39:] + " with " + str[:6]
print(str)
