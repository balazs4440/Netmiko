from netmiko import ConnectHandler

Router = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


try:
    with ConnectHandler(**Router) as kapcsolat:
        uptime = (kapcsolat.send_command("sh ver | inc uptime"))
        cucc = uptime.split(" ")[-2:]
        print("Az eszköz", cucc,"ideje megy")
        
        off = (kapcsolat.send_command("sh ip in br | inc down"))
        print(off)
        
        küldeni=["interface loopback 100",
                "ip add 10.10.10.10 255.255.255.0",
                "no sh"]
        
        kapcsolat.send_config_set(küldeni)
        
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")