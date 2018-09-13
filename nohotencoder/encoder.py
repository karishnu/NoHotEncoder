

def encoder(data, columns, name, handle_linear_dep = False):
    length = len(columns)
    data[name] = 0
    for i in range(0, length):
        data[name] = data[name] + data[columns[i]]*i

    if(handle_linear_dep):
        data['name'] = data['name'].replace([0], length+1)

    data.drop(columns, axis=1, inplace=True)



