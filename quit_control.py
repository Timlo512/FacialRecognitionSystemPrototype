"""
This file is used to quit the mainflow run_realtime_video function
By executing this program, the function will modify switch.json in
the control folder. 
"""

import json

def main():
    with open('control/switch.json',"r") as f:
        quit = json.load(f)

    quit["quit"] = True

    with open('control/switch.json',"w") as f:
        json.dump(quit,f)

    pass

if __name__ == "__main__":
    main()