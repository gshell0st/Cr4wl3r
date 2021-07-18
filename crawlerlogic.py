#! This code was maked with python 3.8.5-64bit
#! This code was maked by GsHell0ST

#=-=-=-=-=-=-=-=-=-=-LIBS=-=-=-=-=-=-=-=-=
import subprocess
import requests
from time import sleep
import optparse
from colorama import init, Fore
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("--sC", "--crawler", dest="simpli", help="Go to scanner Option")
	(options, arguments) = parser.parse_args()

	if not options.simpli:
		parser.error("[x] Please specify the option, use --help for more info [x]")
        
	return options

def esp():
    print(' ')
    sleep(1)
def apar():
    print(Fore.LIGHTYELLOW_EX+'''
                     ______     __ __          _______     
                    / ____/____/ // /_      __/ /__  /_____
                   / /   / ___/ // /| | /| / / / /_ </ ___/
                  / /___/ /  /__  __/ |/ |/ / /___/ / /    
                  \____/_/     /_/  |__/|__/_//____/_/     
                                        
                    [!] ~ Develope by GsHell0ST ~ [!]

             ''')

def request(url): # Here is the place when the request happend
    try:
        return requests.get('https://' + url)

    except requests.exceptions.ConnectionError:
        return print('[X] ERROR, the url is not found [X]')
        pass

def simpli(target_url): # In this line is simplify mode, so in this function, is not going to show on screen de bad request
    subprocess.call('clear') # in this line, i call a linux command to clear the screen
    esp()

    wordlist = input('[!] Put here the path file of the wordlist [!] : ')
    if wordlist == '':
        esp()
        with open('/home/gshell0st/Documentos/V4L-D1R/wordlist/dirb/common.txt', 'r') as wordlist_file:
                for line in wordlist_file:                 # In this for          |
                    word = line.strip()                    # is the logic of      |
                    test_url = target_url + '/' + word     # the wordlist process |
                    response = request(test_url)           # only                 |

                    if response:
                        print('[+] Directory found! ---> ' + test_url + ' [+]')
                        esp()
                    else:
                        pass
    else:
        esp()
        with open(wordlist, 'r') as wordlist_file: # The file path of the wordlist / exemple: '/home/gshell0st/Documentos/V4L-D1R/wordlist/directory.txt'
                for line in wordlist_file:
                    word = line.strip()
                    test_url = target_url + '/' + word
                    response = request(test_url)

                    if response:
                        print('[+] Directory found! ---> ' + test_url + ' [+]')
                        esp()
                    else:
                        pass

def recursive(): # this function is about a recursive mode, so this def shows everithing about the process
    subprocess.call('clear')
    esp()

    target_url = input('[!] Put here a target [!] : ')
    wordlist = input('[!] Put here the path file of the wordlist [!] : ')
    if wordlist == '': # here i make te logic of wordlist, so if the user dosent input anything the code go direct to default wordlist
        esp()
        print('[!] Using the default wordlist : /home/gshell0st/Documentos/V4L-D1R/wordlist/directory.txt [!]')
        esp()
        with open('/home/gshell0st/Documentos/V4L-D1R/wordlist/directory.txt', 'r') as wordlist_file: # The file path of the wordlist
            for line in wordlist_file:               # In this for          |
                word = line.strip()                  # is the logic of      |
                test_url = target_url + '/' + word   # the wordlist process |
                response = request(test_url)         # only                 |
                if response:
                    print('[+] Directory found! ---> ' + test_url + ' [+]') 
                    esp()
                else:
                    print(f'[-] ERROR, Directory not found ---> {test_url} [-]')
                    esp()
    else: # here is the other answer, so here if in output have something, this code is running
        esp()

        with open(wordlist, 'r') as wordlist_file:  # The file path of the wordlist
            for line in wordlist_file:              # In this for's logic        |
                word = line.strip()                 # is the                     | 
                test_url = target_url + '/' + word  # the wordlist process       |
                response = request(test_url)        # only                       |

                if response:
                    print('[+] Directory found! ---> ' + test_url + ' [+]')
                    esp()
                
                else:
                    print(f'[-] ERROR, Directory not found ---> {test_url} [-]')
                    esp()

options = get_arguments()
apar()
simpli(options.simpli)