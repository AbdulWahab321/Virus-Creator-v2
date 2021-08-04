import os
import subprocess
import ctypes,sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
        subprocess.run(["powershell", "-Command",f"python runner.py"], capture_output=False)
else:
      # Re-run the program with admin rights
      ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,__file__, None, 1)

