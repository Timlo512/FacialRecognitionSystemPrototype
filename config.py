from facenet.src import facenet
import cv2 as cv
import tensorflow as tf


class Configuration():
    
    def __init__(self):
        self.model = "20180402-114759"

class Face():

    def __init__(self):
        self.name = None
        self.image = None
        self.embedding = None

class Encoder():
    def __init__(self,facenet_model_checkpoint="20180402-114759"):
        self.sess = tf.Session()
        with self.sess.as_default():
            facenet.load_model(facenet_model_checkpoint)
        
    def generate_embedding(self,face):
        # Get input and output tensors
        images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
        embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
        phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")

        prewhiten_face = facenet.prewhiten(face.image)

        # Run forward pass to calculate embeddings
        feed_dict = {images_placeholder: [prewhiten_face], phase_train_placeholder: False}
        return self.sess.run(embeddings, feed_dict=feed_dict)[0]

class Face_detect():
    def __init__(self):
        self.face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')