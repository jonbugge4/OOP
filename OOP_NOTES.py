#Its a notes page
#procedural vs OOP
# Procudural is how we've been coding (def printname (n) --> print(n) --> printname(John))
"""
Data hiding(making private): object's data attributes are hidden from code outside the object
- Access restricted to the object's methods--> protects from accidental corruptions --> outside code does not need to know 
internal structure of the object.

Weapons: sowrd, M4
M4: number of bullets, speed, range, fire
-- We have to hide the attributes from the user so that they cannot maniuplate it so that the Sword shoots or the M4 has unlimited bullets

THIS ALSO ALLOWS US TO REUSE OBJECTS IN DIFFERENT CODE

Create a file with object definitions, and ALSO a program file that calls the obecjt file. 
We will now have two files for things


CLASS: code that specifices the data attributes and methods of a particular type of object (like a blueprint for building cookie-cutter
houses) (Weapons)

INSTANCE: an object created from a CLASS (Sword, M4)-- things may be unique, but they still have the same attributes that
define them as a class


Format: begin with 
class Class_name:

'self' Parameter: required in every method in the class - references the specific object that the method is working on

_init__ is initalizes

__ allows for attributes to remain hidden





self 
"""