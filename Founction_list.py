shopping_list = []

def show_help():
  print ("What should we pick up at the store?")
  print ("Enter DONE to stop. Enter HELP for this help")


def add_to_list(item):
  shopping_list.append(item)
  print("Adding! List has {} items.".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
      print(item)

  

while  True:
  new_item = input("> ")
  if new_item == 'DONE':
    break 
  elif new_item == 'HELP':
    show_help()
    continue
  add_to_list(new_item)
  continue

show_list()