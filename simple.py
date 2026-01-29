from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}

kapcsolat = ConnectHandler(**kapcsolo)

print(kapcsolat.find_prompt())
print(dir(kapcsolat))





