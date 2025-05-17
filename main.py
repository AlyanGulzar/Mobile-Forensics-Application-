import subprocess
import threading
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, Scrollbar, Frame, Text, simpledialog, Toplevel
import time

# Function to run ADB commands
def run_adb_command(command):
try:
return subprocess.check_output(command, shell=True).decode('utf-8', errors='ignore')
except subprocess.CalledProcessError as e:
messagebox.showerror("Error", f"Command failed: {e}")
return ""

# Get connected devices
def get_connected_devices():
output = run_adb_command("adb devices")
lines = output.strip().split('\n')[1:]
devices = [line.split('\t')[0] for line in lines if 'device' in line and not 'offline' in line]
return devices

# Connect device button handler
def connect_device():
devices = get_connected_devices()
if devices:
info_text.set(f"Connected Device(s): {', '.join(devices)}")
else:
messagebox.showerror("Error", "No connected devices found or devices are offline.")

# Show loading indicator
def show_loading():
loading_window = Toplevel(root)
loading_window.title("Loading")
loading_window.geometry("200x100")
loading_label = tb.Label(loading_window, text="Processing...", font=("Arial", 12))
loading_label.pack(pady=20)
loading_circle = tb.Progressbar(loading_window, mode='indeterminate', bootstyle='success')
loading_circle.pack(pady=10, fill='x', padx=10)
loading_circle.start()
return loading_window

# Hide loading indicator
def hide_loading(loading_window):
loading_window.destroy()

# Function to run ADB command in a thread
def run_command_in_thread(command, callback):
loading_window = show_loading()
time.sleep(1)  # Simulate processing time
output = run_adb_command(command)
hide_loading(loading_window)
callback(output)

# Display output in the text area
def display_output(output):
output_text.delete('1.0', 'end')  # Clear previous output
output_text.insert('1.0', output)  # Insert new output

# Device Info Functions
def display_device_info():
threading.Thread(target=run_command_in_thread, args=("adb shell getprop", display_output)).start()

def display_battery_status():
threading.Thread(target=run_command_in_thread, args=("adb shell dumpsys battery", display_output)).start()

def display_cpu_memory_info():
cpu_info = run_adb_command("adb shell cat /proc/cpuinfo")
mem_info = run_adb_command("adb shell cat /proc/meminfo")
display_output(f"CPU Info:\n{cpu_info}\n\nMemory Info:\n{mem_info}")

# App Management Functions
def display_installed_apps():
threading.Thread(target=run_command_in_thread, args=("adb shell pm list packages -3", display_output)).start()

# Logs Functions
def get_system_logs():
threading.Thread(target=run_command_in_thread, args=("adb logcat", display_output)).start()

def clear_logs():
run_adb_command("adb logcat -c")
messagebox.showinfo("Info", "Logs cleared.")

# File Management Functions
def push_file_to_device():
local_path = simpledialog.askstring("Input", "Enter local file path:")
remote_path = simpledialog.askstring("Input", "Enter remote file path:")
if local_path and remote_path:
threading.Thread(target=run_command_in_thread, args=(f"adb push {local_path} {remote_path}", display_output)).start()

def pull_file_from_device():
remote_path = simpledialog.askstring("Input", "Enter remote file path:")
local_path = simpledialog.askstring("Input", "Enter local file path:")
if remote_path and local_path:
threading.Thread(target=run_command_in_thread, args=(f"adb pull {remote_path} {local_path}", display_output)).start()

# Network Functions
def display_ip_address():
threading.Thread(target=run_command_in_thread, args=("adb shell ifconfig", display_output)).start()

# Call & SMS Logs Functions
def display_call_logs():
threading.Thread(target=run_command_in_thread, args=("adb shell content query --uri content://call_log/calls", display_output)).start()

def display_sms_logs():
threading.Thread(target=run_command_in_thread, args=("adb shell content query --uri content://sms/", display_output)).start()

# App Data Extraction
def pull_app_data():
package_name = simpledialog.askstring("Input", "Enter package name:")
if package_name:
threading.Thread(target=run_command_in_thread, args=(f"adb pull /data/data/{package_name}", display_output)).start()

# Screen & Media Functions
def take_screenshot():
threading.Thread(target=run_command_in_thread, args=("adb shell screencap -p /sdcard/screen.png", display_output)).start()

def record_screen():
threading.Thread(target=run_command_in_thread, args=("adb shell screenrecord /sdcard/video.mp4", display_output)).start()

# Access & Shell Functions
def enable_root():
threading.Thread(target=run_command_in_thread, args=("adb root", display_output)).start()

def open_shell():
threading.Thread(target=run_command_in_thread, args=("adb shell", display_output)).start()

# Initialize ttkbootstrap window
root = tb.Window(themename="cyborg")
root.title("Mobile Forensics Tool")

# Information Bar
info_text = tb.StringVar()

info_frame = tb.LabelFrame(root, text="Device and Network Info", padding=10, bootstyle=INFO)
info_frame.pack(padx=10, pady=10, fill="both", expand=True)
info_label = tb.Label(info_frame, textvariable=info_text, anchor="w", justify="left", font=("Arial", 10))
info_label.pack(fill="both", expand=True)

# Create a Notebook (tabs)
notebook = tb.Notebook(root)
notebook.pack(padx=10, pady=10, fill="both", expand=True)

# Create frames for each tab
tab_frames = {
"Device Info": tb.Frame(notebook),
"App Management": tb.Frame(notebook),
"Logs": tb.Frame(notebook),
"File Management": tb.Frame(notebook),
"Network": tb.Frame(notebook),
"Call & SMS Logs": tb.Frame(notebook),
"Screen & Media": tb.Frame(notebook),
"Access & Shell": tb.Frame(notebook)
}

# Add frames to the notebook
for tab_name, frame in tab_frames.items():
notebook.add(frame, text=tab_name)

# Device Info Tab
tb.Button(tab_frames["Device Info"], text="Connect Device", command=connect_device, bootstyle=INFO).pack(pady=5)
tb.Button(tab_frames["Device Info"], text="Display Device Info", command=display_device_info, bootstyle=INFO).pack(pady=5)
tb.Button(tab_frames["Device Info"], text="Display Battery Status", command=display_battery_status, bootstyle=WARNING).pack(pady=5)
tb.Button(tab_frames["Device Info"], text="Display CPU & Memory Info", command=display_cpu_memory_info, bootstyle=INFO).pack(pady=5)

# App Management Tab
tb.Button(tab_frames["App Management"], text="List Installed Apps", command=display_installed_apps, bootstyle=INFO).pack(pady=5)

# Logs Tab
tb.Button(tab_frames["Logs"], text="Get System Logs", command=get_system_logs, bootstyle=INFO).pack(pady=5)
tb.Button(tab_frames["Logs"], text="Clear Logs", command=clear_logs, bootstyle=DANGER).pack(pady=5)

# File Management Tab
tb.Button(tab_frames["File Management"], text="Push File to Device", command=push_file_to_device, bootstyle=INFO).pack(pady=5)
tb.Button(tab_frames["File Management"], text="Pull File from Device", command=pull_file_from_device, bootstyle=INFO).pack(pady=5)

# Network Tab
tb.Button(tab_frames["Network"], text="Get IP Address", command=display_ip_address, bootstyle=INFO).pack(pady=5)

# Call & SMS Logs Tab
tb.Button(tab_frames["Call & SMS Logs"], text="Get Call Logs", command=display_call_logs, bootstyle=INFO).pack(pady=5)
tb.Button(tab_frames["Call & SMS Logs"], text="Get SMS Logs", command=display_sms_logs, bootstyle=INFO).pack(pady=5)
tb.Button(tab_frames["Call & SMS Logs"], text="Pull App Data", command=pull_app_data, bootstyle=INFO).pack(pady=5)

# Screen & Media Tab
tb.Button(tab_frames["Screen & Media"], text="Take Screenshot", command=take_screenshot, bootstyle=INFO).pack(pady=5)
tb.Button(tab_frames["Screen & Media"], text="Record Screen", command=record_screen, bootstyle=INFO).pack(pady=5)

# Access & Shell Tab
tb.Button(tab_frames["Access & Shell"], text="Enable Root", command=enable_root, bootstyle=INFO).pack(pady=5)
tb.Button(tab_frames["Access & Shell"], text="Open Shell", command=open_shell, bootstyle=INFO).pack(pady=5)

# Text area for displaying output
output_text = Text(root, wrap='word', height=15)
output_text.pack(padx=10, pady=10, fill='both', expand=True)

# Run the main GUI loop
root.mainloop()"
