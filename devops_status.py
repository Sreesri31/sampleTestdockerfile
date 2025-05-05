import platform
import socket
import shutil
import datetime

def check_system_info():
    print(" System Info:")
    print(f"Hostname     : {socket.gethostname()}")
    print(f"OS           : {platform.system()} {platform.release()}")
    print(f"Python Ver   : {platform.python_version()}")

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    print("\n Disk Usage (in GB):")
    print(f"Total: {total // (2**30)} GB")
    print(f"Used : {used // (2**30)} GB")
    print(f"Free : {free // (2**30)} GB")

def main():
    print(f" Checked at: {datetime.datetime.now()}\n")
    check_system_info()
    check_disk_space()

if __name__ == "__main__":
    main()
