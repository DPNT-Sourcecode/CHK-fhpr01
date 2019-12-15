

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

    total = 0

    for key, value in item_dic.items():
        if key == 'A':
            total += 50
        elif key == 'B':
            total += 30
        elif key == 'C':
            total += 20
        elif key == 'D':
            total += 15

    return total

