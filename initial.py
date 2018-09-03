"""
This module is used to initialize all default setting,
including switch.json
"""
import json

def initialize():
     
    def initalize_switch_json():
        init = {"quit":False}
        with open("control/switch.json","w") as f:
            json.dump(init,f)

    def initialize_on_face_detect_json():
        init = {"on_face_detect":True,"face_detect_boundary_shape":"rectangle"}
        with open("control/on_face_detect.json","w") as f:
            json.dump(init,f)

    def initialize_on_face_recognize_json():
        init = {"on_face_recognize": False, "loaded": False}
        with open("control/on_face_recognize.json","w") as f:
            json.dump(init,f)
    # Execution all initializing functions

    initalize_switch_json()
    initialize_on_face_detect_json()
    initialize_on_face_recognize_json()
    pass