# **Underwater Plastic Detection Using YOLOv9**  
![Project Logo](Assets/Logo/logo.jpg)
A real-time underwater plastic detection system utilizing YOLOv9 and live video feeds from the IP Webcam app. This project aims to enhance marine conservation efforts by accurately identifying plastic waste in underwater environments.  

---

## **About the Project**  
Underwater plastic waste is a significant environmental issue impacting marine life and ecosystems. This project addresses this problem by leveraging advanced deep learning techniques for real-time detection of underwater plastic. The YOLOv9 model ensures high accuracy and efficiency, making it suitable for diverse underwater conditions.  

### **Key Features**  
- **Real-Time Detection**: Supports live video streaming via IP Webcam.  
- **High Accuracy**: YOLOv9-based model fine-tuned for underwater plastic detection.  
- **Customizable**: Easily modify configurations to adapt to different use cases and environments.  
- **Scalable Solution**: Deployable on various hardware platforms, including edge devices.  

---

## **Steps to Set Up the IP Webcam App**  

### **1. Download the App**  
Install the **IP Webcam** app from the Google Play Store on your mobile device.  

### **2. Launch the App**  
- Open the app on your phone and configure the settings.  
- Navigate to **Settings > Video Preferences** and adjust the resolution for optimal performance.  

### **3. Connect to the Same Wi-Fi Network**  
Ensure both your phone and computer are connected to the same Wi-Fi network for proper communication.  

### **4. Start the Stream**  
- Tap on **Start Server** within the IP Webcam app to begin streaming.  
- Note the IP address displayed at the bottom of the app (e.g., `http://192.168.0.101:8080`).  

---

## **Update IP Address in Code**  
Modify the `app.py` file to include the IP address of your IP Webcam stream:  

```python
cap = cv2.VideoCapture("http://192.168.0.101:8080/video")
```
## **Run the Application**  
Run the application using the following command:  

```bash
python app.py
```

---

## **License**  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

## **Acknowledgments**  
This project is inspired by ongoing research in marine conservation and deep learning for real-time object detection.  
