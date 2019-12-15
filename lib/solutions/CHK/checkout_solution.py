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
            total_discount = math.floor(item_dic['A'] / 5)

            if item_dic['A'] >= 5:
                total -= (50 * total_discount)
                total_reminder_discount = item_dic['A'] - (total_discount * 5)
                if total_reminder_discount >= 3:
                    total_reminder_discount = math.floor(
                        total_reminder_discount / 3)
                    total -= (20 * total_reminder_discount)
            elif item_dic['A'] >= 3:
                total_discount = math.floor(item_dic['A'] / 3)
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
            if item_dic['B'] > 0 and item_dic['E'] >= 2:
                total_discount = math.floor(item_dic['E'] / 2)
                total_B = item_dic['B']
                if total_B == total_discount:
                    total -= PRICE_B * total_discount
                elif total_discount > total_B:
                    total -= total_B * PRICE_B
                elif total_discount < total_B:
                    total -= total_discount * PRICE_B

        else:
            return -1

    return total

