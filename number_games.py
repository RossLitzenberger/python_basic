import random	

def random_member(some_list):
	x = len(some_list) - 1
	num = random.randint(0,x)
	return some_list[num] 