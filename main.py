import requests,os
os.system("title Username Checker Maker")
checktype = input(" > What Will This Check Usernames For? \n > ")
siteformat = input(" > Please give the site format as if the username was 'memes'\n > Example: https://www.instagram.com/memes/ \n > ")
takenname = input(" > Name on the site that IS taken?\n > ")
nottakenname = input(" > Name on the site that ISN'T taken?\n > ")


taken = siteformat.replace("memes",takenname)
nottaken = siteformat.replace("memes",nottakenname)

takenstatus = requests.get(taken).status_code
nottakenstatus = requests.get(nottaken).status_code
finalsiteformat = siteformat.replace("memes","{line.strip()}")
print(f" > {takenstatus} \n > {nottakenstatus}")
if takenstatus == nottakenstatus:
	input(f" > Site returns {takenstatus} For both taken and non taken usernames. Sorry, this won't be possible :(")
	exit(0)
f = open(f"{checktype} username checker.py", "a")




f.write("""
from colorama import Fore, init, Style
import requests,os,threading, time

init(convert = True)
print(Fore.CYAN) 
filepath = input(f"[!] Write the name of the text file containing all names - eg 'usernames.txt'\\n[!] ")
amount = int(0)
valid = int(0)
invalid = int(0)

def my_function(line):
	global amount
	global valid
	global invalid """)
f.write("""
	abc = requests.get(f""")
f.write(f""""{finalsiteformat}").status_code 

	if abc == {takenstatus}:""")
f.write("""
		print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {Fore.RED}{line.strip()}")
		invalid = invalid + 1
""")
f.write(f"""
	elif abc == {nottakenstatus}: """)
f.write("""
		print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}{line.strip()}")
		valid = valid + 1
		f = open("valid.txt", "a")
		f.write(line)
		f.close()
	else:
		print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] {Fore.RED}{line.strip()} - ERROR")
		invalid = invalid + 1
	amount = amount + 1
	os.system(f"title Username Checker // Checked {amount} Out of {totalamount} - UNTAKEN : {valid} // TAKEN : {invalid}")


with open(filepath) as f:
    for i, l in enumerate(f):
        pass
totalamount = i + 1
""") #had some errors so just split it 
f.write("""
with open(filepath, 'r') as f:
    for line in f.readlines():   
        threading.Thread(target = my_function, args = (line,)).start() 
        time.sleep(0.1) 
""")

f.close()
