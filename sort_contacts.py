def sort_contacts(param):
    result = []
    for i in sorted (param.keys()) :  
        result.append((i,) + param[i])
    return result
