## dict_helper
some operation on python dict object.

### compare_dict_include
compare two dict object include or contained relationship
    
   return True : d totally contain the second dict

```text
>>> compare_dict_include({'a':1},{})
True
>>> compare_dict_include({'a':1},{'a':2})
False
>>> compare_dict_include({'a':1},{'a':1})
True
>>> compare_dict_include({'a':1,'b':2},{'a':1})
True
>>> compare_dict_include({'a':1,'b':2},{'b':2})
True
```

### merge_dict
merge two dict, very old school style. just equal to the below:

```text
x = {'a':1, 'b':2}
y = {'b':3}
z = {**x, **y}
```

