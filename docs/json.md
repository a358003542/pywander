## json
some fucntion for json file quick operation.

### write_json
```python
def write_json(file, data):
    """
    write data to json file
    """
```

### get_json_file
```python
def get_json_file(json_filename, default_data=None):
    """
    try get json file or auto-create the json file with default_data
    """
```

### get_json_data
```python
def get_json_data(json_filename, default_data=None):
    """
    get json file data
    """
```

### get_json_value
```python
def get_json_value(json_filename, key, default_data=None):
    """
    get value by key in json file if your json file stored value as one dict.
    """
```
### set_json_value
```python
def set_json_value(json_filename, key, value, default_data=None):
    """
    set value by key and value in json file if your json file stored value
    as one dict.
    """
```