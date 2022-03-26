## THE MEATBALL for line ctf lib
---
Meatball is a small library that manages files.
You can check the fast-managed data here.
It supports simple AES encryption.
There are small vulnerabilities that may occur when managing files.

---

```python

from me7_ba11.meatball import MeatBall

## Create meatball and create data
# append data
mb = MeatBall('meat.ball',)
data = {data:'meatball'}
key = mb.append(data)
print(key)
data = mb.get({"key":"uuid key"})
print(data)
{'uuid key':'meatball'}

# update data
data = {'key':'uuid key', 'data': 'meatball_change'}
mb.update(data)
data = mb.get({"key":"uuid key"})
print(data)
{'uuid key':'meatball_change'}

## File upload and update
# upload
with open('file','rb') as f:
    _file = f.read()

data = {data:'meatball'} <- Parameters are not used when uploading files.
key = mb.append(data, _file)
print(key)
data = mb.get({"key":"uuid key"})
print(data)
{'uuid key':'encoded file binary'}

# update to file
data = {'key':'uuid key', 'data': 'meatball'} <- Parameters are not used when uploading files.
mb.update(data, _file)
data = mb.get({"key":"uuid key"})
print(data)
{'uuid key':'encoded file binary'}

## Encryption
# append data with encryption
mb = MeatBall('meat.ball',)
data = {data:'meatball', enc='on'}
key = mb.append(data)
print(key)
data = mb.get({"key":"uuid key"})
print(data)
{'uuid key':'meatball'}

# update data with encrtyption
data = {'key':'uuid key', enc='on', 'data': 'meatball_change'}
mb.update(data)
data = mb.get({"key":"uuid key"})
print(data)
{'uuid key':'meatball_change'}

```