# Mobile Forensics Tool

The Mobile Forensics Tool is a GUI-based application built with Python and `ttkbootstrap`. It leverages **ADB (Android Debug Bridge)** to extract forensic artifacts from Android devices in real-time. The tool provides access to device information, logs, app data, network status, and more, making it ideal for mobile forensics analysis and lawful investigations.

---

## Features

- **Device Info**
  - Connect device
  - Get system properties
  - Battery stats
  - CPU and memory info

- **App Management**
  - List installed user applications

- **Logs**
  - View live system logs (`logcat`)
  - Clear logs

- **File Management**
  - Push files to the device
  - Pull files from the device

- **Network**
  - View network interface configuration (IP address, interfaces)

- **Call & SMS Logs**
  - Retrieve call logs
  - Retrieve SMS logs
  - Extract app data by package name

- **Screen & Media**
  - Capture screenshots
  - Record screen video

- **Access & Shell**
  - Attempt to enable root access (`adb root`)
  - Open interactive ADB shell

---

## Prerequisites

### 1. Install ADB (Android Debug Bridge)

- Download from: https://developer.android.com/studio/releases/platform-tools
- Add the extracted platform-tools directory to your system’s `PATH`.

### 2. Python Dependencies

Install required libraries:

```bash
pip install ttkbootstrap
```
### 3. Enable USB Debugging on the Android Device

- Go to Settings > About phone > Tap 'Build number' 7 times
- Navigate to Developer Options and enable USB Debugging

---

## How to Use

1. **Clone or download this repository:**

   ```bash
   git clone https://github.com/your-username/mobile-forensics-tool.git
   cd mobile-forensics-tool
   ```

2. **Run the tool:**

   ```bash
   python mobileforensics.py
   ```

3. **Interact with the GUI:**

   - Use the tabs to navigate between features (`Device Info`, `Logs`, `Network`, etc.)
   - Click buttons to extract or view information
   - Output will be displayed in the main output window

## Use Cases

- Forensic analysis of Android devices
- Incident response investigations
- Data recovery and evidence extraction
- App behavior inspection

## Limitations

- Root access is not guaranteed and depends on the target device.
- Some files and app data may be inaccessible on non-rooted devices.
- SMS and call log access may be restricted on newer Android versions due to permission model changes.
- Some ADB features require device to be in unlocked bootloader state.

## Troubleshooting

- **Device shows "unauthorized" in `adb devices`:**  
  Reconnect device and accept the USB debugging prompt on the phone.

- **Device not listed:**  
  Check cable and USB mode (should be "File Transfer" or "Transferring files").

- **Restart ADB:**

  ```bash
  adb kill-server
  adb start-server
  ```
