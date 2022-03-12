import os, json

ident_gap = 2

class js():
  def pj(d): # pretty json results
    return json.dumps(d, indent = ident_gap)
  def pp(d):
    print(json.dumps(d, indent = ident_gap))
  def loads(s):
    res = ''
    try:
      res = json.loads(s)
    except Exception as e:
      res = {"error":"invalid key or results - %s" % e}
    return res

class az():
  def kv(kvn, key):
    return os.popen("~/azure/za-kv %s %s 2>/dev/null" % (kvn, key)).read()
