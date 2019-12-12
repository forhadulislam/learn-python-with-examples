
brands = ["Apple", "Samsung", "Huawei", "One plus", "Nokia"]

print(brands)
print(brands[1])
print(brands[-1])
print(brands[0:2])
print(brands[:2])
print(brands[1:])
print(brands[-4:-1])

# Case sensitive
if "Nokia" in brands:
    print("Nokia is in the list")

print( "We have a list of {0} brands. {1} is one of them.".format(len(brands), brands[0]) )