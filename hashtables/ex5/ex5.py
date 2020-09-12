# Your code here


def finder(files, queries):
    result = []
    fdict = {}

    for file in files:
        path = file.split('/')
        filename = path[len(path) - 1]
        if filename in fdict:
            fdict[filename].append(file)
        else:
            fdict[filename] = [file]

    for query in queries:
        if query in fdict:
            for path in fdict[query]:
                result.append(path)

    print("============ RESULTS ==============")
    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
