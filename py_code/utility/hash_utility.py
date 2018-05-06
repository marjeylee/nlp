"""
hash操作工具类
"""
import hashlib

src = 'this is a ma5 test.'
m2 = hashlib.md5()
m2.update(src.encode('utf-8'))
print(m2.hexdigest())
