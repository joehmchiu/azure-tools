import os, sys

class cli():
  def kv(kvn, key):
    return os.popen("~/azure/za-kv %s %s" % (kvn, key)).read()
