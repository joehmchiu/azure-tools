import os, json

ident_gap = 2

class js():
  def validate(s):
    try:
      json.loads(s)
      return True
    except:
      return False

  def pj(d): # pretty json results
    return json.dumps(d, indent = ident_gap)

  def pp(d):
    print(json.dumps(d, indent = ident_gap))

  def loads(s, k="error"):
    if not js.validate(s):
      if s:
        return {"error":"Invalid or malformatted JSON - %s" % s}
      elif not s:
        return {k:"No results found"}
      else:
        return {"error":"Invalid or malformatted JSON"}
    else:
      return json.loads(s)

class az():
  def kv(path, kvn, key):
    return os.popen("%s/azure/za-kv %s %s 2>/dev/null" % (path, kvn, key)).read()

  def kvlist(path, kvn):
    return os.popen("%s/azure/za-kv-list %s 2>/dev/null" % (path, kvn)).read()

class conf():
  kvn = "dev2-khq-vault" # the existing key vault name in azure



