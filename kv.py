#!/usr/bin/env python3
import os, sys
import argparse

parser = argparse.ArgumentParser(prog='Get scret value(s) from Key Vault')
parser.add_argument('-k', '--kv', '--keyvault', help='input the key vault namei - ./kv.py -k my-key-vault', required=False)
parser.add_argument('-o', '--opt', '--option', help='options - ./kv.py -o ["*"|all|show|list]', required=False)
parser.add_argument('-s', '--secret', '--secrets', type=str, nargs='+', help='input the secret names - ./kv.py -s s1 s2 s3')
args = parser.parse_args()

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
if args.kv:
  kvn = args.kv
else:
  kvn = u.conf.kvn 
try:
  if args.opt:
    opt = args.opt
  else:
    opt = ""
except:
  u.js.pp({"error":"option not found"})
  sys.exit()

def fillin(a):
  if not a: 
    u.js.pp({"error":"option not found"})
    sys.exit()
  for key in a:
    res = u.az.kv(path, kvn, key)
    h = u.js.loads(res, key)
    arr.append(h)

if opt.lower() in ['*','all','show','list']:
  u.js.pp(u.js.loads(u.az.kvlist(path, kvn)))
  sys.exit()
  # fillin(u.js.loads(u.az.kvlist(path, kvn)))
else:
  fillin(args.secret)

u.js.pp(arr)

