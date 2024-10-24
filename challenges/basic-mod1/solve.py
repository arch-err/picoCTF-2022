#!/usr/bin/env python
import string

a = string.ascii_lowercase + "0123456789_"

with open("./message.txt", "r") as f:
    message = f.read()

flag = "picoCTF{"

for c in message.split(" "):
    # print(c)
    flag += a[int(c) % 37]

flag += "}"

print(flag)
