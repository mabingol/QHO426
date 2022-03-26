#Once a set is created you can add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)

#thisset.add("orange","aaa")

tropical = {"pineapple", "mango", "papaya"}

#mylist = ["kiwi", "orange"]

thisset.update(tropical)

print(thisset)

thisset.remove("banana")
print(thisset)