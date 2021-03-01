T = input()
dics = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for key in dics:
    T = T.replace(key, "_")
print(len(T))
