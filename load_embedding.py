import json
import numpy as np

def load_embedding():
    """
    This function load saved embedding from embedding.json.
    """
    try:
        with open("control/embedding.json","r") as f:
            database = json.load(f)
        loaded_database = {name:np.array(eval(embedding)) for name,embedding in database.items()}
        return loaded_database
    except:
        print("No embedding at all.")
    finally:
        with open("control/on_face_recognize.json","r") as f:
            isloaded = json.load(f)
        isloaded["loaded"] = True
        with open("control/on_face_recognize.json","w") as f:
            json.dump(isloaded,f)

def reload_embedding():
    """
    This function turn off the embedding loaded setting in embedding.json
    """

    try:
        with open("control/on_face_recognize.json",'r') as f:
            loaded = json.load(f)
        loaded['loaded'] = False
        with open("control/on_face_recognize.json",'w') as f:
            json.dump(loaded,f)
    except:
        print("reload_embedding is failed.")