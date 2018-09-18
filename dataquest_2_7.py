
##########
# Display exception type (ValueError)
# Display exception message

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))