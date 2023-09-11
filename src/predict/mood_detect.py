import cv2
import numpy as np

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'predict/haarcascade_frontalface_default.xml')

# Load the pre-trained emotion recognition model
emotion_model = cv2.dnn.readNetFromTensorflow('predict/fer2013_mini_XCEPTION.102-0.66.hdf5')

# Define emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Function to detect emotions from an image object
def detect_emotions(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    emotions = []
    
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        
        # Resize the face ROI for emotion recognition
        face_roi = cv2.resize(face_roi, (64, 64))
        face_roi = face_roi.astype('float') / 255.0
        face_roi = face_roi - 0.5
        face_roi = face_roi * 2.0
        
        # Prepare the input blob for the emotion recognition model
        blob = cv2.dnn.blobFromImage(face_roi, 1.0, (64, 64), (0, 0, 0), swapRB=True, crop=False)
        
        # Set the input blob for the model and perform forward pass
        emotion_model.setInput(blob)
        emotion_prediction = emotion_model.forward()
        
        # Get the emotion label with the highest confidence
        emotion_label = emotion_labels[emotion_prediction[0].argmax()]
        emotions.append(emotion_label)
    
    return emotions

# Example usage:
# Assuming 'image_object' is your image object (e.g., obtained from Django request.FILES)
# You can use image_object.read() to get the image bytes.
image_bytes = image_object.read()
image_array = np.frombuffer(image_bytes, np.uint8)
image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

moods = detect_emotions(image)
print("Detected emotions:", moods)
