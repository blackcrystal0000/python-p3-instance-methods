#!/usr/bin/env python3

class Person:
    def talk(self):
        print("Hello World!")
    
    def walk(self):
        print("The person is walking.")

person1 = Person()
person1.talk()  # calling an instance method to talk
person1.walk()  # calling another instance method to walk