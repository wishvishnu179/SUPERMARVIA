class script(object):
    START_TXT = """𝐻𝑒𝑙𝑙𝑜 {},
𝑀𝑦 𝑁𝑎𝑚𝑒 𝐼𝑠 <a href=https://t.me/{}>{}</a>, 𝐼 𝐴𝑚 𝐴 𝑆𝑖𝑚𝑝𝑙𝑒 𝐴𝑢𝑡𝑜𝐹𝑖𝑙𝑡𝑒𝑟 𝐵𝑜𝑡, 𝐼 𝐶𝑎𝑛 𝑃𝑟𝑜𝑣𝑖𝑑𝑒 𝑀𝑜𝑣𝑖𝑒𝑠, 𝐽𝑢𝑠𝑡 𝑆𝑒𝑎𝑟𝑐ℎ 𝑌𝑜𝑢𝑟 𝑅𝑒𝑞𝑢𝑒𝑠𝑡𝑒𝑑 𝑀𝑜𝑣𝑖𝑒 𝑜𝑟 𝑆𝑒𝑟𝑖𝑒𝑠 𝑁𝑎𝑚𝑒 𝐴𝑛𝑑 𝐸𝑛𝑗𝑜𝑦 😍"""
    HELP_TXT = """𝑯𝒆𝒚 {}
𝐻𝐸𝑅𝐸 𝐼𝑆 𝑇𝐻𝐸 𝐻𝐸𝐿𝑃 𝐹𝑂𝑅 𝑀𝑌 𝐶𝑂𝑀𝑀𝐴𝑁𝐷𝑆."""
    ABOUT_TXT = """✯ 𝑴𝒚 𝑵𝒂𝒎𝒆: {}
✯ 𝑪𝒓𝒆𝒂𝒕𝒐𝒓: <a href=https://t.me/VishnuMBbot>𝐕𝐢𝐬𝐡𝐧𝐮 𝐌𝐁</a>
✯ 𝑳𝒊𝒃𝒓𝒂𝒓𝒚: 𝑃𝑌𝑅𝑂𝐺𝑅𝐴𝑀
✯ 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆: 𝑃𝑌𝑇𝐻𝑂𝑁 3.10
✯ 𝑫𝒂𝒕𝒂𝑩𝒂𝒔𝒆: 𝑀𝑂𝑁𝐺𝑂 𝐷𝐵
✯ 𝑩𝒐𝒕 𝑺𝒆𝒓𝒗𝒆𝒓: 𝑆𝑂𝑀𝐸𝑊𝐻𝐸𝑅𝐸
✯ 𝑩𝒖𝒊𝒍𝒅 𝑺𝒕𝒂𝒕𝒖𝒔: 𝑉𝑒𝑟𝑠𝑖𝑜𝑛 69🤤 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TGCinemaworld>Vishnu MB🤍</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. tgcwsearch bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/tgcwfilterBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝑻𝑶𝑻𝑨𝑳 𝑭𝑰𝑳𝑬𝑺: <code>{}</code>
★ 𝑻𝑶𝑻𝑨𝑳 𝑼𝑺𝑬𝑹𝑺: <code>{}</code>
★ 𝑻𝑶𝑻𝑨𝑳 𝑪𝑯𝑨𝑻𝑺: <code>{}</code>
★ 𝑼𝑺𝑬𝑫 𝑺𝑻𝑶𝑹𝑨𝑮𝑬: <code>{}</code> 𝙼𝚒𝙱
★ 𝑭𝑹𝑬𝑬 𝑺𝑻𝑶𝑹𝑨𝑮𝑬: <code>{}</code> 𝙼𝚒𝙱"""
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 [ Sᴛᴀʙʟᴇ ]</code>

Bʏ @TGCWFilterbot</b>"""
    CAPTION = """ <b><i><a href="https://telegram.me/Tgcinemaworld">{file_caption}</a>\nSize:-<i>{file_size}</i>\nJoin:- @TGCinemaworld</i></b>\n\n"""
    
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
