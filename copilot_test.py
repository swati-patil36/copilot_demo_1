import os
import platform
import time

def get_uptime():
    # For Unix/Linux/Mac
    if platform.system() != "Windows":
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds
    # For Windows
    else:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        uptime_ms = kernel32.GetTickCount64()
        return uptime_ms / 1000.0

if __name__ == "__main__":
    uptime = get_uptime()
    print(f"System Uptime: {uptime:.2f} seconds")
