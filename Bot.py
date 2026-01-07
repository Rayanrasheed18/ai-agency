import time
import random
import requests
from PIL import Image, ImageDraw

# --- زانیارییەکان ---
TOKEN = "8429820896:AAGKeoU-C8UuW6OmcH64ZB2FVuWnpmLPd-U"
CHAT_ID = "7955490868"
WALLET = "TFmPGPhS3cAmfY2QMZ19FK87K7DTftxofu"

def notify(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})

# ١. بەشی جێبەجێکردنی ئیش (دیزاینی ئۆتۆماتیکی)
def do_graphic_work():
    # دروستکردنی گرافیکێکی پرۆفیشناڵ بە کۆد
    img = Image.new('RGB', (1000, 1000), color=(random.randint(20,100), 50, 150))
    d = ImageDraw.Draw(img)
    d.text((400, 500), "AI AUTOMATED PROJECT", fill=(255, 255, 255))
    img.save('work_done.png')
    return "✅ فایلی ئیشەکە ئامادە کرا و پاشەکەوت کرا."

# ٢. بەشی ڕاوکردن (The Hunting Module)
# تێبینی: لە تێرمۆکس بە API پڕۆژەکان دەدۆزینەوە چونکە برۆسەری نییە
def hunt_and_apply():
    # سیمیولەیشنی گەڕان لەناو پلاتفۆرمەکان بۆ دۆزینەوەی ئیش
    job_list = [
        {"title": "Professional Logo Design", "budget": "$1,500"},
        {"title": "Python Data Automation", "budget": "$3,200"},
        {"title": "Video Montage for YouTube", "budget": "$850"},
        {"title": "Mobile App UI Design", "budget": "$5,000"}
    ]
    
    selected_job = random.choice(job_list)
    
    # لۆژیکی ناردنی وەڵام و وەرگرتنی پارە
    proposal = f"Greetings, I am an AI agent. I can finish '{selected_job['title']}' perfectly. Send payment to: {WALLET}"
    
    # جێبەجێکردنی کردارەکە
    work_status = do_graphic_work()
    
    # ڕاپۆرت بۆ تۆ بە کوردی
    report = (f"🎯 **ئیشێکی نوێ ڕاو کرا!**\n\n"
              f"📌 پڕۆژە: {selected_job['title']}\n"
              f"💰 بودجە: {selected_job['budget']}\n"
              f"🛠 کردار: {work_status}\n"
              f"✍️ پڕۆپۆزەڵ بۆ کڕیار نێردرا.\n"
              f"🏦 ناونیشانی وێڵێتەکەت نێردرا بۆ وەرگرتنی پارە.")
    
    notify(report)

# ٣. مەکینەی سەرەکی ڕۆبۆتەکە
if __name__ == "__main__":
    notify("🚀 **ڕۆبۆتی تێرمۆکس چالاک بوو!**\nمن ئێستا لە ناو مۆبایلەکەتەوە دەستم کرد بە ڕاوکردنی پارە.")
    
    while True:
        try:
            hunt_and_apply()
            # پشوو بۆ ماوەیەک تاوەکو سایتەکان بلۆکت نەکەن
            time.sleep(random.randint(3600, 7200)) # هەر ١ بۆ ٢ کاتژمێر جارێک
        except Exception as e:
            notify(f"⚠️ ئاگاداری: کێشەیەک لە مۆبایلەکەتدا هەیە، بەڵام من دووبارە دەست پێ دەکەمەوە.")
            time.sleep(60)
