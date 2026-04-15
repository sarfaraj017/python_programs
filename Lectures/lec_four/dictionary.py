dict={
    "name" : "sk sarfaraj",
    "age": 21,
    "roll":"CSE244017",
    "sub":{ #nested
        "math":65,
        "phy":56,
    }
}
print(type(dict))
print(dict.get("sub"))
#methods
print(dict.keys())
print(dict.values())
print(dict.items())
#update
dict_two={
    "class":"b.tech"
}
dict.update(dict_two)
print(dict)