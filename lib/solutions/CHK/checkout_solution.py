import math

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    """
    Add the total checkout item values
    :param: skus: checkout items in
    string i.e. (A, B, C)
    :return: total value after adding the
    items
    :rtype: int
    """

    if not isinstance(skus, str):
        return -1

    skus = skus.replace(" ", "").split()
    items = [x for x in skus]
    print(items)
    item_dic = {}
    for x in items:
        if x in item_dic:
            item_dic[x] += 1
        else:
            item_dic[x] = 1

    total = 0
    for key, value in item_dic.items():
        if key == 'A':
            total += 50 * value
            total_discount = math.floor(item_dic['A'] / 3)
            if item_dic['A'] >= 3:
                total -= (20 * total_discount)
        elif key == 'B':
            total += 30 * value
            total_discount = math.floor(item_dic['B'] / 2)
            if item_dic['B'] >= 2:
                total -= (20 * total_discount)
        elif key == 'C':
            total += 20 * value
        elif key == 'D':
            total += 15 * value
        else:
            return -1

    return total



