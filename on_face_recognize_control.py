"""
This file is used to control the on_face_detect function in the mainflow run_realtime_video function
By executing this program, the function will modify on_face_detect.json in the control folder. 
"""

import json

def main():
    with open('control/on_face_recognize.json',"r") as f:
        on_face_recognize = json.load(f)

    if on_face_recognize["on_face_recognize"]:
        on_face_recognize["on_face_recognize"] = False
    else:
        on_face_recognize["on_face_recognize"] = True

    with open('control/on_face_recognize.json',"w") as f:
        json.dump(on_face_recognize,f)

    pass

if __name__ == "__main__":
    main()