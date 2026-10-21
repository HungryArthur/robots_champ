import cv2
from ultralytics import YOLO

# Загружаем более легкую и быструю nano-модель для робота
model = YOLO("yolov8n.pt")

# Инициализируем видеопоток с камеры
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
  print("Не удалось подключиться к камере")
  exit()

while cap.isOpened():
  ret, frame = cap.read(
     
  )
  if not ret:
    break

  # Инференс в режиме стрима для экономии памяти
  results = model.predict(frame, stream=True, verbose=False)

  for r in results:
    # Получаем отрисованный кадр с рамками
    annotated_frame = r.plot()

    # Здесь можно добавить логику управления роботом
    # Например: анализировать координаты r.boxes и отправлять команды на Arduino/ESP32

    cv2.imshow("Robot Vision", annotated_frame)

  # Нажмите 'q' для выхода
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()