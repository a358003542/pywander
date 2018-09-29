#!/usr/bin/env python
# -*-coding:utf-8-*-

##
"""
winreg_utils

base on Ryan Kelly Copyright 2009,  (ryan@rfk.id.au)'s regobj.py

updated by cdwanze.

Redistributable under the terms of the MIT license:



This module provides a thin wrapper around the standard _winreg module,
allowing easier and more pythonic access to the Windows Registry.

All access to the registry is done through Key objects, which (surprise!)
represent a specific registry key.  To begin, there are pre-existing Key
objects defined for the HKEY_* root keys, using both long and short names:

  >>> HKEY_CURRENT_USER
  <regobj Key 'HKEY_CURRENT_USER'>
  >>> HKLM
  <regobj Key 'HKEY_LOCAL_MACHINE'>


## Key(parent, *name)

## add_child(name)



## .subkeys  迭代列出所有子键，TODO 数据结构字典化支持按名字索引
## .get_subkey 根据名字获取某个子键
## .set_subkey 设置某个子键的值
## .del_subkey 删除某个子键


## create 实际向注册表提交改动

And that's that - enjoy!

"""

import winreg


class NoHKeyError(Exception):
    pass


class Key(object):
    """Class representing a registry key.

    Each key has a name and a parent key object.  Its values can be
    accessed using standard item access syntax, while its subkeys can
    be accessed using standard attribute access syntax.

    Normally code would not create instance of this class directly.
    Rather, it would begin with one of the root key objects defined in
    this module (e.g. HKEY_CURRENT_USER) and then traverse it to load
    the appropriate key.
    """
    _hkey = None

    def __init__(self, parent, *names, sam=winreg.KEY_READ, create=True, **kwargs):
        """Construct a new Key object.

        The key's name and parent key must be specified.  If the given
        name is a backslash-separated path it will be processed one
        component at a time and the intermediate Key objects will be
        transparently instantiated.

        The optional argument 'sam' gives the security access mode to use
        for the key, defaulting to KEY_READ.  It more permissions are required
        for an attempted operation, we attempt to upgrade the permission
        automatically.

        If the optional argument 'hkey' is given, it is the underlying
        key id to be used when accessing the registry. This should really
        only be used for bootstrapping the root Key objects.
        """
        if len(names) == 0:
            raise ValueError("a non-empty key name is required")

        if isinstance(parent, str):
            import sys
            current_module = sys.modules[__name__]
            parent = getattr(current_module, parent)

        for pname in names[:-1]:
            parent = Key.add_child(parent, pname, create=create)

        self.name = names[-1]
        self.parent = parent
        self.sam = sam

        self._hkey = self.create_hkey(create=create)

    @property
    def hkey(self):
        if not self._hkey:
            raise NoHKeyError('there is no hkey.')
        return self._hkey

    @hkey.setter
    def hkey(self, value):
        self._hkey = value

    @staticmethod
    def add_child(parent, child_name, create=True, **kwargs):
        child = Key(parent, child_name, **kwargs)
        child.hkey = child.create_hkey(create=create)
        return child

    def add_subkey(self, child_name, create=True, **kwargs):
        child = Key(self, child_name, **kwargs)
        child.hkey = child.create_hkey(create=create)
        return child

    def delete(self):
        """
        删除本Key
        :param child:
        :return:
        """
        winreg.DeleteKey(self.parent.hkey, self.name)

    def create_hkey(self, create=True):
        if not self.has_hkey():
            if self.parent is None:
                self.hkey = winreg.ConnectRegistry(None, getattr(winreg, self.name))
            else:
                if create:
                    self.hkey = winreg.CreateKey(self.parent.hkey, self.name)
                else:
                    self.hkey = winreg.OpenKey(self.parent.hkey, self.name)
        return self.hkey

    def __str__(self):
        return "<regobj Key '%s'>" % (self.names)

    @property
    def names(self):
        names = []
        obj = self
        while obj.parent is not None:
            names.append(obj.name)
            obj = obj.parent
        names.append(obj.name)
        return '\\'.join(names[::-1])

    def __repr__(self):
        return str(self)

    def has_hkey(self):
        try:
            self.hkey
            return True
        except NoHKeyError:
            return False

    def create_all_hkey(self):
        """
        核对所有的子键都创建hkey了
        :return:
        """
        avail = []

        def _set_hkey(keyobj):
            if keyobj.parent.has_hkey():
                avail.append(keyobj.parent.hkey)

                hkey = winreg.CreateKey(keyobj.parent.hkey, keyobj.name)
                keyobj.hkey = hkey
            else:
                return _set_hkey(keyobj.parent)

        _set_hkey(self)

    def get_subkey(self, name):
        """
        获取某个子键，如果不存在将抛出异常
        """
        child = Key(self, name, create=False)
        child.hkey = child.create_hkey(create=False)
        return child


    def del_subkey(self, name):
        """Delete the named subkey, and any values or keys it contains."""
        self.sam |= winreg.KEY_WRITE

        winreg.DeleteKey(self.hkey, name)


    def get(self, name):
        """
        获取某个子键，不存在不会抛出异常
        :param name:
        :return:
        """
        try:
            return self.__getitem__(name)
        except KeyError:
            return None

    def __getitem__(self, name):
        """Item access retrieves key values."""
        self.sam |= winreg.KEY_QUERY_VALUE

        try:
            if name == '':
                data = winreg.QueryValue(self.parent.hkey, self.name)
            else:
                data = winreg.QueryValueEx(self.hkey, name)

            if isinstance(data, tuple):
                return Value(data=data[0], name=name, type=data[1])
            elif data:
                return Value(data=data, name=name)
            else:
                return Value(name=name)
        except WindowsError:
            raise KeyError("no such value: '%s'" % (name,))

    def __setitem__(self, name, value):
        """Item assignment sets key values."""
        self.sam |= winreg.KEY_SET_VALUE
        if not isinstance(value, Value):
            value = Value(value, name)

        try:
            if name == '':
                winreg.SetValue(self.parent.hkey, self.name,
                                value.type, value.data)
            else:
                winreg.SetValueEx(self.hkey, name, 0, value.type, value.data)
        except WindowsError:
            raise KeyError("set value failed")

    def __delitem__(self, name):
        """Item deletion deletes key values."""
        winreg.DeleteValue(self.hkey, name)

    def subkeys(self):
        """Iterator over the subkeys of this key."""
        self.sam |= winreg.KEY_ENUMERATE_SUB_KEYS
        return SubkeyIterator(self)

    def values(self):
        """Iterator over the key's values."""
        return ValueIterator(self)


class Value(object):
    """Class representing registry key values.

    Each Value instance has a name, a type and some associated data.
    The default name is '', which corresponds to the default value for
    a registry key.  The type must be one of the REG_* constants from
    this module; if it is not specified, it will be guessed from the
    type of the data.
    """

    _DWORD_MAX_SIGNED = (1 << 31) - 1

    _DWORD_MIN_SIGNED = -1 * (1 << 32)

    _DWORD_MAX_UNSIGNED = (1 << 32) - 1

    def __init__(self, data=None, name="", type=None):

        if type is None:
            type = self._default_type(data)
        #  DWORD values are unsigned, but _winreg treats them as signed.
        #  We do some conversion on input so that unsigned values are
        #  accepted, but python will convert them into negative integers.
        #  when you read it back out :-(
        if data is not None and type == winreg.REG_DWORD:
            if data < self._DWORD_MIN_SIGNED:
                raise ValueError("DWORD value too small: %s" % (data,))
            elif data > self._DWORD_MAX_UNSIGNED:
                raise ValueError("DWORD value too large: %s" % (data,))
            elif data > self._DWORD_MAX_SIGNED:
                data = int(data - self._DWORD_MAX_UNSIGNED - 1)
        self.name = name
        self.data = data
        self.type = type

    def __str__(self):
        data = (self.name, self.data, self.type)
        return "<regobj Value (%s,%s,%s)>" % data

    def __repr__(self):
        return str(self)

    def _default_type(self, data):
        if isinstance(data, int):
            return winreg.REG_DWORD
        if data is None:
            return winreg.REG_NONE
        return winreg.REG_SZ


from collections import UserList


class SubkeyIterator(UserList):

    def __init__(self, key):
        super(SubkeyIterator, self).__init__()
        self.key = key
        self.data = self.init_data()

    def __len__(self):
        return winreg.QueryInfoKey(self.key.hkey)[0]

    def __index__(self, index):
        return winreg.EnumValue(self.key.hkey, index)

    def init_data(self):
        index = 0
        data = []

        while True:
            try:
                k = winreg.EnumKey(self.key.hkey, index)
            except WindowsError:
                break

            index += 1
            data.append(Key(self.key, k))

        return data


class ValueIterator(UserList):
    """Iterator over the values contained in a key.

    This iterator is capable of efficient membership detection
    and length reporting.  As usual, the underlying registry key
    should not be modified during iteration.
    """

    def __init__(self, key):
        """
        self.Key 当前的Key
        :param key:
        """
        super(ValueIterator, self).__init__()
        self.key = key
        self.data = self.init_data()

    def __index__(self, index):
        return winreg.EnumValue(self.key.hkey, index)

    def __len__(self):
        return winreg.QueryInfoKey(self.key.hkey)[1]

    def init_data(self):
        index = 0
        data = []

        while True:
            try:
                v = winreg.EnumValue(self.key.hkey, index)
            except WindowsError:
                break
            index += 1
            data.append(Value(v[1], v[0], v[2]))
        return data


# Bootstrap by creating constants for the root keys

HKCR = Key(None, "HKEY_CLASSES_ROOT", sam=winreg.KEY_READ)

HKEY_CLASSES_ROOT = HKCR

HKCC = Key(None, "HKEY_CURRENT_CONFIG", sam=winreg.KEY_READ)

HKEY_CURRENT_CONFIG = HKCC

HKCU = Key(None, "HKEY_CURRENT_USER", sam=winreg.KEY_READ)

HKEY_CURRENT_USER = HKCU

HKDD = Key(None, "HKEY_DYN_DATA", sam=winreg.KEY_READ)

HKEY_DYN_DATA = HKDD

HKLM = Key(None, "HKEY_LOCAL_MACHINE", sam=winreg.KEY_READ)

HKEY_LOCAL_MACHINE = HKLM

HKPD = Key(None, "HKEY_PERFORMANCE_DATA", sam=winreg.KEY_READ)

HKEY_PERFORMANCE_DATA = HKPD

HKU = Key(None, "HKEY_USERS", sam=winreg.KEY_READ)

HKEY_USERS = HKU
