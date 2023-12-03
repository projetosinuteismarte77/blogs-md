Enable Wake-On-LAN (wol) in the BIOS of your computer

By default Ubuntu was enabling wol once and then if you shut it down afterwards, you couldn't use wol, needing to set the command everytime on boot
```sh
sudo ethtool --change <your_ethernet_device> wol g
```
So using netplan, vim /etc/netplan/00-installer-config.yaml, you can simply add it:

```yaml
network:
  ethernets:
    <your_eth>:
      match:
        macaddress: <your_eth_macaddress (ifconfig displays it)>
      wakeonlan: true
      dhcp4: true
  version: 2

```
Now wol works everytime on boot
