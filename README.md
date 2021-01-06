# Simple Lamport sign implementation in Python

SHA-256 hash function is used.


### How to create pair of public and private keys?

```
python generate.py [key_name]
```

It will produce two files with names `[key_name].public` and `[key_name].private`.

Be careful, files will be overwritten!


### How to sign file?

```
python sign.py [document_name] [key_name]
```

On output will be one file with name `[key_name].sign`.


### How to check file with sign?

```
python verify.py [document_name] [key_name]
```

Public and sign files should be at same path and have default names format.
