	# long hand is list()
shopping_list = []

print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
	new_item = input(" > ")

	if new_item == 'DONE':
	   break	

	   # append will add item to end of the list
	shopping_list.append(new_item)
	# this will count how many tiem we have
	print("Added! List has {} items.".format(len(shopping_list)))
	continue

print("Here's your list:")

for item in shopping_list:
	print(item)