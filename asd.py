from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.219",
    "username": "balazs",
    "password": "sshP455"
}


def vlan(ssh):
    vlanok = ("vlan 10",
              "name Tanulo",
              "vlan 20",
              "name Oktato",
              "vlan 30",
              "name Pedagogus",
              "vlan 100",
              "name Ugyvitel"
             )
    ssh.send_config_set(vlanok)




try:
    with ConnectHandler(**login_adatok)as kapcsolat:
        vlan(kapcsolat)
        print(kapcsolat.send_command("sh vl br"))

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")


