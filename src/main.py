import os
import subprocess

def get_desktop_environment():
    try:
        desktop_session = os.environ.get("XDG_CURRENT_DESKTOP")
        if desktop_session:
            return desktop_session
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session:
            return desktop_session
        desktop_session = subprocess.getoutput("xprop -root _DT_SAVE_MODE")
        if " = \"xfce4\"" in desktop_session:
            return "XFCE"
    except:
        pass
    return "Unknown DE"

def get_window_manager():
    try:
        wm = subprocess.getoutput("xprop -root _NET_WM_NAME")
        wm = wm.split("=")[1].strip().replace("\"", "")
        return wm
    except:
        pass
    return "Unknown WM"

def fetch_info():
    username = os.getenv("USER")
    hostname = os.uname()[1]
    de = get_desktop_environment()
    wm = get_window_manager()

    print(f"{username}@{hostname}")
    print(f"Desktop Environment: {de}")
    print(f"Window Manager: {wm}")

if __name__ == "__main__":
    fetch_info()



