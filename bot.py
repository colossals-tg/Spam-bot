# join @PythonPortalz for more tools
from telethon import TelegramClient, events
from telethon.tl.types import InputPeerUser
import asyncio
import random
import time
from typing import Dict, Optional
from dataclasses import dataclass
import os

SPAM_MESSAGES = {
    "hindi": [
    "Janta dukhi hai modi se, teri mummy ko uthne nahi dunga aaj apni godi se",
    "Lund loge lund¿?",
    "विराट कोहली के बल्ले का शॉट और तेरी मम्मी का पेटीकोट, दोनों एक Time पर ऊपर उठते ही हैं",
    "गोभी प्याज भिंडी आलू, क्या तेरी बहन को मैं पटालूं¿?",
    "तेरी मम्मी ने last time अपनी झाटे कब काटी थी...?🤗",
    "प्रशांत महासागर की गहराइयों में लेजाकर तेरी दीदी को चो*द दूंगा",
    "There's a word called WHORE, Your Mom Owns it",
    "1+1=3 (क्योंकि तेरी मम्मी को बिन condom के चो*द दिया था मैं)",
    "Teri mummy ko tajmahal ki नोक par bitha dunga",
    "Agar 1 se pehle 0 aata hai, to A se pehle cya aayega¿?",
    "Teri budhiya dadi mere bathroom me fisal gyi",
    "Teri mummy ko 73वीं hoor bana dunga rndike",
    "jannat me jaakr teri pardadi ko chod dunga",
    "Teri mummy ke muh pr apne lund se knock knock kr dunga",
    "Ek hota hai chutiya ek hota hai maha chutiya or teesra main hu jisne bina condom ke teri mummy chodne ki galti kr di",
    "Aadat se लचार hu, teri mummy ka purana भतार hu",
    "Kati patang tera kon sa rang... Jis rang ki teri behan ne panty pehni hogi wo wala rang",
    "Teri behan ki chut me चाकू 🔪 se fingering kar dunga abb",
    "चुप गरीबी रेखा में रेंगने वाले कीड़े🤫🥱",
    "muh band rakh napunsak ki awlaad",
    "Fruti ya pepsi, teri behan badi sexy",
    "Teri behan ka insta id milega cya😈😉¿?",
    "तू अपनी बहन को बोल न मुझे अपने जांघों के बीच दबा कर मार दे🙈",
    "Koi hota hai pagal, to koi banata hai khayali pulau, cya main teri didi ke boobs dabau?",
    "Sarkari school ke peeche lejakr teri didi ki salwar ka nada khol dunga",
    "Gali gali me rehta hai saand, teri mummy ko itna choda ki wo ban gyi Raand😁",
    "Teri maa 150 wali randi",
    "Jungle me naachta hai Morr, teri mummy ki chudayi dekhkar sb bolte hn once more once more",
    "Teri behan ki chut me kutte ka sperm",
    "Teri behan ki yaado me jee rha hu ab bss",
    "Teri mummy ki flipcart se order kar lunga",
    "Duniya paise laha rahi ghode pe, or teri mummy ghum fir kar aa jaati hai mere 🤭😈",
    "Teri mummy ko itna chodunga ki usko लकवा maar jayega",
    "Bura mat maniyo teri mummy ni chod sakta, apni wali ke liye loyal hu",
    "teri behan ki gand me top chala dunga",
    "Teri mummy ko momos khilakr chod dunga",
    "Move Theatre me teri behan ki panty me hath daal dunga",
    "kaise chudi teri maa¿?",
    "चुदले फेर🤗🤫",
    "Chudayi kar du aapni mummy ki??",
    "Teri behan ko geela kar diya maine",
    "Mere sexting se to tere ghar ki saari aurte khush hai",
    "Ronaldo ka football teri mummy ki gand ke chhed me ghusa dunga",
    "अंधेरे में rehne wala भूत और तेरी मम्मी की काली चूत, दोनों useless hai",
    "ये गरजने वाले बादल है ना ! शेर दहाड़ने wala घायल है ना !! और कहती है मेरे लंड पे मूतेगी, तेरी मम्मी भी कितनी पागल है ना ",
    "बच्चे रोते हैं मिठाई के लिए, और तेरी मम्मी के मुंह में पानी आता है मेरे लंड wale मलाई के लिए",
    "Teri behan ki chut me thanos ka glub",
    "Spiderman ki tarah diwar par latak kar teri mummy ki gand maar lunga",
    "Teri mummy ko superman wali laal chaddi pehna dunga",
    "Maine to sapne bhi teri behan ko chodne wale dekhe hn",
    "Shatap mere bete",
    "Aand bhaat khayega¿?",
    "teri mummy ko apna lwda-paaw khilata hu ruk",
    "Teri mummy ke 2 kaam~ pehla mere lund par baithkar mootna or dusra fir usi lund ko chusna",
    "Teri mummy ko bulu bulu kar du kya🥺🫣¿?",
    "tu apni behan ko meri godi me bitha de",
    "Teri maa chod di, teri behan pel daali, ab aayi teri nani ki baari",
    "teri mummy ki chut me Sidha lund se shot marunga to tera bhai hoga, Aada-Tedha shot maarunga to teri behan hogi, bata tujhe kyw chahiye",
    "Ter behan ko hentai dikha dunga",
    "Teri didi ke boobs chaba jaunga🫦",
    "Teri behan ki gori chut hai ya kaali¿?",
    "Teri mummy meri gulam",
    "Teri behan ki chut pe vimal thuk diya kisi ne¿?",
    "Abe tere or teri mummy ke jaiso ko lund par jhula du",
    "chup madarchod",
    "Jana lwde teri mummy ko chudne se bacha",
    "Teri behan ki pet me mera bachha",
    "Teri randi maa ko kitno ne choda¿?",
    "Teri mummy ke muh se apna zip khulwa lunga",
    "Teri behan bhi teri mummy ki tarah randi nikal gyi",
    "Teri mummy ko apne lund se jhula jhulwa dunga",
    "Tujhe, teri mummy ko, tere bane banaye ghar ke sath khareed lunga gareeb",
    "Teri didi ke sath sexting kr dunga",
    "Chut ka diwana main teri mummy ki chut ka diwana",
    "Your mom, My bitch, Otey¿?",
    "Teri mummy ki brownish chut pe apna paani giraunga",
    "Hawe hawe me teri mummy ko उछालते hue chod dunga",
    "Teri mummy ke sath lawandiyabaazi karu randi ke",
    "Teri mummy ki fati choot apne jhaato se seel dunga",
    "chup chudi hui raand ke bette",
    "Or bete kya haal",
    "Teri mummy ki chut me pura laat ghusa dunga",
    "Teri behan meri khelne wali gudiya ok?",
    "Teri behan ki teady bear dilakr chod dunga",
    "Teri didi ka WhatsApp number milega cya¿?",
    "Teri behan ke noods de to dekhkr delete kar dunga☠️🙈",
    "Just Imagine ki teri mummy ki gand me agar hathi ka lund chala jaaye to☠️😭",
    "Teri mummy mere ghar me kam karne wali baai",
    "Teri mummy ko sexually harass kar dunga😈👍🏻",
    "Teri mummy ko promise kiya hu ki use aaj bikni gift karunga",
    "Teri behan ki chut me captain america ka shield",
    "Teri behan kidnap ho gayi",
    "kutte ke muh me ghee or tu mera lund pee randike",
    "Andhere me teri didi chodkr bhaag jaunga",
    "Apni maa chuda lwde",
    "TERI MA CHUDD JAYEHI BCHEE MOCHI KE",
    "𝐂𝐏 𝐊𝐀𝐑𝐄𝐆𝐀 𝐓𝐄𝐑𝐈 𝐌𝐀. 𝐌𝐀𝐑𝐉𝐀𝐘𝐀 𝐆𝐈 𝐆𝐀𝐑𝐄𝐄𝐁𝐂𝐘𝐀 𝐌𝐀?",
    "OYE JHAATU 😒 LE YE SUN 👇👇▶︎ •၊၊၊|။||။‌‌‌‌‌၊|• 0:10________NHII CHLIII 🥲",
    "Ek chatt pe 7 kabootar🕊️ Saato kha gyi billi 🐈‍⬛😠 Teri mmy pair uthye Chomde puri Delhi 👄😈",
    "ऐसे तेरी चुदाई nhi rukegi",
    "तेरे माई के चूत मैं १०० हटीओ का लंड 🤪",
    "ना परचॉ लगता है ना खर्चा लगता है तेरी माँ को जब मर्ज़ी चोदू अच्छा लगता hai.",
    "Teryma ki shut pe प्रहार kru apne लुंड se ☠️💥☠️💥",
    "7 रंग के 7 कबूतर सातों  खा गई बिल्ली तेरी मम्मी तांग उठाये चोदे पूरा दिल्ली ♨️♨️😋👑🍷😂😂",
    "Abe oy bengaliyo pr 1 shabd nhi sunuga me ruk tere papa ko call kru",
    "Teri maa ki chut mai deadlift mardunga",
    "Teri behen ko aeroplane mai betha ke chodunga",
    "Teri maa ko satellite pe chodu space mai new experience 🤣🤣🤣🤣🌌🌌🌌🌌🌌🌌",
    "Teri maa ko asthetic way mai chodunga",
    "roj khaata mai burger teri maa q daily chudwane jaati hai Ghar ghar?",
    "तेरी माँ रंगबिरंगी रंडी ❤️🧡💛🩷💚🩵💙💜",
    "Oye Teri maa ke bhosde mai pathhar daldunga",
    "Muh pe asa lund mrunga chud chudke pagal hojyga Oye Teri maa ke bhosde mai pathhar daldunga",
    "Teri maa ko chodkr chat se latka ke maar dalunga",
    "तेरी मां को स्वतंत्रता दिवस में झंडा लगाके चोद लूंगा ok na",
    "oye mukke maru tere ma k mu prr",
    "teri ma rndy k mu pr lawda maru",
    "Reacted लंड लेले to your message",
    "a guy gave me wise advice ignore kro jaise mai krta hu coz vo randike bachhe hai so imma apply that on you.",
    "Badle ki aag mein teri maa iss kadar joojh gayi Khaake mirch ka pakoda mera lund choos gayi",
    "Ary...sal😂😂😂 huahh betichodke  🫵😏 thare pichwade🍑 mese 💨 nikal jayego🤣😭kati baham parle o beta 😂😆",
    "Beta aaise chudega ya fir waise??Teri maa ch√de rafta rafta ya fir slowly slowly?"
 ]
}

@dataclass
class SpamTarget:
    user_id: int
    chat_id: int
    count: int
    active: bool
    reply_spam: bool = False

@dataclass
class RaidTarget:
    user_id: int
    chat_id: int
    active: bool

class SpamBot:
    def __init__(self, api_id: str, api_hash: str, owner_id: int):
        self.client = TelegramClient('session_name', api_id, api_hash)
        self.owner_id = owner_id
        self.spam_targets: Dict[int, SpamTarget] = {}
        self.raid_targets: Dict[int, RaidTarget] = {}
        self.spam_tasks: Dict[int, asyncio.Task] = {}

    async def send_spam(self, chat_id: int, user_id: int, count: int):
        try:
            user = await self.client.get_entity(user_id)
            username = f"@{user.username}" if user.username else f"User {user_id}"
            for _ in range(count):
                message = random.choice(SPAM_MESSAGES['hindi'])
                await self.client.send_message(chat_id, f"{username} {message}", reply_to=user_id)
                await asyncio.sleep(random.uniform(0.5, 1.5))
        except Exception as e:
            print(f"Error in send_spam: {str(e)}")

    async def raid_spam(self, user_id: int, chat_id: int):
        try:
            user = await self.client.get_entity(user_id)
            username = f"@{user.username}" if user.username else f"User {user_id}"
            while self.raid_targets.get(user_id, RaidTarget(user_id, chat_id, False)).active:
                message = random.choice(SPAM_MESSAGES['hindi'])
                await self.client.send_message(chat_id, f"{username} {message}")
                await asyncio.sleep(random.uniform(2, 3))
        except Exception as e:
            print(f"Error in raid_spam: {str(e)}")

    async def handle_message(self, event):
        if event.sender_id != self.owner_id:
            return

        text = event.message.text.strip()
        chat_id = event.chat_id
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.sender_id if reply_msg else None

        try:
            await event.delete()
        except:
            pass

        if text == ".help":
            help_text = """📚 **Available Commands:**

🔹 **.spam <number>** - Spam random messages <number> times in current chat.
🔹 **.spam <number>** (reply to user) - Spam <number> times replying to the user.
🔹 **.rspam** (reply to user) - Auto-spam reply when the user sends a message or mentions you in the same chat.
🔹 **.slist** - List all active spam targets.
🔹 **.soff <username or ID>** (or reply to user) - Stop spamming a specific user.
🔹 **.offg** - Stop all active spam and raid tasks.
🔹 **.chudab <username or ID>** (or reply to user) - Start continuous raid spam on a user every 2-3 seconds.
🔹 **.roff <username or ID>** (or reply to user) - Stop raid spam for a specific user.
🔹 **.info** (reply to user) - Get user info (ID, username, name)."""
            await event.respond(help_text)
            return

        elif text.startswith(".spam"):
            parts = text.split()
            if len(parts) < 2 and not reply_msg:
                await event.respond("❌ Usage: .spam <number> or reply to a user with .spam <number>")
                return

            try:
                count = int(parts[1]) if len(parts) > 1 else 10
                if count <= 0:
                    raise ValueError
            except ValueError:
                await event.respond("❌ Invalid number for spam count")
                return

            if reply_msg:
                user_id = reply_msg.sender_id
                self.spam_targets[user_id] = SpamTarget(user_id, chat_id, count, True)
                await event.respond(f"✅ Spamming {count} messages to User {user_id}")
                await self.send_spam(chat_id, user_id, count)
                self.spam_targets[user_id].active = False
            else:
                for _ in range(count):
                    message = random.choice(SPAM_MESSAGES['hindi'])
                    await self.client.send_message(chat_id, message)
                    await asyncio.sleep(random.uniform(0.5, 1.5))
                await event.respond(f"✅ Spammed {count} messages in this chat")

        elif text == ".rspam" and reply_msg:
            user_id = reply_msg.sender_id
            self.spam_targets[user_id] = SpamTarget(user_id, chat_id, 0, True, reply_spam=True)
            await event.respond(f"✅ Auto-reply spam enabled for User {user_id} in this chat")

        elif text == ".slist":
            if not self.spam_targets and not self.raid_targets:
                await event.respond("❌ No active spam or raid targets")
                return

            output = "📋 **Active Spam Targets:**\n\n"
            for user_id, target in self.spam_targets.items():
                if target.active:
                    output += f"🆔 User {user_id} | Chat {target.chat_id} | {'Reply Spam' if target.reply_spam else f'Count: {target.count}'}\n"
            for user_id, target in self.raid_targets.items():
                if target.active:
                    output += f"🆔 User {user_id} | Chat {target.chat_id} | Raid Spam\n"
            await event.respond(output)

        elif text.startswith(".soff"):
            parts = text.split()
            target_id = None
            if len(parts) > 1:
                target = parts[1].lstrip('@')
                try:
                    target_id = int(target)
                except ValueError:
                    try:
                        entity = await self.client.get_entity(target)
                        target_id = entity.id
                    except:
                        await event.respond("❌ Invalid username or ID")
                        return
            elif reply_msg:
                target_id = reply_msg.sender_id

            if target_id and target_id in self.spam_targets:
                self.spam_targets[target_id].active = False
                await event.respond(f"✅ Spam stopped for User {target_id}")
            else:
                await event.respond("❌ No active spam for this user")

        elif text == ".offg":
            for user_id in self.spam_targets:
                self.spam_targets[user_id].active = False
            for user_id in self.raid_targets:
                self.raid_targets[user_id].active = False
                if user_id in self.spam_tasks:
                    self.spam_tasks[user_id].cancel()
                    del self.spam_tasks[user_id]
            await event.respond("✅ All spam and raid tasks stopped")

        elif text.startswith(".chudab"):
            parts = text.split()
            target_id = None
            if len(parts) > 1:
                target = parts[1].lstrip('@')
                try:
                    target_id = int(target)
                except ValueError:
                    try:
                        entity = await self.client.get_entity(target)
                        target_id = entity.id
                    except:
                        await event.respond("❌ Invalid username or ID")
                        return
            elif reply_msg:
                target_id = reply_msg.sender_id

            if target_id:
                self.raid_targets[target_id] = RaidTarget(target_id, chat_id, True)
                self.spam_tasks[target_id] = asyncio.create_task(self.raid_spam(target_id, chat_id))
                await event.respond(f"✅ Raid spam started for User {target_id}")
            else:
                await event.respond("❌ Usage: .chudab <username or ID> or reply to a user")

        elif text.startswith(".roff"):
            parts = text.split()
            target_id = None
            if len(parts) > 1:
                target = parts[1].lstrip('@')
                try:
                    target_id = int(target)
                except ValueError:
                    try:
                        entity = await self.client.get_entity(target)
                        target_id = entity.id
                    except:
                        await event.respond("❌ Invalid username or ID")
                        return
            elif reply_msg:
                target_id = reply_msg.sender_id

            if target_id and target_id in self.raid_targets:
                self.raid_targets[target_id].active = False
                if target_id in self.spam_tasks:
                    self.spam_tasks[target_id].cancel()
                    del self.spam_tasks[target_id]
                await event.respond(f"✅ Raid spam stopped for User {target_id}")
            else:
                await event.respond("❌ No active raid for this user")

        elif text == ".info" and reply_msg:
            user = reply_msg.sender
            user_info = f"""👤 **User Info:**

🆔 **ID:** `{user.id}`
📝 **Name:** {user.first_name or 'N/A'}
👤 **Username:** @{user.username if user.username else 'None'}
🔗 **Link:** tg://user?id={user.id}"""
            await event.respond(user_info)

    async def handle_reply_spam(self, event):
        sender_id = event.sender_id
        chat_id = event.chat_id
        if sender_id in self.spam_targets and self.spam_targets[sender_id].active and self.spam_targets[sender_id].reply_spam and self.spam_targets[sender_id].chat_id == chat_id:
            user = await self.client.get_entity(sender_id)
            username = f"@{user.username}" if user.username else f"User {sender_id}"
            message = random.choice(SPAM_MESSAGES['hindi'])
            await self.client.send_message(chat_id, f"{username} {message}", reply_to=event.message.id)
            await asyncio.sleep(random.uniform(0.5, 1.5))

    async def start(self):
        print("Starting spam bot...")

        @self.client.on(events.NewMessage)
        async def message_handler(event):
            await self.handle_message(event)
            await self.handle_reply_spam(event)

        await self.client.start()
        print("✅ Bot is running! Type .help to see commands")
        await self.client.run_until_disconnected()

async def main():
    api_id = input("Enter your Telegram API ID: ")
    api_hash = input("Enter your Telegram API Hash: ")
    owner_id = int(input("Enter your Telegram User ID: "))

    bot = SpamBot(api_id, api_hash, owner_id)
    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
