import nacl.utils

buf = nacl.utils.random(128)
print(buf.hex(), "\n")

for i in buf:
    print(hex(i)[2:], end=" ")

