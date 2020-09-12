def intersection(arrays):
    everything = {}
    result = []

    for array in arrays:
        for val in array:
            if val in everything:
                everything[val] += 1
            else:
                everything[val] = 1

    for val in everything:
        if everything[val] == len(arrays):
            result.append(val)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
