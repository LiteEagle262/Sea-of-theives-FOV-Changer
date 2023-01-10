import ctypes, sys, psutil, traceback
from colorama import Fore, init
from time import sleep
from pyinjector import inject

init(convert=True)

ctypes.windll.kernel32.SetConsoleTitleW("Nest | SOT Fov Changer")

def getpid(name):
    for process in psutil.process_iter():
        try:
            if name == process.name():
                return(process.pid)
        except:
            return traceback.format_exc()

pid = getpid("SoTGame.exe")
if pid is None:
    print(Fore.RED + "Game not found")
    print(Fore.RED + "Please run the game before executing this.")
    sleep(3)
    sys.exit()

print(Fore.GREEN + """
    ████████╗██╗░░██╗███████╗  ███╗░░██╗███████╗░██████╗████████╗
    ╚══██╔══╝██║░░██║██╔════╝  ████╗░██║██╔════╝██╔════╝╚══██╔══╝
    ░░░██║░░░███████║█████╗░░  ██╔██╗██║█████╗░░╚█████╗░░░░██║░░░
    ░░░██║░░░██╔══██║██╔══╝░░  ██║╚████║██╔══╝░░░╚═══██╗░░░██║░░░
    ░░░██║░░░██║░░██║███████╗  ██║░╚███║███████╗██████╔╝░░░██║░░░
    ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░╚══╝╚══════╝╚═════╝░░░░╚═╝░░░
""")
print(Fore.YELLOW + "What client are you running?...")
client = input(Fore.YELLOW + "1 | Steam | 2 | Microsoft > ")
if client == "1":
    path = "dll/steam.dll"
    try:
        inject(pid, path)
        print(Fore.BLUE + "DLL Injected, This fov is adjustable, press the insert key on your keyboard to open the menu.")
    except:
        print(Fore.RED + "\nDLL Injection Failed")
        print(Fore.BLUE + "\nError:  ------------------------------------------------------")
        print(Fore.RED + traceback.format_exc())
        sleep(3)
        sys.exit()
elif client == "2":
    path = "dll/windows.dll"
    try:
        inject(pid, path)
        print(Fore.BLUE + "DLL Injected")
    except:
        print(Fore.RED + "\nDLL Injection Failed")
        print(Fore.BLUE + "\nError:  ------------------------------------------------------")
        print(Fore.RED + traceback.format_exc())
        sleep(3)
        sys.exit()
