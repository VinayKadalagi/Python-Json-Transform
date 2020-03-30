import json

jsonMap = { "comments" : "Notes" ,
            "bookNumber" : "bookingId",
            "firstName" : "fullName" }

def find_key(obj, key):
    if isinstance(obj, dict):
        yield from iter_dict(obj, key, [])
    elif isinstance(obj, list):
        yield from iter_list(obj, key, [])

def iter_dict(d, key, indices):
    for k, v in d.items():
        if k == key:
            yield indices + [k], v
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])

def iter_list(seq, key, indices):
    for k, v in enumerate(seq):
        if isinstance(v, dict):
            yield from iter_dict(v, key, indices + [k])
        elif isinstance(v, list):
            yield from iter_list(v, key, indices + [k])

with open('./bwi.json') as f:
   bwi = json.load(f)

seq = []
for oldvalue in jsonMap:
    seq = find_key(bwi, oldvalue)
    for item in list(seq):
        tempstr = str(item[0])
        print(tempstr)
        oldcmdparam = tempstr.replace(',', '][')
        newcmdparam = oldcmdparam.replace(oldvalue, jsonMap[oldvalue])
        exec ("bwi" + newcmdparam + "= bwi" + oldcmdparam)
        exec("del bwi" + oldcmdparam)

print (json.dumps(bwi))
