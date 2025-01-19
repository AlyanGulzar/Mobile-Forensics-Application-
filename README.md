# **Mobile Forensics Application**  
The **Mobile Forensics Tool** is a GUI-based application designed to extract data from Android devices using **ADB (Android Debug Bridge)**. This tool provides information such as:  
- Installed apps  
- Social media apps  
- Battery status  
- Call logs  

It is particularly useful for **mobile forensics investigations**.

---

## **🚀 Features**
- **View Connected Devices**: Lists all connected Android devices.  
- **Installed Apps**: Displays all apps installed on the device.  
- **Social Media Apps**: Identifies and filters popular social media applications.  
- **Battery Status**: Shows the battery information of the device.  
- **Call Logs**: Extracts and displays detailed call logs.  

---

## **📋 Prerequisites**
To use this tool, ensure the following requirements are met:

### **1. Install Required Tools and Libraries**
#### **ADB (Android Debug Bridge)**
1. Install ADB on your computer. Follow [this guide](https://developer.android.com/studio/releases/platform-tools) to download and set up ADB.  
2. Ensure `adb` is added to your system's PATH for global use.

#### **Python Libraries**
1. Install `ttkbootstrap` for the GUI framework:  
   ```bash
   pip install ttkbootstrap
   ```

---

### **2. Enable USB Debugging on Your Mobile Device**
1. On your Android device, go to **Settings > About Phone**.  
2. Tap **Build Number** 7 times to enable **Developer Options**.  
3. Navigate to **Settings > Developer Options** and enable **USB Debugging**.  

---

### **3. Connect Your Device**
1. Use a USB cable to connect the device to your computer.  
2. Open a terminal or command prompt and run:  
   ```bash
   adb devices
   ```
3. If prompted on your device, allow **USB Debugging**. You should see your device listed as `"device"`.  

---

### **4. Run the Script**
1. Save the provided script to a `.py` file (e.g., `mobile_forensics.py`).  
2. Run the script:  
   ```bash
   python mobile_forensics.py
   ```
3. Interact with the GUI to extract data:  
   - **All Installed Apps**: Displays all installed apps on the connected device.  
   - **Social Media Apps**: Lists only popular social media applications.  
   - **Battery Status**: Fetches the current battery information.  
   - **Call Logs**: Displays call log details.  

---

### **5. Troubleshooting**
- **If `adb devices` shows the device as `"unauthorized"`:**  
  - Reconnect your device and accept the debugging prompt.  
- **If no devices are listed:**  
  - Verify the USB connection and ensure **USB Debugging** is enabled.  
  - Run the following commands:  
    ```bash
    adb kill-server
    adb start-server
    ```

---

### **6. Extracted Data**
- **Installed Apps**: Retrieved using the `adb shell pm list packages -3` command.  
- **Social Media Apps**: Filters installed apps based on specific package names.  
- **Battery Status**: Captures detailed battery statistics using `adb shell dumpsys battery`.  
- **Call Logs**: Queries the call log content provider with `adb shell content query`.  

---

## **📦 Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mobile-forensics.git
   cd mobile-forensics
   ```

2. Run the application:
   ```bash
   python mobile_forensics.py
   ```

---

## **⚠️ Instructions**
- Ensure that **ADB is installed and added to PATH** before running the tool.  
- The application will not function unless **USB Debugging is enabled** on the connected device.  
- Use this tool **only with proper authorization** and for educational or lawful purposes.  

---

## **📄 License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **🤝 Contributing**
We welcome contributions! To contribute:  
1. Fork the repository.  
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **👤 Author**  
**Your Name**  
- GitHub: [@your-username](https://github.com/your-username)  
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)  

---

## **⚠️ Disclaimer**  
This tool is for **educational purposes only**. Ensure you have explicit authorization before using it on any device.

---

Feel free to replace placeholders like `your-username` and `Your LinkedIn Profile` with your actual information! Let me know if you'd like further assistance!
