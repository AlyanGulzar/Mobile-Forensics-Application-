# Mobile Forensics Tool

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

## 🚀 Overview

The **Mobile Forensics Tool** is a GUI-based application designed to extract data from Android devices using ADB (Android Debug Bridge). This tool provides information such as installed apps, social media apps, battery status, and call logs, helping in mobile forensics investigations.

The GUI has been designed with a futuristic and modern look using the `ttkbootstrap` library.

---

## ✨ Features

- **Connected Devices**: Lists all connected Android devices.
- **Installed Apps**: Retrieves and displays all installed apps.
- **Social Media Apps**: Filters and displays popular social media apps.
- **Battery Status**: Shows detailed battery information.
- **Call Logs**: Extracts and displays call logs.

---

## 🛠️ Prerequisites

1. **Python 3.8+**: Install Python from [python.org](https://www.python.org/downloads/).
2. **ADB (Android Debug Bridge)**: 
   - Download the [Android SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools).
   - Add the `platform-tools` directory to your system's PATH.

   Verify installation:
   ```bash
   adb version
   ```
3. **ttkbootstrap**:
   - Install using pip:
     ```bash
     pip install ttkbootstrap
     ```

4. **Enable USB Debugging on Android Device**:
   - Go to **Settings > About Phone** and tap **Build Number** 7 times to enable Developer Options.
   - Navigate to **Settings > Developer Options** and enable **USB Debugging**.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mobile-forensics.git
   cd mobile-forensics
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python mobile_forensics.py
   ```

---

## 🖥️ Usage

1. Connect your Android device to your computer via USB.
2. Launch the tool by running the `mobile_forensics.py` script.
3. Use the buttons on the GUI to:
   - View connected devices.
   - Display all installed apps.
   - Display social media apps.
   - Get battery status.
   - View call logs.

---

## 🎨 Screenshots

### Main GUI
<img src="screenshots/main_gui.png" alt="Main GUI" width="600"/>

### Installed Apps
<img src="screenshots/installed_apps.png" alt="Installed Apps" width="600"/>

---

## 🛡️ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this project:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## 🧑‍💻 Author

**Your Name**  
- GitHub: [@your-username](https://github.com/your-username)  
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

---

## ⚠️ Disclaimer

This tool is intended for educational purposes only. Ensure you have proper authorization before using it on any device.

---

### Notes
1. Replace `your-username` with your GitHub username.
2. Add screenshots of the application in the `screenshots` directory and reference them in the README.
3. Customize the "Author" section with your details.

Let me know if you need help with uploading this to GitHub!
