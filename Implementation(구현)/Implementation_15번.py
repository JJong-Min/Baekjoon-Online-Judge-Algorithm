all_num = list(range(1, 10001))
delete = set()

for i in all_num:
    for j in str(i):
        i += int(j)
    delete.add(i)

self_num = sorted(set(all_num) - delete)

for i in self_num:
    print(i)
