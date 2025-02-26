import face_recognition
import cv2
import os
import pickle

KNOWN_FACES_DIR = "dataset/known_faces"
ENCODINGS_FILE = "encodings/face_encodings.pkl"

known_encodings = []
known_names = []

print("🔄 Đang mã hóa ảnh...")

for person in os.listdir(KNOWN_FACES_DIR):
    person_path = os.path.join(KNOWN_FACES_DIR, person)

    for filename in os.listdir(person_path):
        filepath = os.path.join(person_path, filename)

        image = face_recognition.load_image_file(filepath)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person)
            print(f"✅ Mã hóa thành công: {filename}")

with open(ENCODINGS_FILE, "wb") as f:
    pickle.dump({"encodings": known_encodings, "names": known_names}, f)

print("✅ Hoàn tất! Đã lưu vector khuôn mặt vào", ENCODINGS_FILE)
