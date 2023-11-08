import json
import os
import copy
from videohash import VideoHash
from os.path import join

PATH = r"C:"

file_extensions = (".mp4")
files = []
for root, dirs, files in os.walk(PATH, topdown=True):
    for fi in files:
        if fi.endswith(file_extensions):
            files.append(fi)

print("Calculando Hashes...")
links = [{"file": join(PATH, x), "hash": VideoHash(path=join(PATH, x))} for x in files]
print("Fazendo Deepcopy dos hashes...")
comp = copy.deepcopy(links)

dups = []
LENGTH = len(links)
now = 1
for i in links:
    print(f"{now}/{LENGTH} => {i['file']}")
    i_hash = i["hash"]
    for j in comp:
        if i == j: continue
        j_hash = j["hash"]

        if i_hash.is_similar(j_hash):
            dups.append({"link": i["file"], "dup": j["file"], "delta": i_hash - j_hash})
    comp.remove(i)
    now += 1

with open("closure.json", "w", encoding="utf-8") as f:
    json.dump(dups, f)