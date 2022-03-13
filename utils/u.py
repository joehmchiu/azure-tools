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

  def loads(s):
    if not js.validate(s):
      if s:
        return {"error":"Invalid or malformatted JSON - %s" % s}
      else:
        return {"error":"Invalid or malformatted JSON"}
    else:
      return json.loads(s)

class az():
  def kv(kvn, key):
    return os.popen("../azure/za-kv %s %s 2>/dev/null" % (kvn, key)).read()

  def kvlist(kvn):
    return os.popen("../azure/za-kv-list %s 2>/dev/null" % (kvn)).read()
