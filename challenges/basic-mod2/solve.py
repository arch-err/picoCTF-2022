#!/usr/bin/env python
import string

a = " " + string.ascii_lowercase + "0123456789_"

with open("./message.txt", "r") as f:
    message = f.read()

flag = "picoCTF{"

for c in message.split(" "):
    y = pow(int(c), -1, 41)
    flag += a[y]

flag += "}"

print(flag)
