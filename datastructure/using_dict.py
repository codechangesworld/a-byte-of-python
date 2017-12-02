#!/usr/bin/python
# Filename: using_dict.py

ab = {
    "swaroop": "swaroop@swaroopch.com",
    "larry": "larry@wall.org",
    "matsumoto": "matz@ruby-lan.org",
    "spammer": "spamar@hotmail.com"
}

print("swaroop's address is", ab["swaroop"])
del ab["spammer"]
print("\nThere are {0} cantacts in the address-book\n".format(len(ab)))

for name, address in ab.items():
    print("Contact {0} at {1}".format(name, address))

ab["guido"] = "guido@python.com"
if "guido" in ab:
    print("\nguido's address is", ab["guido"])

string = "strings"
for cc in string:
    print(cc, end=' ')
    cc = 'a'
print(string)
