import platform
import subprocess
import sys

def update_system() -> None:
    """
    Detect operating system and update.
    """
    os_name: str = platform.system()

    try:
        if os_name == "Linux":
            # Detectar la distribución de Linux
            with open("/etc/os-release") as f:
                os_info = f.read()
                if "Ubuntu" in os_info or "Debian" in os_info:
                    print("Updating system!")
                    subprocess.run(["sudo", "apt", "update"], check=True, stdout=sys.stdout, stderr=sys.stderr)
                    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True, stdout=sys.stdout, stderr=sys.stderr)
                elif "Fedora" in os_info or "RHEL" in os_info or "CentOS" in os_info:
                    print("Updating system!")
                    subprocess.run(["sudo", "dnf", "upgrade", "--refresh", "-y"], check=True, stdout=sys.stdout, stderr=sys.stderr)
                elif "openSUSE"  in os_info:
                    print("Updating system!")
                    subprocess.run(["sudo", "zypper", "up", "-y"], check=True, stdout=sys.stdout, stderr=sys.stderr)
                else:
                    print("Distro not supported!")
        elif os_name == "Darwin":
            print("Updating system!")
            subprocess.run(["softwareupdate", "--install", "--all"], check=True, stdout=sys.stdout, stderr=sys.stderr)
        elif os_name == "Windows":
            print("Updating system!")
            # For Windows, can use PowerShell for update
            subprocess.run(["powershell", "-Command", "Start-Process", "powershell", "-ArgumentList", "'-Command', 'Get-WindowsUpdate -Install -AcceptAll -AutoReboot'", "-Verb", "RunAs"], check=True)
        else:
            print("OS not Compatible")
    except subprocess.CalledProcessError as e:
        print(f"Error in command execution: {e}")
    except Exception as e:
        print(f"Error has ocurred: {e}")

if __name__ == "__main__":
    update_system()