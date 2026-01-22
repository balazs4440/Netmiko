from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.133",
    "username": "bali",
    "password": "netmiko1234"
}

kapcsolat = ConnectHandler(**kapcsolo)

print(kapcsolat.find_prompt())
print(dir(kapcsolat))





