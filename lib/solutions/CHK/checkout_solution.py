

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
    items = skus.replace(" ", "").split(',')
    item_dic = {}
    for x in items:
        if x in item_dic:
            item_dic[x] += 1
        else:
            item_dic[x] = 1

    total = 0
    print(item_dic)
    for key, value in item_dic.items():
        if key == 'A':
            total += 50 * value
        elif key == 'B':
            total += 30 * value
        elif key == 'C':
            total += 20 * value
        elif key == 'D':
            total += 15 * value

    return total
