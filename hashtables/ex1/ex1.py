def get_indices_of_item_weights(weights, length, limit):
    table = {}

    for i, weight in enumerate(weights):
        complement = limit - weight
        if complement in table:
            return (i, table[complement])
        else:
            table[weight] = i

    return None


if __name__ == "__main__":
    print(get_indices_of_item_weights(
        [12, 6, 7, 14, 19, 3, 0, 25, 40], length=9, limit=7))
