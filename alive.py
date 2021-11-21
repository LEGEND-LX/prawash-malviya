import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot.Config import Config
from telethon import version
from userbot import ALIVE_NAME, StartTime, PYTHONversion
from PYTHONBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from . import *
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "✞t͛ẞ̸ Pythonẞø✞ 🇮🇳"
PYTHON_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂ Choice Pythonẞø✞"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@Python_Userbot_Support"

Python = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={Python})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="pyalive$"))
@bot.on(sudo_cmd(pattern="pyalive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  PYTHON_IMG:
        PYTHON_caption = f"{CUSTOM_ALIVE_TEXT}**\n"
        
        PYTHON_caption += f"╔════❰Alive-linux❱═❍⊱❁ \n"
        PYTHON_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        PYTHON_caption += f"║┣⪼Developer    ┣⪼ [Legend-Lx](t.me/Legendl_Mr_Hacker) \n"
        PYTHON_caption += f"║┣⪼E-Developer  ┣⪼ [Legend-Os](t.me/The_LegendBoy) \n"
        PYTHON_caption += f"║╰━━━━━━━━━━━━━━━➣\n"
        PYTHON_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        PYTHON_caption += f"║┣⪼LegendBot    ┣⪼  [LegendBot](https://github.com/LEGEND-OS/LEGENDBOT)\n"
        PYTHON_caption += f"║┣⪼PyLegend     ┣⪼9.0.8,3.0\n"
        PYTHON_caption += f"║┣⪼LegendMix    ┣⪼ 3.0\n"
        PYTHON_caption += f"║╰━━━━━━━━━━━━━━━➣ \n"
        PYTHON_caption += f"╔══❰🔥Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ🔥❱═➣\n"
        PYTHON_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        PYTHON_caption += f"║┣⪼Ⲟⲱⲛⲉʀ      ┣⪼   [ℓєgєи∂-ℓx](t.me/Legendl_Mr_Hacker) \n"
        PYTHON_caption += f"║┣⪼Ⲋⲧⲁⲧυⲋ       ┣⪼    Ⲟⲛⳑⲓⲛⲉ\n"
        PYTHON_caption += f"║┣⪼Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ  ┣⪼  {mention}\n"
        PYTHON_caption += f"║┣⪼Ⳙⲣⲧⲓⲙⲉ       ┣⪼  {uptime}\n"
        PYTHON_caption += f"║┣⪼Ⲃⲟⲧ Ⲣⲓⲛⳋ     ┣⪼   290.087 \n"   
        PYTHON_caption += f"║┣⪼Ⲣⲩⲧⲏⲟⲛ       ┣⪼  {PYTHONversion}\n"
        PYTHON_caption += f"║┣⪼Os:  ┣⪼  [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
        PYTHON_caption += f"║┣⪼Ⲧⲉⳑⲉⲧⲏⲟⲛ      ┣⪼  {version.__version__}\n" 
        PYTHON_caption += f"║┣⪼[✨🐍PYTHON┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/Python_Userbot_Support)\n"
        PYTHON_caption += f"║╰━━━━━━━━━━━━━━━➣ \n"
        PYTHON_caption += f"╚══════════════════❍⊱❁۪۪\n"
        
        await alive.client.send_file(
            alive.chat_id, PYTHON_IMG, caption=PYTHON_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"╔════❰Alive-linux❱═❍⊱❁ \n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼Developer    ┣⪼ [Legend-Lx](t.me/Legendl_Mr_Hacker) \n"
            f"║┣⪼E-Developer  ┣⪼ [Legend-Os](t.me/The_LegendBoy) \n"
            f"║╰━━━━━━━━━━━━━━━➣\n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼LegendBot    ┣⪼  [LegendBot](https://github.com/LEGEND-OS/LEGENDBOT)\n"
            f"║┣⪼PyLegend     ┣⪼9.0.8,3.0\n"
            f"║┣⪼LegendMix    ┣⪼ 3.0\n"
            f"║╰━━━━━━━━━━━━━━━➣ \n"
            f"╔══❰🔥Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ🔥❱═➣\n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼Ⲟⲱⲛⲉʀ      ┣⪼   [ℓєgєи∂-ℓx](t.me/Legendl_Mr_Hacker) \n"
            f"║┣⪼Ⲋⲧⲁⲧυⲋ       ┣⪼    Ⲟⲛⳑⲓⲛⲉ\n"
            f"║┣⪼Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ  ┣⪼  {mention}\n"
            f"║┣⪼Ⳙⲣⲧⲓⲙⲉ       ┣⪼  {uptime}\n"
            f"║┣⪼Ⲃⲟⲧ Ⲣⲓⲛⳋ     ┣⪼   290.087 \n"   
            f"║┣⪼Ⲣⲩⲧⲏⲟⲛ       ┣⪼  {PYTHONversion}\n"
            f"║┣⪼Os:          ┣⪼  [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
            f"║┣⪼Ⲧⲉⳑⲉⲧⲏⲟⲛ      ┣⪼  {version.__version__}\n" 
            f"║┣⪼[✨🐍PYTHON┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/Python_Userbot_Support)\n"
            f"║╰━━━━━━━━━━━━━━━➣ \n"
            f"╚══════════════════❍⊱❁۪۪\n"
        )


msg = f"""
  ⚜️ pythonẞø† ιѕ σиℓιиє ⚜️
{Config.ALIVE_MSG}
**╔════❰Alive-linux❱═❍⊱❁ \n"
**║╭━━━━━━━━━━━━━━━➣ \n"
**║┣⪼Developer    ┣⪼ [Legend-Lx](t.me/Legendl_Mr_Hacker) \n"
**║┣⪼E-Developer  ┣⪼ [Legend-Os](t.me/The_LegendBoy) \n"
**║╰━━━━━━━━━━━━━━━➣\n"
**║╭━━━━━━━━━━━━━━━➣ \n"
**║┣⪼LegendBot    ┣⪼  [LegendBot](https://github.com/LEGEND-OS/LEGENDBOT)\n"
**║┣⪼PyLegend     ┣⪼9.0.8,3.0\n"
**║┣⪼LegendMix    ┣⪼ 3.0\n"
**║╰━━━━━━━━━━━━━━━➣ \n"
**╔══❰🔥Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ🔥❱═➣\n"
**║╭━━━━━━━━━━━━━━━➣ \n"
**║┣⪼Ⲟⲱⲛⲉʀ    ┣⪼   [ℓєgєи∂-ℓx](t.me/Legendl_Mr_Hacker) \n"
**║┣⪼Ⲋⲧⲁⲧυⲋ     ┣⪼    Ⲟⲛⳑⲓⲛⲉ\n"
**┣⪼Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ ┣⪼  {mention}\n"
**║┣⪼Ⳙⲣⲧⲓⲙⲉ     ┣⪼  {uptime}\n"
**║┣⪼Ⲃⲟⲧ Ⲣⲓⲛⳋ   ┣⪼   290.087 \n"   
**║┣⪼Ⲣⲩⲧⲏⲟⲛ    ┣⪼  {PYTHONversion}\n"
**║┣⪼Os:  ┣⪼  [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
**║┣⪼Ⲧⲉⳑⲉⲧⲏⲟⲛ   ┣⪼  {version.__version__}\n" 
**║┣⪼[✨🐍PYTHON┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/Python_Userbot_Support)\n"
**║╰━━━━━━━━━━━━━━━➣ \n"
**╚══════════════════❍⊱❁۪۪\n"
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def python_a(event):
    try:
        python = await bot.inline_query(botname, "alive")
        await python[0].click(event.chat_id)
        if event.sender_id == Python_Userbot_Support:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)

CmdHelp("alive").add_command(
    'bot', None, 'υѕє αи∂ ѕєє'
).add_type(
    "Official"
).add()
