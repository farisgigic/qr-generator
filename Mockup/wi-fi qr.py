import qrcode
import os


def load_saved_ssids(file_path="WiFi_list/wifi_list.txt"):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return file.read().splitlines()


def save_ssid_to_file(ssid, file_path="WiFi_list/wifi_list.txt"):
    with open(file_path, "a") as file:
        file.write(ssid + "\n")


def generate_wifi_qr(ssid, password, security_type="WPA", folder="img"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    wifi_data = f"WIFI:T:{security_type};S:{ssid};P:{password};;"
    img = qrcode.make(wifi_data)

    file_path = os.path.join(folder, f"{ssid}_wifi_qr.png")
    img.save(file_path)
    print(f"QR code for '{ssid}' saved as '{file_path}'.")


def main():
    saved_ssids = load_saved_ssids()
    print(f"Previously saved SSIDs: {saved_ssids}")

    ssid = input("Enter Wi-Fi SSID: ").strip()

    if ssid in saved_ssids:
        print(f"QR code for '{ssid}' already exists. No new QR code generated.")
    else:
        password = input("Enter Wi-Fi Password: ").strip()
        generate_wifi_qr(ssid, password)
        save_ssid_to_file(ssid)
        print(f"SSID '{ssid}' added to the list and QR code generated.")


if __name__ == "__main__":
    main()
