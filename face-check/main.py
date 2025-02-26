import os

print("🚀 Hệ thống nhận diện khuôn mặt")
print("1️⃣ Quay video & lưu ảnh")
print("2️⃣ Mã hóa khuôn mặt")
print("3️⃣ Nhận diện khuôn mặt")
choice = input("Chọn chức năng (1, 2 hoặc 3): ")

if choice == "1":
    os.system("python scripts/capture_faces.py")
elif choice == "2":
    os.system("python scripts/encode_faces.py")
elif choice == "3":
    os.system("python scripts/recognize_faces.py")
else:
    print("❌ Lựa chọn không hợp lệ!")
