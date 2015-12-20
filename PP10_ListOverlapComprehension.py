import random


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = random.sample(range(100), 11)
d = random.sample(range(100), 13)


def common_lists(list1,list2):
	common = [number for number in set(list1) if number in list2]
	print (common)


if __name__ == "__main__":
	common_lists(c,d)
