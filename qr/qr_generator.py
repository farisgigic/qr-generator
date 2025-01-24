import os
import subprocess
import qrcode

def get_wifi_details():
    try:
        # Using "subprocess" we are accessing our network details
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True)
        ssid = None
        for line in result.stdout.split("\n"):
            if "SSID" in line and "BSSID" not in line:
                ssid = line.split(":")[1].strip()
                break

        # Get the Wi-Fi password
        result = subprocess.run(["netsh", "wlan", "show", "profile", ssid, "key=clear"], capture_output=True, text=True)
        print(result.stdout)
        password = None
        for line in result.stdout.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break

        return ssid, password
    except:
        return None, None

def create_qr_code(ssid, password):
    if not ssid or not password:
        print("Could not retrieve Wi-Fi details. :( ")
        return

    # Generate the Wi-Fi QR code
    qr_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    img = qrcode.make(qr_data) # generating QR code based on our credentials
    os.makedirs("img", exist_ok=True)
    img.save(f"img/{ssid}.png")
    print(f"QR code saved as img/{ssid}.png")

def main():
    ssid, password = get_wifi_details()
    if ssid and password:
        print(f"Wi-Fi Network: {ssid}")
        print(f"Password: {password}")
        create_qr_code(ssid, password)
    else:
        print("Failed to get Wi-Fi details. Are you connected to a network?")

if __name__ == "__main__":
    main()
