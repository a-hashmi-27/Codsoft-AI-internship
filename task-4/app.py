import cv2
import face_recognition
import os
import numpy as np

# Lists to store known face data
known_face_encodings = []
known_face_names = []

# Load all images from the "known_faces" folder
face_folder = "known_faces"
for filename in os.listdir(face_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(face_folder, filename)

        # Load the image file
        img = face_recognition.load_image_file(img_path)

        # Get the face encodings (assuming one face per image)
        face_encodings = face_recognition.face_encodings(img)
        if face_encodings:
            known_face_encodings.append(face_encodings[0])

            # Remove extension from filename to use as name
            name = os.path.splitext(filename)[0]
            known_face_names.append(name)
        else:
            print(f"Warning: No face found in {filename}")

# Start webcam feed
cap = cv2.VideoCapture(0)

print("Starting webcam. Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Skipping.")
        continue

    # Convert frame to RGB (face_recognition works with RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face locations and get encodings
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare current face with known ones
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.45)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

        name = "Unknown"

        if face_distances.any():  # Make sure there are known faces
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        # Draw rectangle and name on the frame
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the current frame
    cv2.imshow("Webcam Face Recognition", frame)

    # Break loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Webcam stopped.")

