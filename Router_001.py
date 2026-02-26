from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


try:
    with ConnectHandler(**kapcsolo) as kapcsolat:

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")