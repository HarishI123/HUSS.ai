import cv2
from ultralytics import YOLO
import cvzone
import pyttsx3
import threading
from ipcam import cam  # Ensure this function retrieves frames from IP camera

# Initialize pyttsx3 for offline text-to-speech
engine = pyttsx3.init()

# Create a lock for thread safety
tts_lock = threading.Lock()

def play_sound(text):
    """Function to convert text to speech using pyttsx3."""
    with tts_lock:  # Ensure that only one thread can access the TTS engine at a time
        engine.say(text)
        engine.runAndWait()

def play_sound_async(text):
    """Run play_sound in a separate thread to avoid blocking."""
    thread = threading.Thread(target=play_sound, args=(text,))
    thread.start()

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# Load COCO class names
with open("coco.txt", "r") as f:
    class_names = f.read().splitlines()

# Load the YOLO model (using a small model for efficiency)
model = YOLO("yolo11s.pt")

# Set to store already spoken track IDs to avoid repeating
spoken_ids = set()
count = 0

while True:
    frame = cam()  # Capture frame from IP camera
    count += 1
    if count % 3 != 0:  # Skip frames to improve efficiency
        continue

    # Resize for processing
    frame = cv2.resize(frame, (1020, 500))

    # Run YOLO tracking
    results = model.track(frame, persist=True)

    if results[0].boxes is not None and results[0].boxes.id is not None:
        # Extract box, class, track ID, and confidence information
        boxes = results[0].boxes.xyxy.int().cpu().tolist()
        class_ids = results[0].boxes.cls.int().cpu().tolist()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        confidences = results[0].boxes.conf.cpu().tolist()
        
        current_frame_counter = {}

        for box, class_id, track_id, conf in zip(boxes, class_ids, track_ids, confidences):
            c = class_names[class_id]
            x1, y1, x2, y2 = box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cvzone.putTextRect(frame, f'{track_id}', (x1, y2), 1, 1)
            cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1)
            
            # Count only new detections
            if track_id not in spoken_ids:
                spoken_ids.add(track_id)

                if c not in current_frame_counter:
                    current_frame_counter[c] = 0
                current_frame_counter[c] += 1

        # Convert counts to speech for each class detected
        for class_name, obj_count in current_frame_counter.items():
            count_text = f"{obj_count} {class_name}" if obj_count > 1 else f"One {class_name}"
            play_sound_async(count_text)
        
        # Reset after each loop iteration
        current_frame_counter.clear()

    # Display the frame
    cv2.imshow("RGB", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
