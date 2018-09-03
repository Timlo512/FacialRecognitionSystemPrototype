from config import Face, Encoder, Face_detect
from facenet.src import facenet
import cv2 as cv
import tensorflow as tf
import numpy as np
import time
import json
from initial import initialize
from load_embedding import load_embedding, reload_embedding
from calculation import L2_dist
from on_face_detect_control import turn_on_face_detect

def preload():
    face = Face()
    encoder = Encoder()
    face_detect = Face_detect()
    return face,encoder,face_detect

def quit_loop():
    # This function input switch.json file check if quit switch is on
    try:
        with open("control/switch.json","r") as f:
            switch = json.load(f)
        if switch["quit"]:
            return False
        else:
            return True
    except:
        print("onclick switch function happened.")
        return True

def on_face_detect():
    # This function input on_face_detect.json file check if 
    # on_face_detect is on. Default it is on.
    try:
        with open("control/on_face_detect.json","r") as f:
            switch = json.load(f)
        return switch["on_face_detect"]
    except:
        print("onclick switch function happened.")
        return True

def face_detect_rectangle(face_detect,frame):
    faces = face_detect.face_cascade.detectMultiScale(frame,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
    return frame

def save_image_switch():
    # This function input save_image.json file check if save_image
    # is on. Default it is off
    try:
        with open("control/save_image.json","r") as f:
            switch = json.load(f)
        return switch["save_image"]
    except:
        print("onclick switch function happened.")
        return False
    

def save_image(face,encoder,face_detect,frame):
    faces = face_detect.face_cascade.detectMultiScale(frame,1.3,5)
    if len(faces) == 1:
        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
            roi_color = frame[y:y+h,x:x+w]
            img = cv.resize(roi_color,dsize=(160,160),interpolation = cv.INTER_CUBIC)
            face.image = img
            embedding = encoder.generate_embedding(face)
    try:
        with open("control/save_image.json","r") as f:
            save = json.load(f)
        name = save["name"]
        with open("control/embedding.json","r") as f:
            database = json.load(f)
        database[name] = str(embedding.tolist())
        with open("control/embedding.json","w") as f:
            json.dump(database,f)
    except:
        try:
            with open("control/save_image.json","r") as f:
                save = json.load(f)
            name = save["name"]
            database = {}
            database[name] = str(embedding.tolist())
            with open("control/embedding.json","w") as f:
                json.dump(database,f)
        except:
            print("fail to save image.")
    finally:
        pass

def off_save_image_switch():
    with open('control/save_image.json',"r") as f:
        switch  = json.load(f)

    switch['save_image'] = False

    with open('control/save_image.json',"w") as f:
        json.dump(switch,f)

    pass

def off_face_detect():
    with open('control/on_face_detect.json',"r") as f:
        on_face_detect = json.load(f)

    control = False
    on_face_detect["on_face_detect"] = control

    with open('control/on_face_detect.json',"w") as f:
        json.dump(on_face_detect,f)

    pass

def on_face_recognize():
    # This function input on_face_recognize.json file check if on_face_recognize
    # is on. Default it is off
    try:
        with open("control/on_face_recognize.json","r") as f:
            switch = json.load(f)
        return switch["on_face_recognize"]
    except:
        print("onclick switch function happened.")
        return False  

def hasLoadedEmbedding():
    # This function input on_face_recognize.json file check if on_face_recognize
    # is on. Default it is off
    try:
        with open("control/on_face_recognize.json","r") as f:
            switch = json.load(f)
        return switch["loaded"]
    except:
        print("onclick switch function happened.")
        return False

def face_recognize(face,encoder,face_detect,frame,database,font):
    faces = face_detect.face_cascade.detectMultiScale(frame,1.3,5)
    if len(faces) > 2:
        faces = faces[0:2]
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        roi_color = frame[y:y+h,x:x+w]
        img = cv.resize(roi_color,dsize=(160,160),interpolation = cv.INTER_CUBIC)
        face.image = img
        embedding = encoder.generate_embedding(face)
        text, rank = 'Unknown',0.70
        try:
            for name,embedding_data in database.items():
                dist = L2_dist(embedding_data,embedding)
                if dist < 0.75 and dist < rank:
                    print(dist,"\n",name)
                    text,rank = name, dist
        except:
            print("Nothing can be recognized.")
        finally:
            cv.putText(frame,text,(x,y+5),font,1,(30,0,150),2,cv.LINE_AA) 
    
    return frame
        

def run_realtime_video():
    face, encoder, face_detect = preload()
    cap = cv.VideoCapture(0)
    font = cv.FONT_HERSHEY_SIMPLEX
    check = True
    while(check):
        # Quit Program Control
        check = quit_loop()

        # Start playing video
        ret, frame = cap.read()

        # Control face detection
        if on_face_detect():
            frame = face_detect_rectangle(face_detect,frame)

        # Save your image to embedding.json
        if save_image_switch():
            if on_face_detect():
                save_image(face,encoder,face_detect,frame)
                off_save_image_switch()
            else:
                turn_on_face_detect()
                save_image(face,encoder,face_detect,frame)
                reload_embedding()
                off_save_image_switch()
        
        # Control face recognition
        if on_face_recognize():
            if not hasLoadedEmbedding():
                database = load_embedding()
            frame = face_recognize(face,encoder,face_detect,frame,database,font)
            off_face_detect()
    
        cv.imshow('mainflow',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()
    end = True
    return end


def main():
    initialize()
    run_realtime_video()
    quit()

if __name__ == "__main__":
    main()