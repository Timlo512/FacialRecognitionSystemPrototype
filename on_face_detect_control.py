"""
This file is used to control the on_face_detect function in the mainflow run_realtime_video function
By executing this program, the function will modify on_face_detect.json in the control folder. 
"""

import json

def turn_on_face_detect():
    with open('control/on_face_detect.json',"r") as f:
        on_face_detect = json.load(f)

    if on_face_detect["on_face_detect"]:
        on_face_detect["on_face_detect"] = False
    else:
        on_face_detect["on_face_detect"] = True

    with open('control/on_face_detect.json',"w") as f:
        json.dump(on_face_detect,f)

    pass

if __name__ == "__main__":
    turn_on_face_detect()