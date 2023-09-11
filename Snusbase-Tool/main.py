import os
import json
import traceback
import datetime
import requests
import psutil
from colorama import Fore, Style
from urllib.request import Request, urlopen


#FULL BACK-END BY 7XWV:
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_directory(category):
    directory = f"./resource/{category}"
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

def save_error_log(error):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    log_directory = create_directory("logs")
    log_file = os.path.join(log_directory, f"error_{timestamp}.log")
    with open(log_file, "w") as file:
        file.write(str(error))

def handle_error():
    error = traceback.format_exc()
    print(Style.RESET_ALL + "Une erreur s'est produite. Veuillez consulter les logs pour plus de détails.")
    save_error_log(error)

snusbase_auth = 'sb0sl0hf866dmrtc4fkeatw7h8wlfo'
snusbase_api = 'https://api-experimental.snusbase.com/'

#API-COMBO:
def api_combo():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    class network_discord:
        def __init__(self):
            pass

        def search(self, term):
            f = requests.get(f"https://beta.snusbase.com/v2/combo/{term}")
            if f.status_code == 200:
                out = f.json()["result"]
                l = []
                for item in out:
                    for item2 in out[item]:
                        l.append(item2)
                        
                formatted_results = json.dumps(l, indent=2)  # Pretty print the results
                print("")
                print(formatted_results)
            else:
                print("La requête a échoué.")
    
    if __name__ == '__main__':

        term = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez n'importe quelle valeur : ")

        if term == "exit":
            exit()

        elif term == "menu":
            default_menu()

        else:
            search = network_discord()
            search.search(term)
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-IP WHOIS:
def api_ip_whois():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def api_whois(auth_token, ip):
        url = f"https://beta.snusbase.com/v1/whois/{ip}"
        headers = {
            "authorization": auth_token
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            print("")
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print("La requête a échoué.")

    if __name__ == "__main__":
        auth_token = "sb0sl0hf866dmrtc4fkeatw7h8wlfo"
        ip = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez l'adresse IP : ")

        api_whois(auth_token, ip)
        input("\nAppuyez sur Entrée pour continuer...")
        default_menu()

#-----------------------------------------------------------------

#API-EMAIL:
def api_email():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un adresse Email : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["email"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-USERNAME:
def api_username():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un Username : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["username"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)

            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-IP:
def api_ip():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un adresse Ip : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["lastip"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-HASH:
def api_hash():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un mot de passe Hash : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["hash"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-PASSWORD:
def api_password():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un mot de passe : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["password"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#API-NAME:
def api_name():
    clear_screen()
    text_default_fade = fade.greenblue(text_default)
    print(text_default_fade)
    
    def send_request(url, body=None):
        
        headers = {
            'Auth': snusbase_auth,
            'Content-Type': 'application/json',
        }
        method = 'POST' if body else 'GET'
        data = json.dumps(body) if body else None
        response = requests.request(method, snusbase_api + url, headers=headers, data=data)
        return response.json()

    if __name__ == "__main__":
        
        termz = input(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrer un Prenom & Nom avec un espace : ")

        if termz == "exit":
            exit()
        elif termz == "menu":
            default_menu()
        else:
        # Search Snusbase
            search_response = send_request('data/search', {
                'terms': [termz],
                'types': ["name"],
                'wildcard': False,
            })
            formatted_response = json.dumps(search_response, indent=2)
            print(formatted_response)
            
            input("\nAppuyez sur Entrée pour continuer...")
            default_menu()

#-----------------------------------------------------------------

#DEFAULT TEXT:
text_default = '''
    ...     ..      ..                                                                                                 
  x*8888x.:*8888: -"888:                                                                                    ..         
 X   48888X `8888H  8888                 u.    u.                                            .d``          @L          
X8x.  8888X  8888X  !888>       .u     x@88k u@88c.       u           .        .u            @8Ne.   .u   9888i   .dL  
X8888 X8888  88888   "*8%-   ud8888.  ^"8888""8888"    us888u.   .udR88N    ud8888.          %8888:u@88N  `Y888k:*888. 
'*888!X8888> X8888  xH8>   :888'8888.   8888  888R  .@88 "8888" <888'888k :888'8888.          `888I  888.   888E  888I 
  `?8 `8888  X888X X888>   d888 '88%"   8888  888R  9888  9888  9888 'Y"  d888 '88%"           888I  888I   888E  888I 
  -^  '888"  X888  8888>   8888.+"      8888  888R  9888  9888  9888      8888.+"              888I  888I   888E  888I 
   dx '88~x. !88~  8888>   8888L        8888  888R  9888  9888  9888      8888L         .    uW888L  888'   888E  888I 
 .8888Xf.888x:!    X888X.: '8888c. .+  "*88*" 8888" 9888  9888  ?8888u../ '8888c. .+  .@8c  '*88888Nu88P   x888N><888' 
:""888":~"888"     `888*"   "88888%      ""   'Y"   "888*""888"  "8888P'   "88888%   '%888" ~ '88888F`      "88"  888  
    "~'    "~        ""       "YP'                   ^Y"   ^Y'     "P'       "YP'      ^*      888 ^              88F  
                                                                                               *8E               98"   
                  ON DISCORD WKCC OR @NETWORK_UHQ ON TELEGRAM!                                '8>             ./"     
                                                                                                "             ~`'''

#MENU:
def default_menu():
    try:
        clear_screen()
        text_default_fade = fade.greenblue(text_default)
        print(text_default_fade)

        choose_text = '''(1) - Rechercher avec une Email.      /  (5) - Rechercher via un Password.
(2) - Rechercher avec un Username.    /  (6) - Rechercher avec un mot de passe Hash.
(3) - Rechercher via une Adresse Ip.  /  (7) - Rechercher avec Combo.
(4) - Whois une Adresse Ip.           /  (8) - Rechercher avec Prenom & Nom.
               (exit) for leave the app ! (by kzqx7 on discord)'''
        
        text_choose_fade = fade.purpleblue(choose_text)
        print(text_choose_fade)

        print(Style.RESET_ALL + "["+Fore.BLUE+"+"+Style.RESET_ALL+"] " + "Entrez votre choix (1-8) :")
        choice = input("> ")
        
        #API EMAIL:
        if choice == "1":
            api_email()

        #API USERNAME:
        if choice == "2":
            api_username()

        #API IP:
        elif choice == "3":
            api_ip()

        #API IP WHOIS:
        elif choice == "4":
            api_ip_whois()

        #API PASSWORD:
        elif choice == "5":
            api_password()

        #API HASH:
        elif choice == "6":
            api_hash()

        #API COMBO:
        elif choice == "7":
            api_combo()

        #API NAME:
        elif choice == "8":
            api_name()

        #EXIT:
        elif choice == "exit":
            clear_screen()
            exit()

        #ERREUR
        else:
            print("Choix invalide. Veuillez réessayer.")
            input("Appuyez sur une touche pour continuer...")
            default_menu()
            
    except Exception as e:
        handle_error()


if __name__ == "__main__":
    default_menu()
