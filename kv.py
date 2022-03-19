#!/usr/bin/env python3
import os, sys

try:
  path = os.path.dirname(os.path.abspath(__file__))
  sys.path.append(path + "/utils")
  import u
except:
  print('{"error":"utilities not found"}')
  sys.exit()

os.chdir(path)

arr = list()
# update the keyvault name in the utility conf class
kvn = u.conf.kvn 
try:
  opt = sys.argv[1]
except:
  u.js.pp({"error":"option not found"})
  sys.exit()

def fillin(a):
  for key in a:
    res = u.az.kv(kvn, key)
    h = u.js.loads(res)
    arr.append(h)

if opt.lower() in ['*','all']:
  fillin(u.js.loads(u.az.kvlist(kvn)))
else:
  fillin(sys.argv[1:])

u.js.pp(arr)
