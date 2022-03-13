#!/usr/bin/env python3
import sys

try:
  sys.path.append('/home/joechiu/utils')
  import u
except:
  print('{"error":"utilities not found"}')
  sys.exit()

arr = list()
kvn = "kv-box-001" # the existing key vault name in azure
try:
  opt = sys.argv[1]
except:
  u.js.pp({"error":"option not found"})
  sys.exit()

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
