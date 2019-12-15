

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	items = skus.split(',')
	item_dic = {}
	for x in items:
		if x in item_dic:
			item_dic[x] += 1
		else:
			item_dic[x] = 1
    return 100


