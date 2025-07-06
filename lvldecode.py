import sys, gzip, base64

if len(sys.argv) < 2:
    print('Usage: lvldecode.py [GMD gdshare file]')
    sys.exit(1)

ldata = ''
with open(sys.argv[1], 'rb') as f:
    ldata = gzip.decompress(base64.urlsafe_b64decode(f.read().decode().split('<k>k4</k><s>')[1].split('</s>')[0].encode())).decode('utf-8')
with open('output.txt', 'w+') as f:
    f.write(ldata)
print("Level string exported to output.txt")