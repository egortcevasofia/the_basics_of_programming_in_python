import sys

message = sys.stdin.readlines()
k = ' '.join(message)
print(len(set(k.split())))
print(type(k))