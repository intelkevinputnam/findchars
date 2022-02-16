import sys

if len(sys.argv) < 2:
    print('File name required.')
    exit()

workfile = sys.argv[1]

content = ''
try:
    f = open(workfile)
except IOError:
    print(workfile + " doesn't exist.")
else:
    with f:
        content = f.readlines()

badChars = ['“','”','—',' ','↩︎︎']

lineCounter = 1
badCharCounter = 0
for line in content:
    for char in badChars:
        if char in line:
            badCharCounter += 1
            print('Enemy char (' + char + ') detected at line ' + str(lineCounter) + '!')
    lineCounter += 1
print (str(badCharCounter) + ' bad chars found.')
