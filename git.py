import os
import subprocess
import sys



# ==============================================================

paths = [
    r"a"
]

# ==============================================================
try:
    action = sys.argv[1]
except:
    print("An action must be passed (up/down)")
    exit()

if action == "up":
    for path in paths:
        useless_cat_call = subprocess.run(["git","pull"], 
                                  stdout=subprocess.PIPE, 
                                  text=True, 
                                  input="Hello from the other side")

        print(useless_cat_call.stdout.strip()) 

elif action == "down":
    for path in paths:
        os.chdir(path)
        subprocess.run(["git", "pull"])


