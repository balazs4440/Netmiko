from netmiko import ConnectHandler

Router = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


try:
    with ConnectHandler(**Router) as kapcsolat:

        neighbor = kapcsolat.send_command("sh ip ospf neig")
        neighbor = neighbor.strip().split("\n")[1:]
        
        print(len(neighbor),"szomszéd található a hálózaton.")
        
        
        
        
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")