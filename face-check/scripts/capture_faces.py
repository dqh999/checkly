import cv2
import os

# Cấu hình
NAME = "hop_do_quang"  # Đổi thành tên bạn
SAVE_PATH = f"dataset/known_faces/{NAME}"
os.makedirs(SAVE_PATH, exist_ok=True)

video_capture = cv2.VideoCapture(0)  # Mở camera
count = 0

print("🎥 Đang quay video, nhấn 'q' để thoát...")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    cv2.imshow("Video Capture", frame)

    # Chụp ảnh tự động sau mỗi 20 frame (~1 giây)
    if count % 20 == 0:
        img_path = os.path.join(SAVE_PATH, f"{NAME}_{count//20}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"📸 Lưu ảnh: {img_path}")

    count += 1

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
print("✅ Đã lưu ảnh từ video.")
