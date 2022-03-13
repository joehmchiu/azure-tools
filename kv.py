#!/usr/bin/env python3
import sys

try:
    sys.path.append('/home/joechiu/utils')
    import u
except:
    print("utilities not found")

arr = list()
kvn = "kv-box-001" # the existing key vault name in azure
opt = sys.argv[1]

def fill(a):
  for key in a:
      res = u.az.kv(kvn, key)
      h = u.js.loads(res)
      arr.append(h)

if opt.lower() in ['*','all']:
  fill(u.js.loads(u.az.kvlist(kvn)))
else:
  fill(sys.argv[1:])

u.js.pp(arr)
