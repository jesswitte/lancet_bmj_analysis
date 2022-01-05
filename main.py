from hathitrust_api import DataAPI
import pandas as pd
import codecs, time, os, random

data_api = DataAPI("546686df08", "fbda40a272c61f76a40d3c80ee2e")

files = [x for x in os.listdir('hathivols') if x.endswith('.txt')]

already = []

for f in files:
    f = f.replace('.txt', '').replace('+', '/').replace('=', ':')
    already.append(f)

print(already)
print()

meta = pd.read_csv('lancet_to_1910_3.csv')
hathi_ids = meta.id



for anid in hathi_ids:
    if anid in already:
        continue
    pages = []
    finished = False

    print(anid)
    for i in range(1, 1000):
        try:
            text = data_api.getpageocr(anid, i)
            text = codecs.decode(text, 'utf-8')
            pages.append(text)

        except Exception as inst:
            print(type(inst))
            print(inst.args)
            if inst.args[0].startswith('404'):
                already.append(anid)
                finished = True
            break
        time.sleep(1)

    if finished:
        print(i)
        print()
        cleanid = anid.replace('/', '+').replace(':', '=')
        with open('hathivols/' + cleanid + '.txt', mode = 'w', encoding = 'utf-8') as f:
            for i, p in enumerate(pages):
                f.write(p)
                f.write('\n')
                f.write('<page ' + str(i + 1) + '>\n')
    else:
        time.sleep(50)
        print('failed: ' + str(i))
        print()
        cleanid = anid.replace('/', '+').replace(':', '=')
        if not os.path.isdir(cleanid):
            os.mkdir(cleanid)
        for i, p in enumerate(pages):
            with open(cleanid + '/' + str(i) + '.txt', mode = 'w', encoding = 'utf-8') as f:
                f.write(p)
print('finished')



