
#############################
# Use None data type

values = [-50, -80, -100]
max_value = None
for i in values:
    if max_value is None or i > max_value:
        max_value = i

print(max_value)