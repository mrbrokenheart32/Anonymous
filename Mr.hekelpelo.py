import os
print("=====================??=====================")
print("Metasploit Framework Console Installer ")
print("=====================??=====================")
print("""
1).Install Metasploit Framework Console [ Android 7.0 ] 
2).Install Metasploit Framework Console [ Android 5.0 ]
3).About Us
4).Quit From This Tools
""")
code = raw_input("Please Choose : ")
if code == "1":
	print("Are You Sure Want To Install Metasploit Framework Console??")
	code = raw_input("[ Y/N ] :")
	if code == "y":
		os.system("apt update && apt upgrade && pkg install unstable-repo && pkg install metasploit")
		print("Now You Can Run Metasploit Framework Console By Typing msfconsole")
elif code == "2":
	print("Are You Sure Want To Install Metasploit Framework Console??")
	code == raw_input("[ Y/N ] : ")
	if code == "y":
		os.system("apt update && apt upgrade -y && apt install git curl wget nano -y && curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz && gunzip metasploit_5.0.65-1_all.deb.gz && dpkg -i metasploit_5.0.65-1_all.deb && apt install -f && apt --fix-broken install")
		print("Now You Can Run Metasploit Framework Console By Typing msfconsole")
elif code == "3":
	print("This Tools Is Created By MR.BR0K3NH34RT,u0_a117 and Rio_Vatar")
else:
	print("")