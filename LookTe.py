#!/usr/bin/python

#------- I LOVE PYTHON..Security(^-^) --------#

# SCRIPT INFO
#-----------#

#[1] SCRIPT: LookTe
#[2] Job: Scanning TARGET Website And Find All IPaddresses Of Servers Using this Website.
# And Find All Domains Of This Website.

#[3] Version: 1.0
#[4] Coded By: Oseid Aldary.

# Wait New Version Soooooon :)
## Add More Features And Options...Soooon :)

#~~~~~~~~~~Welcome~~~~~~~~~~#

# IMPORT LIBRARIES.
import requests,urllib,socket
from ast import literal_eval as d
from datetime import datetime
from time import sleep as se
import optparse
try:
   import dns.resolver
except:
	print("\033[1;37m[\033[1;33m!\033[1;37m] Please Install Requirements.txt:::Use\033[1;32m pip install -r requirements.txt")
	exit(1)
###############################

## SHow Time ##
###############
now = datetime.now()
H = now.hour
M = now.minute
S = now.second
timenow = "{}:{}:{}".format(H,M,S)
##################################

## Check Internet Connection
server = "www.google.com"
def check():
  try:
     IP = socket.gethostbyname(server)
     con = socket.create_connection((IP, 80), 2)
     return True
  except:
	pass
  return False
CHECKNET = check()
##############

## Output Options:
parse = optparse.OptionParser("""
Usage:
------
     python ./SpyEye.py [OPTIONS...]

OPTIONS:
--------
       -T --TARGET     <Set TARGET Website Or IP>
       -1 --DOMAINF    <Use This Option For Scan All Domains Of The TARGET>
       -2 --IPs        <Use This Option For Find all TARGET IPaddresses Of Servers>

EXAMPLES:
---------
./SpyEye.py -T www.google.com -1 ::> So This Command Scan For All Domains Of Google

./SpyEye.py -T www.google.com -2 ::> This Command Scan For All IPaddresses Of Google Servers

""",version="1.0")
####

# Cteate Main Function
def Main():

# Create Options
  parse.add_option("-T","-t","--TARGET","--target",dest="TARGET",type="string")
  parse.add_option("-1","--DOMAINSF","--domainsf",action="store_true",dest="DOMAINS",default=False)
  parse.add_option("-2","--IPs",action="store_true",dest="IPS",default=False)
  (options,args) = parse.parse_args()

## Start...:)

  if options.TARGET !=None and options.DOMAINS:
	TARGET = options.TARGET
        ## Check Target If Exist:
        if CHECKNET == True:
         def checkTAR():
           try:
              if TARGET[:8] == "https://":
                 host = TARGET[8:]
              elif TARGET[:7] == "http://":
	         host = TARGET[7:]
              else:
                 host = TARGET
              IP = socket.gethostbyname(host)
              con = socket.create_connection((IP, 80), 2)
              return True
           except:
		 pass
           return False
         if checkTAR() == True:
                try:
		   user_agent = { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" }
                   url = "https://domains.yougetsignal.com/domains.php"
	           form = { "remoteAddress" : "{0}".format(TARGET), "key" : "" }
		   req = requests.post(url, headers=user_agent, data=form, timeout=15)
		   res = d(req.text)
		except KeyError:
		    print("\033[1;31m[\033[1;33m!\033[1;31m]\033[1;33m[\033[1;31mERROE\033[1;33m]\033[1;33m Something Went Wrong \033[1;31m!!!")
		    print("\033[1;31m[\033[1;33m!\033[1;31m]\033[1;33mDomain/IP Address is incorrect\033[1;31m !!!")
		    print("\033[1;31m[\033[1;33m!\033[1;31m]\033[1;32m Try Other Domains Format \033[1;36m(^-^)")
		    exit(1)
	        if res["status"] == "Success":
                 se(0.10)
		 print("\033[1;33m="*20+"\033[1;32m>\033[1;35m Config \033[1;32m<"+"\033[1;33m="*20)
                 se(0.10)
                 print("\033[0;32m[T]\033[1;37m TARGET          : \033[1;31m"+str(TARGET))
		 se(0.10)
		 print("\033[0;32m[S]\033[1;37m START At        : \033[1;34m"+str(timenow))
		 se(0.10)
		 print("\033[0;32m[R]\033[1;37m Results Method  : \033[1;33m"+res["resultsMethod"])
		 se(0.10)
		 print("\033[0;32m[D]\033[1;37m Domain Count    : \033[1;36m"+res["domainCount"])
		 se(0.60)
		 print("\n\n\033[1;36m[\033[1;31m+\033[1;36m]\033[1;32m Scanning TARGET\033[1;33m...\n")
		 se(1.1)
                 try:
		  for i in range(len(res["domainArray"])):
		    print("\033[0;34m[\033[1;34m+\033[0;34m] \033[1;31mDomain Reversed\033[1;33m[\033[1;32m{}\033[1;33m]\033[1;30m   :\033[1;35m {}".format(i+1, res["domainArray"][i][0]))
		    if not int(i) > 20:
			se(.1)
		 except KeyboardInterrupt:
			print("\033[1;33m[Ctrl+C]\033[1;31mExitng....")
			se(1)
			print("\033[1;32mSee You Later (^-^)")
			exit(1)

		 print("\n\033[1;32m[*]\033[0;32m Shutdown At: \033[1;37m"+str(timenow))
		elif res["status"] == "Fail":
			if "Invalid remote address" in res["message"]:
			 print("\n\033[1;31m[!]\033[1;33m Something Went Wrong\033[1;31m !!!")
			 print("\033[1;31m[\033[0;31m!\033[1;31m]\033[1;33m Status: \033[1;37m"+res["status"])
			 print("\033[1;33m[\033[0;33m!\033[1;33m] "+res["message"])
			 print("\n~\033[1;37mTry using www. or remove http:// Or Try Other Domain Format\033[1;33m!")
			elif "check limit reached for" in res["message"]:
		         print("\n\033[1;31m[!]\033[1;33m Something Went Wrong\033[1;31m !!!")
                         print("\033[1;31m[\033[0;31m!\033[1;31m]\033[1;33m Status: \033[1;37m"+res["status"])
                         print("\033[1;33m[\033[0;33m!\033[1;33m] "+res["message"])
			 print("\n~\033[1;37m Try To Change Your IP Address\033[1;33m!")
			else:
                         print("\n\033[1;31m[!]\033[1;33m Something Went Wrong\033[1;31m !!!")
                         print("\033[1;31m[\033[0;31m!\033[1;31m]\033[1;33m Status: \033[1;37m"+res["status"])
                         print("\033[1;33m[\033[0;33m!\033[1;33m] "+res["message"])
         else:
	     print("\n\033[1;31m[!]\033[1;33m[ERROR:\033[1;34m 404\033[1;33m] Server Not Found Of[\033[1;34m{}\033[1;33m ]\033[1;31m !!!".format(TARGET))
	     exit(1)
        else:
	    print("\n\033[1;31m[!][\033[1;33mERROR\033[1;31m]\033[1;33m Please Check Your Internet Connection\033[1;31m !!!")
	    exit(1)


  elif options.TARGET !=None and options.IPS:
       target = options.TARGET
       if CHECKNET == True:
		def checker():
			try:
			   if target[:8] == "https://":
				host = target[8:]
			   elif target[:7] == "http://":
				host = target[7:]
			   else:
				host = target

			   ip = socket.gethostbyname(host)
			   run = socket.create_connection((ip, 80), 2)
			   return True
		        except:
			      pass
		        return False
	        if checker() == True:
                        if target[:8] == "https://":
                                host = target[8:]
                        elif target[:7] == "http://":
                                host = target[7:]
                        else:
                                host = target
			loop = 1
			se(0.10)
                        print("\033[1;33m="*20+"\033[1;32m>\033[1;35m Config \033[1;32m<"+"\033[1;33m="*20)
                        se(0.10)
                        print("\033[0;32m[T]\033[1;37m TARGET          : \033[1;31m"+str(target))
                        se(0.10)
                        print("\033[0;32m[S]\033[1;37m START At        : \033[1;34m"+str(timenow))
			se(0.60)
			print("\n\n\033[1;36m[\033[1;31m+\033[1;36m]\033[1;32m Scanning TARGET\033[1;33m...\n")
			se(1.5)
			print("\n\033[1;37m[\033[0;32m+\033[1;37m]\033[1;31m:\033[1;32mFound\n\033[1;33m------------------------------")
                        try:
			 for address_type in ['A', 'AAAA']:
	 			try:
		    		   answers = dns.resolver.query(host, address_type)
		    		   for rdata in answers:
				       print("\033[1;34m[\033[0;34m+\033[1;34m] \033[1;32mWebServer:[\033[1;33m{}\033[1;32m]\033[1;30m :\033[1;35m {}".format(loop,rdata))
				       loop +=1
				except dns.resolver.NoAnswer:
				     pass
			 resulit = loop -1
			 print("\n\n\033[1;32m[\033[0;32m+\033[1;32m]\033[1;37m This Target WebSite Has [\033[1;31m{}\033[1;37m] WebServer![:\033[1;33mStatus:[\033[1;32mUP\033[1;33m]".format(resulit))
			 print("\033[1;32m[*]\033[0;32m Shutdown At: \033[1;37m"+str(timenow))
			except KeyboardInterrupt:
                         print("\033[1;33m[Ctrl+C]\033[1;31mExitng....")
                         se(1)
                         print("\033[1;32mSee You Later (^-^)")
                         exit(1)
                else:
                    print("\n\033[1;31m[!]\033[1;33m[ERROR:\033[1;34m 404\033[1;33m] Server Not Found Of[\033[1;34m{}\033[1;33m ]\033[1;31m !!!".format(TARGET))
       else:
	   print("\n\033[1;31m[!][\033[1;33mERROR\033[1;31m]\033[1;33m Please Check Your Internet Connection\033[1;31m !!!")

  else:
	print(parse.usage)
	exit(1)

if __name__ == "__main__":
	Main()

##############################################################
##################### 		     #########################
#####################  END OF SCRIPT #########################
#####################                #########################
##############################################################
#This Script by Oseid Aldary
#Have a nice day :)
#GoodBye

