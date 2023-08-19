import time
a_list = list(range(10))
a_tuple = tuple(range(10))

start_time = time.time()
for i in a_tuple:
    pass

a_list[5] =35
print()
print(time.time() - start_time)

start_time = time.time()
for i in a_list:
    pass

print(time.time() - start_time)

a_tuple