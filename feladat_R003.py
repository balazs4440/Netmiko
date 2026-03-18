from netmiko import ConnectHandler

Router = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


try:
    with ConnectHandler(**Router) as kapcsolat:
        uptime = input(kapcsolat.send_command("sh ver | inc uptime"))
        print(uptime)
        
        off = input(kapcsolat.send_command("sh ip in br | inc down"))
        print(off)
        
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")