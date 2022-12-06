Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from hashlib import blake2b
h = blake2b(key=b'pseudorandom key', digest_size=16)
h.update(b'message data')
h.hexdigest()
'3d363ff7401e02026f4a4687d4863ced'
