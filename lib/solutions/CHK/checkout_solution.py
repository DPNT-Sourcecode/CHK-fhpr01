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

    PRICE_A = 50
    PRICE_B = 30
    PRICE_C = 20
    PRICE_D = 15
    PRICE_E = 40

    if not isinstance(skus, str):
        return -1

    skus = skus.replace(" ", "")
    items = [x for x in skus]

    item_dic = {}
    for x in items:
        if x in item_dic:
            item_dic[x] += 1
        else:
            item_dic[x] = 1

    total = 0
    for key, value in item_dic.items():
        if key == 'A':
            total += PRICE_A * value
            total_discount = math.floor(item_dic['A'] / 3)
            if item_dic['A'] >= 3:
                total -= (20 * total_discount)

        elif key == 'B':
            total += PRICE_B * value
            total_discount = math.floor(item_dic['B'] / 2)
            if item_dic['B'] >= 2:
                total -= (15 * total_discount)

        elif key == 'C':
            total += PRICE_C * value

        elif key == 'D':
            total += PRICE_D * value

        elif key == 'E':
            total += PRICE_E * value

        else:
            return -1

    return total
