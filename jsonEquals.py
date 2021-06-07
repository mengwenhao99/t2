import hashlib
import json


def compared(a, b):
    json1 = json.dumps(a)
    json2 = json.dumps(b)
    md51 = hashlib.md5(str(json1).encode('UTF-8')).hexdigest()
    md52 = hashlib.md5(str(json2).encode('UTF-8')).hexdigest()
    return md51 == md52


if __name__ == '__main__':
    obj1 = {'name': 'Marcelo', 'age': 30, 'address': {'country': 'Brasil'}}
    obj2 = {'name': 'Marcelo2', 'age': 30, 'address': {'country': 'Brasil'}}
    print(f'obj1 和 obj2 对比，结果 = {compared(obj1, obj2)}')
