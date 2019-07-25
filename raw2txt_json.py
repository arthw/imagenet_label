
import json

raw=[]
with open("imagenet_1000.raw", "r") as f1:
    raw = [x.split(sep=':', maxsplit=1)[-1].strip()[1:-2] for x in f1]
#    raw = json.load(f1)
    print(raw)

with open("imagenet_1000.txt", "w") as f2:
    f2.write("\n".join(raw))


with open("imagenet_1000.json", "w") as f3:
    o = {}
    i = 0
    for item in raw:
      
        o[i] = item
        i += 1

    json.dump(o, f3)
