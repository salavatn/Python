import subprocess

def get_wifi_networks():
    try:
        output = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"])
        return output.decode().splitlines()[1:]
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while getting Wi-Fi networks: {e}")

# Get Wi-Fi networks
networks = get_wifi_networks()

if networks:
    print("Available Wi-Fi Networks:")
    for network in networks:
        print(network)
else:
    print("No Wi-Fi networks found.")





