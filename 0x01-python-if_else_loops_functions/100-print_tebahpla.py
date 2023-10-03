#!/usr/bin/python3
#!/usr/bin/python3

for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{0}{1}".format(chr(i), chr(i - 32)), end='')
    else:
        print("{0}{1}".format(chr(i - 32), chr(i)), end='')
