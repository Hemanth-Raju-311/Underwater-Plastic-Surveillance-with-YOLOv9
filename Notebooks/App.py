import cv2
from ultralytics import YOLO
from tkinter import filedialog, Tk
import threading

# Initialize YOLOv9 with trained model weights
model = YOLO('best1.pt')  # Replace with the path to your trained model file

def detect_image(image_path):
    """Detects plastic waste in a given image."""
    image = cv2.imread(image_path)
    frame_resized = cv2.resize(image, (640, 640))  # Resize to model's input size
    results = model.predict(frame_resized, conf=0.2)  # Lower confidence threshold
    print("Detection Results:", results[0].boxes)  # Debug: Display detected boxes and scores
    annotated_image = results[0].plot()
    cv2.imshow("Detection Results", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_realtime():
    """Detects plastic waste in real-time using webcam."""
    cap = cv2.VideoCapture("http://100.64.64.17:8080/video")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_resized = cv2.resize(frame, (640, 640))
        results = model.predict(frame_resized, conf=0.2)  # Lower confidence threshold
        print("Real-Time Detection Results:", results[0].boxes)  # Debug: Display detections
        annotated_frame = results[0].plot()
        cv2.imshow("Plastic Waste Detection", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    """Main function to select detection mode."""
    print("Select an option:")
    print("1. Upload an image for detection")
    print("2. Real-time detection with webcam")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        root = Tk()
        root.withdraw()
        image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if image_path:
            detect_image(image_path)
        else:
            print("No image selected.")
    elif choice == '2':
        detect_realtime()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
