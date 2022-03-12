#!/usr/bin/env python3
import sys

try:
    sys.path.append('/home/joechiu/utils')
    import u
except:
    print("utilities not found")

arr = list()
kvn = "kv-box-001" # the existing key vault in azure

for key in sys.argv[1:]:
    res = u.az.kv(kvn, key)
    h = u.js.loads(res)
    arr.append(h)

u.js.pp(arr)
