# FacialRecognitionSystemPrototype
A Facial Recognition System Prototype

Inspired by <a href = "https://github.com/davidsandberg/facenet"> davidsandberg/facenet</a>, I have built a facial recognition system prototype. It is a CUI program developed on macOS High Sierra 10.13.6. 

# Latest Version

| Date | Version | Remarks|
|----------|--------|-----------------|
|2018/09/03| beta_v1| Original Version|

# Documentation

## Get Started
1. First, download .zip file onto your desktop and unzip it. As it is a CUI-based program, it is recommended to put the file on your desktop.

2. Go to <a href = 'https://github.com/davidsandberg/facenet'>this</a> website to download the pretrained model. In the program, the pretrained model is called '20180402-114759'. It has inception RestNet architecture trained by VGGFace2. Below is the direct google drive link that you can download the pretrained model. 

<a href = 'https://drive.google.com/file/d/1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-/view'>https://drive.google.com/file/d/1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-/view</a>

For your reference:
  you can use other model which is written on tensorflow.
  
3. Unzip the pretrained model file and put it into the downloaded folder (FacialRecognitionSystemPrototype).

![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/00.png)

## Run Your Program

4. Move your directory to your downloaded folder (FacialRecognitionSystemPrototype). Run following command:

| <username>$ python mainflow.py|
|-------------------|

<b>Note that above command would be a bit different if you are using Window/ Linux/ Unix OS</b>


![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/01.png)


5. After you successfully run the program, it will be like that:


![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/02.png)

Wait around 20~30s...


![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/03.png)

It will assess your laptop camera and start to reveal real-time video on your Desktop.

Default setting:
facial detection: On
facial recognition: off
<b>It will start to detect face and display a blue color rectangle on the face detected.</b>

## Control Functions

It has four external programs to control the properties of mainflow program. To run those programs, open one more commandline window, move your directory to your downloaded folder (FacialRecognitionSystemPrototype).

### take_photo.py
To save your face feature into the system, you can run take_photo.py. Run following command:

| <username>$ python take_photo.py|
|---------------------|


![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/04.png)

Then, it will ask you name in order to display it when you turn on the facial recognition.


![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/05.png)

Press enter and it will save your face feature into the system.

<b>Be aware that this program takes photo when the mainflow program successfully detects your face.</b>

### on_face_detect_control.py

To control on and off facial detection, you can run on_face_detect_control.py. Run following command:

| <username>$ python on_face_detect_control.py|
|---------------------------------|


![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/06.png)

Setting:
Facial Detection: On --> Off

It will be like that:

![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/07.png)

### on_face_recognize_control.py

To control on and off facial recognizion, you can run on_face_recognize_control.py. Run following command:

| <username>$ python on_face_recognize_control.py|
|---------------------------------|
  
![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/08.png)

Setting:
Facial Recognition: On --> Off

It will be like that:

![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/10.png)

The mainflow program then start to recognize face who has been saved in the system. For those who are not saved in the system, it will recognize as 'unknown'

Default Setting:
Max frame to detect face: 2

### quit_control.py
To quit the mainflow program, you can run quit_control.py. Run following command:

| <username>$ python quit_control.py|
|---------------------------------|
  
![alt text](https://raw.githubusercontent.com/timtimtimab/FacialRecognitionSystemPrototype/master/images/09.png)

The mainflow.py will be terminated within seconds.

## Requirement
1. Python 3.6.5
2. tensorflow 1.9.0
3. numpy 1.14.5
4. cv2 3.4.2

### Reference

1. Facial Recognition Using TensorFlow. <a href = "https://github.com/davidsandberg/facenet"> davidsandberg/facenet</a>.
2. Face Detection using Haar Cascades. <a href = "https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html"> Haar-cascade Detection in OpenCV</a>.




