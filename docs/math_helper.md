## math_helper
do some math .

### number_radix_conversion
进制转换
```text
assert number_radix_conversion(10, 'bin') == '1010'
assert number_radix_conversion('0xff', 2, 16) == '11111111'
assert number_radix_conversion(0o77, 'hex') == '3f'
assert number_radix_conversion(100, 10) == '100'
```

### is_even
是否是偶数

### is_odd
是否是奇数

### is_prime
是否是素数

### gen_prime
到第n个的所有素数的生成器函数

### gen2_prime
到小于某个数n的所有素数的生成器函数

### prime
第n个素数

### gen_fibonacci
到第n个的斐波那契数列生成器函数


### fibonacci
第几个斐波那契数

### gen_factorial
阶乘

start*....stop的生成器，默认start=1

### factorial
start*....stop的值，默认start=1即为stop!的值