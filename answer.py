import random
import time

from декораторы import time_run, null, in_out

# l = random.sample(range(0, 1000000), 1000000)
# ll = l.copy()
#
# @time_run
# def r1():
#     res1 = list(map(str, l))
#     print(res1[:5])
#
# @time_run
# def r2():
#     res2 = [str(i) for i in ll]
#     print(res2[:5])
#
#
# r1()
# r2()

# @time_run
# def etalon(n, m, x):
#     print('START')
#     time.sleep(n+m)
#     print(x)
#
# # etalon(3, 1, x=10)
# @in_out
# def summer(x, y):
#     return x + y
#
# res = summer(random.randint(1, 100),
#              random.randint(1, 100)) / 3.45 ** 3
# print(res)

from dataclasses import dataclass

d = {'key1': {'key1':'info1',
              'key2':'info2'}
     }

print(d['key1'].get('key3'))