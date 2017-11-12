#!C:\Users\0309moha\AppData\Local\Continuum\anacon\python.exe
i = 1

while i <= 100:

    if i%3 == 0 and i%5 == 0:
        print str(i) + " FuzzBin"

    elif i%3 == 0:
        print str(i) + " Fuzz"

    elif i%5 == 0:
        print str(i) + " Bin"

    else:
        print i

    i += 1
