import base64, gzip, sys

if len(sys.argv) < 2:
    print('Usage: lvlencode.py [text file]')
    sys.exit(1)

export = ''
with open(sys.argv[1], 'rb') as f:
    final_enc = base64.urlsafe_b64encode(gzip.compress(f.read())).decode()
    export = f'<d><k>kCEK</k><i>4</i><k>k2</k><s>LVLEncode</s><k>k3</k><s> </s><k>k4</k><s>{final_enc}</s><k>k45</k><i>286138</i><k>k13</k><t/><k>k21</k><i>2</i><k>k50</k><i>35</i></d>'
with open('export.gmd', 'w+') as f:
    f.write(export)
print("Level exported to export.gmd")