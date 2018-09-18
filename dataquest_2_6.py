
##########
# trt/except handling in Python

try:
    float('hello')
except Exception:
    print("Error converting to float.")