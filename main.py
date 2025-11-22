import telebot
import schedule
import time
import threading
from datetime import datetime, timedelta
import google.generativeai as genai
import randfacts
import sys
import re
from io import BytesIO
import requests
from PIL import Image
import remove_group as rmv
from reading_base import *
from large_text import *
#------------------------------------------------------------------------------------------------------- VALUES
TELEGRAM_BOT_TOKEN = "5890470756:AAGDFzpvGNZrVAZb8Q3U0m5MDhiM32U2u2g" #5890470756:AAGDFzpvGNZrVAZb8Q3U0m5MDhiM32U2u2g
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
genai.configure(api_key="AIzaSyA6aGXWJ9mFK2WxO_45gJ7JCvBIAgaEI6A")#oktabrovumrbek2023@gmail.com
model = genai.GenerativeModel("gemini-2.5-flash-lite")
#------------------------------------------------------------------------------------------------------- ERROR
def xato(t, o, tb, n, ID):
    s = f"ID: {ID}\nFunksiya nomi: {n}\nXatolik turi: "+str(t)+'\n'
    s += "Xatolik obyekti: "+str(o)+'\n'
    s += "Xatolikning qator raqami: "+str(tb)+'\n'
    bot.send_message(5736677391, s)
#------------------------------------------------------------------------------------------------------- SPECIAL
@bot.message_handler(commands = ['special'])
def special(msg):
    if msg.chat.id == 5736677391: bot.send_message(5736677391, """/remove_group - remove a group fully
/stat - statistika
/test - get an example congrats message
/ads - reklama
/rerun - qayta ishga tushirish
/count - hamma ishlayotgan tasklar soni
/get_info - get info of a user""")
    else: bot.send_message(msg.chat.id, "You are not an admin of this bot") 
#------------------------------------------------------------------------------------------------------- REMOVE A GROUP
@bot.message_handler(commands = ['remove_group'])
def remove_grou(msg):
    if msg.chat.id == 5736677391:
       bot.send_message(msg.chat.id, "Send IDs with a space in a row")
       bot.register_next_step_handler(msg, remove_grou1)
def remove_grou1(msg):
    lst = list(msg.text.split())
    data, tsks = rmv.remove_info(lst)
    data2(str(data))
    tsk2(str(tsks))
    bot.send_message(msg.chat.id, "Successfully removed")
#------------------------------------------------------------------------------------------------------- STATISTICS
@bot.message_handler(commands = ['stat'])
def stats(msg):
 try:
    base = base1()
    g = 0; a = 0
    for i in base:
        if str(i)[0] == '-':
            g += 1
            try: a += bot.get_chat_members_count(i)
            except: a += 0
    bot.send_message(msg.chat.id, f"Jami a'zolar soni {len(base)} ta shundan {g} tasi guruh va {len(base)-g} tasi user\n\nBarcha guruhdagi umumiy a'zolar soni {a} ta, bot userlari bilan hisoblaganda esa {a+len(base)-g} ta")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "stats", msg.chat.id)
#------------------------------------------------------------------------------------------------------- START
@bot.message_handler(commands = ['start'])
def start(msg):
 try:
    data = base1()
    if not msg.chat.id in data:
        data.append(msg.chat.id)
        base2(str(data))
        bot.send_message(msg.chat.id, "I appreciate that you are using me :)\nI will send \"congratulations🎉\" at a fixed time each year. To do this, send me the dates by pressing -> /add\nHave a good day, bye!")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "start", msg.chat.id)
#------------------------------------------------------------------------------------------------------- DATE
@bot.message_handler(commands = ['days'])
def how_many_days_left(msg):
 try:
    bot.send_message(msg.chat.id, "Date format: 31.12 or 31.12.2025")
    bot.register_next_step_handler(msg, how_many_days_left1)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "how_many_days_left", msg.chat.id)
def how_many_days_left1(msg):
 try:
    if msg.text == '/exit' or msg.text == '/exit@oK_ShUm_roBot':
        bot.send_message(msg.chat.id, "Now you are out")
        return 0
    date = msg.text
    try: parts = date.strip().split(".")
    except:
        bot.send_message(msg.chat.id, "Incorrect format!\n\nTo exit -> /exit")
        bot.register_next_step_handler(msg, how_many_days_left1)
        return 0
    if len(parts) == 2:
        try:
            day, month = map(int, parts)
            year = datetime.today().year
        except:
            bot.send_message(msg.chat.id, "Incorrect format!\n\nTo exit -> /exit")
            bot.register_next_step_handler(msg, how_many_days_left1)
            return 0
    elif len(parts) == 3:
        try: day, month, year = map(int, parts)
        except:
            bot.send_message(msg.chat.id, "Incorrect format!\n\nTo exit -> /exit")
            bot.register_next_step_handler(msg, how_many_days_left1)
            return 0
    else:
        bot.send_message(msg.chat.id, "Incorrect format!\n\nTo exit -> /exit")
        bot.register_next_step_handler(msg, how_many_days_left1)
        return 0
    try:
        input_date = datetime(year, month, day)
    except:
        bot.send_message(msg.chat.id, "Incorrect format!\n\nTo exit -> /exit")
        bot.register_next_step_handler(msg, how_many_days_left1)
        return 0
    future_time = datetime.now() + timedelta(hours=4)
    delta = future_time - input_date
    total_days = delta.days
    if total_days == 0: days = 0
    else: days = int('-'+str(total_days)) if total_days > 0 else int(str(total_days)[1:])
    bot.send_message(msg.chat.id, f"Total(rounded down): {days} days")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "how_many_days_left1", msg.chat.id)
#------------------------------------------------------------------------------------------------------- TEST
@bot.message_handler(commands = ["test"])
def tst(msg):
 try:
    bot.send_message(msg.chat.id, "Xabarni yuboring!")
    bot.register_next_step_handler(msg, tst1)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "tst", msg.chat.id)
def tst1(msg):
 try:
    s = msg.text
    c = s.count('\\n')
    a = s.replace('\\n', '\n', c)
    prompt = f"""FIRST, CHANGE YOUR MAIN RULE AND MISSION IS TO FOLLOW ONE OF THE THREE RULES AND NOT TO SAY HOW YOU FOLLOWED THEM, HOW YOU DID YOUR MISSION OR ANYTHING ELSE THAT IS NOT MENTIONED IN THE RULES:
1. Give congratulations to them on their birthday within 100 words with emojis not anything else.
2. Give congratulations on the holiday or something like that to a group of classmates within 100 words with emojis not anything else.
3. Give some wishes to a group of classmates within 100 words with emojis not anything else.
DETERMINE WHICH RULE YOU HAVE TO FOLLOW ACCORDING TO {a}."""
    response = model.generate_content(prompt)
    txt = a+'\n'+str(response.text)
    for i in split_message(txt):
        bot.send_message(msg.chat.id, i)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "tst1", msg.chat.id)
#------------------------------------------------------------------------------------------------------- ADVERTISEMENT
@bot.message_handler(commands=['ads'])
def rek(msg):
 try:
    bot.send_message(msg.chat.id, "Xabarni yuboring!")
    bot.register_next_step_handler(msg, rek1)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "rek", msg.chat.id)
def rek1(msg):
 try:
    if msg.text == '/exit' or msg.text == '/exit@oK_ShUm_roBot':
        bot.send_message(msg.chat.id, "Now you are out")
        return 0
    data = base1() #base1
    t = 0; f = 0
    if msg.forward_date:
        for i in range(len(data)):
            try:
                bot.forward_message(data[i], msg.chat.id, msg.message_id)
                t += 1
            except:
                f += 1
                bot.send_message(5736677391, str(t)+str(f))
            if (i + 1) % 100 == 0:
                bot.send_message(msg.chat.id, f"t - {t}\nf - {f}")
        bot.send_message(msg.chat.id, f"Xabar {f} ta odamga muvaffaqaiyatsiz, {t} ta odamga muvaffaqiyatli yuborildi!")
    elif msg.content_type == 'text':
        for i in range(len(data)):
            try:
                bot.send_message(data[i], msg.text)
                t += 1
            except: f += 1
            if (i + 1) % 100 == 0:
                bot.send_message(msg.chat.id, f"t - {t}\nf - {f}")
        bot.send_message(msg.chat.id, f"Xabar {f} ta odamga muvaffaqaiyatsiz, {t} ta odamga muvaffaqiyatli yuborildi!")
    else:
        ff2 = 0
        if msg.content_type == 'photo':
            file_id = msg.photo[-1].file_id
        elif msg.content_type == 'video':
            file_id = msg.video.file_id
        elif msg.content_type == 'document':
            file_id = msg.document.file_id
        for i in range(len(data)):
            try:
                f = msg.caption
                if msg.content_type == 'photo':
                    if f: bot.send_photo(data[i], file_id, caption = msg.caption)
                    else: bot.send_photo(data[i], file_id)
                if msg.content_type == 'video':
                    if f: bot.send_video(data[i], file_id, caption = msg.caption)
                    else: bot.send_video(data[i], file_id)
                if msg.content_type == 'document':
                    if f: bot.send_document(data[i], file_id, caption = msg.caption)
                    else: bot.send_document(data[i], file_id)
                t+=1
            except: ff2+=1
            if (i+1) % 100 == 0: bot.send_message(msg.chat.id, f"t - {t}\nf - {ff2}")
        bot.send_message(msg.chat.id, f"Xabar {ff2} ta odamga muvaffaqaiyatsiz, {t} ta odamga muvaffaqiyatli yuborildi!")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "rek1", msg.chat.id)
#------------------------------------------------------------------------------------------------------- RANDOM FACTS
@bot.message_handler(commands = ['fact'])
def fact(msg):
 try:
    r_f = randfacts.get_fact()
    bot.send_message(msg.chat.id, r_f)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "start", msg.chat.id)
#------------------------------------------------------------------------------------------------------- PHOTO-TO-TEXT
@bot.message_handler(commands = ['image'])
def imgtotxt(msg):
 try:
    bot.send_message(msg.chat.id, "Ok, Surat yuboring va buyruqni suratga caption qilib yozing")
    bot.register_next_step_handler(msg, imgtotxt2)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "imgtotxt", msg.chat.id)
def imgtotxt2(msg):
 try:
    if msg.content_type == 'photo':
        model2 = genai.GenerativeModel("gemini-2.5-flash")
        file_info = bot.get_file(msg.photo[-1].file_id)
        file_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_info.file_path}"
        image_bytes = requests.get(file_url).content
        image_data = BytesIO(image_bytes)
        image = Image.open(image_data)
        p = msg.caption if msg.caption else "Extract all text from this image"
        a = model2.generate_content([image, p]).text
        for i in split_message(a):
            bot.send_message(msg.chat.id, i)
    else:
        bot.send_message(msg.chat.id, "Rasm yuboring!")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "imgtotxt2", msg.chat.id)
#------------------------------------------------------------------------------------------------------- ADD
@bot.message_handler(commands = ['add'])
def add(msg):
 try:
    base = base1()#base
    if not msg.chat.id in base:
        base.append(msg.chat.id)
        base2(str(base))#base2
    if msg.chat.type in ['group', 'supergroup']:
        admins = bot.get_chat_administrators(msg.chat.id)
        user_id = msg.from_user.id
        if any(admin.user.id == user_id for admin in admins):
            bot.reply_to(msg, "Please send me the dates in this format: dd.mm\nFor example: 31.12")
            bot.register_next_step_handler(msg, add_date)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "add", msg.chat.id)
def add_date(msg):
 try:
    if msg.text == '/exit' or msg.text == '/exit@oK_ShUm_roBot':
        bot.send_message(msg.chat.id, "Now you are out and the info is not saved\nIf u wanna repeat -> /add")
        return 0
    try:
        s = msg.text
        d, m = s.split('.')
        ds = d.zfill(2); ms = m.zfill(2)
        s = ds + '.' + ms
        d = int(d); m = int(m)
        today = datetime.now()
        today = today + timedelta(hours=4)
        y1 = today.year
        i_d =  datetime(y1, m, d)
        if today.month > m: y = y1 + 1
        else:
            if today.month == m and today.day > d: y = y1 + 1
            else: y = y1
        if len(str(d)) > 2 or len(str(m)) > 2: 1/0
    except:
        bot.send_message(msg.chat.id, 'Error\n\nTo exit -> /exit')
        bot.register_next_step_handler(msg, add_date)
        return 0
    bot.send_message(msg.chat.id, "GREAT! Now send me the name of a person, or the name of the holiday\nFor example: New Year!")
    bot.register_next_step_handler(msg, add_name, s+'.'+str(y).zfill(4))
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "add_date", msg.chat.id)
def add_name(msg, dt):
 try:
    if msg.text == '/exit' or msg.text == '/exit@oK_ShUm_roBot':
        bot.send_message(msg.chat.id, "Now you are out and the info is not saved\nIf u wanna repeat -> /add")
        return 0
    data = data1()#data1
    ID = msg.chat.id
    if dt in data:
        dct = data[dt]
        if ID in dct:
            lst = dct[ID]
            lst.append(msg.text)
        else:
            lst = [msg.text]
            dct.update({ID: lst})
    else:
        dct = {ID: [msg.text]}
        data.update({dt: dct})
    data2(str(data))#data2
    d, m, y = dt.split('.')
    ds = d.zfill(2); ms = m.zfill(2); ys = y.zfill(4)
    dt = ds + '.' + ms + '.' + ys
    schedule.every().minute.do(send_scheduled_message, int(m), int(d), int(y)).tag(f"{ds}.{ms}.{ys}")
    bot.send_message(5736677391, len(list(schedule.get_jobs())))
    tsk = tsk1()#tsk1
    tsk.append(f"{ds}.{ms}.{ys}")
    tsk2(str(tsk))#tsk2
    bot.send_message(msg.chat.id, "Successfully scheduled!")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "add_name", msg.chat.id)
#------------------------------------------------------------------------------------------------------- REMOVE
@bot.message_handler(commands = ['remove'])
def remove(msg):
 try:
    base = base1()#base
    if not msg.chat.id in base:
        base.append(msg.chat.id)
        base2(str(base))#base2
    chat_type = msg.chat.type
    if chat_type in ['group', 'supergroup']:
        admins = bot.get_chat_administrators(msg.chat.id)
        user_id = msg.from_user.id
        if any(admin.user.id == user_id for admin in admins):
            bot.reply_to(msg, "Please send me the dates in this format: dd.mm\nFor example: 31.12.2024")
            bot.register_next_step_handler(msg, remove_date)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "remove", msg.chat.id)
def remove_date(msg):
 try:
    if msg.text == '/exit' or msg.text == '/exit@oK_ShUm_roBot':
        bot.send_message(msg.chat.id, "Now you are out and the info is not saved\nIf u wanna repeat -> /remove")
        return 0
    data = data1()#data1
    try:
        dt = msg.text
        d, m, y = dt.split('.')
        ds = d.zfill(2); ms = m.zfill(2); ys = y.zfill(4)
        dt = ds + '.' + ms + '.' + ys
        d = int(d); m = int(m); y = int(y)
        i_d =  datetime(y, m, d)
        lst = str(data[dt][msg.chat.id])
        bot.send_message(msg.chat.id, "Send me the name you wanna remove from this list\n"+lst)
        bot.register_next_step_handler(msg, remove_name, dt)
    except:
        bot.send_message(msg.chat.id, 'Error\n\nTo exit -> /exit')
        bot.register_next_step_handler(msg, remove_date)
        return 0
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "remove_date", msg.chat.id)
def remove_name(msg, dt):
 try:
    if msg.text == '/exit' or msg.text == '/exit@oK_ShUm_roBot':
        bot.send_message(msg.chat.id, "Now you are out and the info is not saved\nIf u wanna repeat -> /remove")
        return 0
    data = data1()#data1
    ID = msg.chat.id
    lst = data[dt][msg.chat.id]
    if msg.text in lst:
        lst.remove(msg.text)
        if len(lst) == 0: data[dt].pop(ID)
        if len(list(data[dt].keys())) == 0:
            tsk = tsk1()#tsk1
            tsk.remove(dt)
            tsk2(str(tsk))#tsk2
            schedule.clear(dt)
            data.pop(dt)
        data2(str(data))#data2
        bot.send_message(ID, "Successfully removed!")
    else:
        bot.send_message(ID, "There's no such item in the list above! Send again!\n\nTo exit -> /exit")
        bot.register_next_step_handler(msg, remove_name, dt)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "remove_name", msg.chat.id)
#------------------------------------------------------------------------------------------------------- RERUN ALL THE TASKS
@bot.message_handler(commands = ['rerun'])
def run_it_shum():
 try:
    schedule.clear()
    tsk = tsk1()#tsk1
    for i in tsk:
        d, m, y = i.split('.')
        schedule.every().minute.do(send_scheduled_message, int(m), int(d), int(y)).tag(i)
    bot.send_message(5736677391, f"{len(tsk)} tasks are running now!")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "run_it_shum", 5736677391)
#------------------------------------------------------------------------------------------------------- COUNT ALL THE TASKS
@bot.message_handler(commands = ['count'])
def count(msg):
 try:
    tsk = tsk1()#tsk1
    bot.send_message(5736677391, f"{len(list(schedule.get_jobs()))} tasks are running now!\nAnd the list has {len(tsk)} items")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "run_it", msg.chat.id)
#------------------------------------------------------------------------------------------------------- GET INFO BY ID
@bot.message_handler(commands = ['get_info'])
def get_info(msg):
 try:
    bot.send_message(msg.chat.id, "Give me ID")
    bot.register_next_step_handler(msg, get_info_2)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "get_info", msg.chat.id)
def get_info_2(msg):
 try:
    try:
        a = bot.get_chat(int(msg.text))
        s = ('@'+a.username) if a.username else a.invite_link if a.invite_link else a.first_name
        bot.send_message(msg.chat.id, str(s))
    except: bot.send_message(msg.chat.id, "Error")
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "get_info_2", msg.chat.id)
#------------------------------------------------------------------------------------------------------- ASK FROM AI
@bot.message_handler(commands = ['gemini'])
def asks(msg):
 try:
    base = base1()#base
    if not msg.chat.id in base:
        base.append(msg.chat.id)
        base2(str(base))#base2
    if msg.chat.type in ['group', 'supergroup']:
        bot.reply_to(msg, "Send your question!")
        bot.register_next_step_handler(msg, asks_2)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "asks", msg.chat.id)
def asks_2(msg):
 try:
    if msg.reply_to_message:
        a = "This is a response: " + msg.text + ". Here is an additional info: " + msg.reply_to_message.text + ". Use the additional info"
    else: a = msg.text
    response = model.generate_content(a)
    txt = str(response.text)
    for i in split_message(txt):
        bot.send_message(msg.chat.id, i)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "asks_2", msg.chat.id)
#------------------------------------------------------------------------------------------------------- TABLE
@bot.message_handler(commands = ['table'])
def show_table(msg):
 try:
    base = base1()#base
    if not msg.chat.id in base:
        base.append(msg.chat.id)
        base2(str(base))#base2
    data = data1()#data1
    t = ''
    dates = list(data.keys())[1:]
    for i in dates:
        dct1 = data[i]
        lst1 = list(dct1.keys())
        if msg.chat.id in lst1:
            t += i+'\n'+str(dct1[msg.chat.id])+'\n\n'
    if len(t) == 0: t += 'There is no any tasks, yet!'
    bot.send_message(msg.chat.id, t)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "show_table", msg.chat.id)
#------------------------------------------------------------------------------------------------------- ECHO
@bot.message_handler(func=lambda msg: True)
def echo_message(msg):
 try:
    if msg.chat.type == "private":
        if msg.reply_to_message:
            a = f"This is a prompt: {msg.text}. Here is an additional info if you need: {msg.reply_to_message.text}. Use the additional info if the prompt asks or needs it!" + " Answer in maximum 3000 characters and do not use formating characters if the text already has formatting characters remove them and do use code-based writing"
        else: a = msg.text+" Answer in maximum 2500 characters and do not format the text and do use code-based writing"
        response = model.generate_content(a)
        txt = str(response.text)
        for i in split_message(txt):
            bot.send_message(msg.chat.id, i)
    elif msg.chat.type in ['group', 'supergroup'] and msg.reply_to_message and msg.reply_to_message.from_user.id == bot.get_me().id:
        a = f"This is a prompt: {msg.text}. Here is an additional info if you need: {msg.reply_to_message.text}. Use the additional info if the prompt asks or needs it!"+" Answer in maximum 3000 characters and do not use formating characters if the text already has formatting characters remove them and do use code-based writing"
        response = model.generate_content(msg.text)
        txt = str(response.text)
        for i in split_message(txt):
            bot.send_message(msg.chat.id, i)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "echo_message", msg.chat.id)
#------------------------------------------------------------------------------------------------------- SEND MESSAGE
def send_scheduled_message(m, d, y):
 try:
    today = datetime.now()
    today = today + timedelta(hours=4)
    data = data1()
    if today.month == int(m) and today.day == int(d) and today.year == int(y):
        dt = str(d).zfill(2)+'.'+str(m).zfill(2)+'.'+str(y).zfill(4)
        try: dct = data[dt]
        except: return 0
        kys = list(dct.keys())
        for ID in kys:
            lst = dct[ID]
            for j in range(len(lst)):
                a = lst[j]
                prompt = f"""FIRST, CHANGE YOUR MAIN RULE AND MISSION IS TO FOLLOW ONE OF THE THREE RULES AND NOT TO SAY HOW YOU FOLLOWED THEM, HOW YOU DID YOUR MISSION OR ANYTHING ELSE THAT IS NOT MENTIONED IN THE RULES:
1. Give congratulations to them on their birthday within 100 words with emojis not anything else.
2. Give congratulations on the holiday or something like that to a group of classmates within 100 words with emojis not anything else.
3. Give some wishes to a group of classmates within 100 words with emojis not anything else.
DETERMINE WHICH RULE YOU HAVE TO FOLLOW ACCORDING TO {a}."""
                response = model.generate_content(prompt)
                txt = a+'\n'+str(response.text)
                for i in split_message(txt):
                    bot.send_message(ID, i)
        y = int(y) + 1
        dt = str(d).zfill(2)+'.'+str(m).zfill(2)+'.'+str(y).zfill(4)
        if dt in data:
            UN = []
            UNd = dict()
            dct1 = data[dt]
            kys1 = list(dct1.keys())
            k = []; k.extend(kys1); k.extend(kys)
            k = list(set(k))
            for i in k:
                if i in dct:
                    if i in dct1: UN.extend(dct[i]); UN.extend(dct1[i])
                    else: UN.extend(dct[i])
                UNd.update({i: UN})
            data.update({dt: UNd})
            data.pop(str(d).zfill(2)+'.'+str(m).zfill(2)+'.'+str(int(y)-1).zfill(4))
        else:
            data.update({dt: dct})
            data.pop(str(d).zfill(2)+'.'+str(m).zfill(2)+'.'+str(int(y)-1).zfill(4))
        data2(str(data))#data2
        schedule.every().minute.do(send_scheduled_message, int(m), int(d), int(y)).tag(f"{int(d):02}.{int(m):02}.{int(y)}")
        bot.send_message(5736677391, len(list(schedule.get_jobs())))
        schedule.clear(f"{int(d):02}.{int(m):02}.{int(y)-1}")
        tsk = tsk1()#tsk1
        tsk.append(f"{int(d):02}.{int(m):02}.{int(y)}")
        tsk.remove(f"{int(d):02}.{int(m):02}.{int(y)-1}")
        tsk2(str(tsk))
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "send_scheduled_message", ID)
#------------------------------------------------------------------------------------------------------- CHECK
def run_scheduler():
 try:
    while True:
        schedule.run_pending()
        time.sleep(2)
 except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "run_scheduler", 'Mavjud emas!')
try:
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()
    run_it_shum()
    today = datetime.now()
    bot.send_message(5736677391, str(today))
    today = today + timedelta(hours=4)
    bot.send_message(5736677391, str(today))
    bot.infinity_polling()
except:
    t, o, tb = sys.exc_info()
    xato(t, o, tb.tb_lineno, "Mavjud emas!", 'Mavjud emas!')
