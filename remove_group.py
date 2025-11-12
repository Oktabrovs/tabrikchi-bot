from reading_base import data1, tsk1
def remove_info(id_list: list):
    '''returns modified data and tasks'''
    data = data1()
    kys = list(data.keys())
    ids = []
    for i in kys:
        lst = list(data[i].keys())
        if -1002917798854 in lst:
            if len(lst) == 1:
                ids.append(i)
                data.pop(i)
            else: data[i].pop(-1002917798854)
        elif -1002089463048 in lst:
            if len(lst) == 1:
                data.pop(i)
                ids.append(i)
            else: data[i].pop(-1002089463048)
    tsks = tsk1()
    if ids:
        for i in ids:
            tsks.remove(i)
    return data, tsks