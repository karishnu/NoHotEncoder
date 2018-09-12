

def encoder(data, columns, name):
    length = len(columns)
    data[name] = 0
    for i in range(0, length):
        data[name] = data[name] + data[columns[i]]*i

    data.drop(columns, axis=1, inplace=True)



