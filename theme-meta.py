import os, sys

if len(sys.argv) < 2:
    print('Usage: theme-meta.py [jfpt file]')
    sys.exit(1)

jfpt = sys.argv[1]
lines = []
with open(jfpt, 'r') as f:
    lines = f.readlines()

metadata = {}
known_keys = ['Name', 'Author', 'Version', 'Date', 'Pack', 'Type', 'Description']
unknown_key = False
unknown_key_message = '*Unrecognized key'

in_metadata = False
for l in lines:
    l = l.strip()
    if l == '# metadata #':
        in_metadata = True
        continue
    elif l == '# end metadata #':
        in_metadata = False
        break
    if in_metadata:
        try:
            k, v = l.split(':', 1)
        except ValueError:
            continue
        k = k.strip()
        v = v.strip()
        if not v: v = '<empty field>'
        metadata[k] = v

base_file = os.path.basename(sys.argv[1])
print(f'\n--- Metadata for {base_file} ---')
for k, v in metadata.items():
    print(f'{k}', end='')
    if k not in known_keys:
        unknown_key = True
        print('*', end='')
    print(f': {v}')
if unknown_key: print(unknown_key_message)
print('-' * (21 + len(base_file)))