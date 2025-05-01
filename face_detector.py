import cv2

# Load the pre-trained Haar cascade face detector from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load the image (make sure 'test.jpg' is in the same directory as this script)
image = cv2.imread("test.jpg")

# Check if image is loaded properly
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert the image to grayscale for detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Check if faces were found
if len(faces) == 0:
    print("No faces found.")
else:
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the image with the detected faces
    cv2.imshow("Detected Faces", image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()
