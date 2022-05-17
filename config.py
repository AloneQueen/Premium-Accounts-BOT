from dotenv import load_dotenv
from os import environ
from pyrogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv("config.env")

BOT_OWNER = 1467358214
BOT_TOKEN = environ.get("BOT_TOKEN", None)
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
DATABASE = environ.get("DATABASE")


STICKER = ["CAACAgIAAxkBAAEGVApibIes8S62v5AkF1lrsIRygq5xFgACAwEAAladvQoC5dF4h-X6Tx4E",
          "CAACAgIAAxkBAAEGSA5ia93HXYEAAbRDWZlDQGOgseJme-0AAhQAAztgJBQpZ4ESAvfI6h4E",
          "CAACAgIAAxkBAAEGRGtia1jSjDF3Zf5AAYPtf9wVKx79ZgACJgADDbbSGRYpFH5xkFugHgQ",
          "CAACAgIAAxkBAAEGVA1ibIfxr212zltxemfdBkynBVDQEAACjAADFkJrCkKO_mIXPU3iHgQ",
          "CAACAgIAAxkBAAEGVBBibIgYp0OjOF9R58K6DPURLcCknwACYQADDbbSGblGkUk4wVCCHgQ",
          "CAACAgIAAxkBAAEGVBNibIg0nEYtMPGO2wFY2kVOb6BG2QACzgADUomRI77CfDbcY4sSHgQ",
          "CAACAgIAAxkBAAEGVBZibIhRLEJ_jdmIK3C9_9SS2BN2ogACbgEAAjDUnRFcrCcMWa4mkh4E",      
          "CAACAgIAAxkBAAEGVBlibIiXqQWM3-OpSYNqChBYvo6umAACYwIAAsoDBgvs7jNsYlkcax4E",
          "CAACAgIAAxkBAAEGVBxibIjj0Ns8yxO-tGxMXh1blB6BUAACVQMAArVx2gYTIpfj7IkJBx4E",
          "CAACAgIAAxkBAAEGatpicIMuyHYfz2SM_WRR4Y-CAjXdAgACYwIAAsoDBgvs7jNsYlkcax4E",
          "CAACAgIAAxkBAAEGat1icIOjLcwOwNQcK4vtCtX8GGI8iwACWwADKA9qFLdiRrnAirpAHgQ",
          "CAACAgIAAxkBAAEGauBicIPGz_eREGt-k_PB7kt9Le8AAbgAAioAA8GcYAwjxoukwOqqDB4E",
          "CAACAgIAAxkBAAEGauVicIQVEz6rR8gDLQ1XmW_Wv3OtagACKQADWbv8JWiEdiw7SWZ7HgQ",
          "CAACAgIAAxkBAAEGauhicIRKAAGF1tKkfwSmkM97mLtUonEAAqsAAztgJBS0UIDM90a6nR4E"
         ]     

ABOUT_TEXT = f"""
<u>**🙋‍♂️ About  menu of Mafia Giveway Bot**</u>

<u>🌀 **About BOT basic** </u>

🔹 This Bot Developed And Server Maintained By [Supun](https://t.me/aboutsupun)
If You Have Any Problem With Bot Code or Another things Contact Me(Don't Come DM for Accounts)
🔹 I was got help from **Ⲋⲉⲛⲓⲧⲏ Ⲥⲏⲇⲛ𝖽ⳙⳑ** & **𝙎𝙞𝙩𝙝𝙪𝙢 𝘽𝙖𝙩𝙧𝙤𝙬** to manage Database.
🔹 This BOT was made useing Pyrogram + Mongo Data base.
🔹 If you want create Your own BOT come pm with your price.

<u>📚 **About Premium Accounts** </u>

▪️ All Of Premium Accounts Provides From This BOT Was Provided By 
@ImJanith & Mafia Team  If you have problem With  Accounts Contact Them or simply Use  Support Button.

Thank You All Of User !."""
HELP_TEXT =f"""

📮<u>**Help menu of Mafia Giveway Bot**</u>

🎁<u> **How To Get Free Credit **</u>

▪️ First click Free Credit buttons and join with the provided channels and get your bonus credits (1 time only).

▪️ After you can see   Referral  banner , share it with your friends and get 1 $ per one new user.

💎<u>** How To Get Accounts **</u>

▪️ First click Get Accounts button and get panel of accounts available in this moment click buttons as your want.

⚠️ **You must earn minimum 2 $ to get 1 account**

✅ You can see your request post in proof channel and i will provide your account..."""

START_TEXT = """
📚<u> I am bot that can provide **Premium Accounts**
Share me and get account as you want...</u>

For more open Giveaway join with [Mafia](https://t.me/MafiaGiveaways) & join with [sz team](https://t.me/szteambots) for BOT updates."""
REF = """
Send the banner above to your friends or contacts and for every new member that joins bot by you, you will gain 1 $!

UserID:`{}`
"""
SUPORT = """
**🔰 Our partners are at your service**

💁 Send us your problem bellow.
📨 For direct communication » @MafiaGiveawaysChat

⚠️ The support department tries to respond to all incoming messages in less than 12 hours, 
so be patient until you receive a response."""

fsubbutton = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔥 Join Here", url="https://t.me/szteambots")
                    ],
                    [
                        InlineKeyboardButton("🔥 Join Here", url="https://t.me/MafiaGiveaways")
                    ],
                    [ 
                        InlineKeyboardButton("🔥 Join Here", url="https://t.me/Mafiapayment")
                    ],
                    [ 
                        InlineKeyboardButton("🔥 Join Here", url="https://t.me/TheAmazonX")
                    ],
                ]
            )

TRANS = """
🆔 In this section you can transfer your $ to other bot users.
Your balance: {} $

Enter **UserID** of the person you want to transfer your money.
"""
TRANSC = """
💸  Enter the number of $ to transfer
Your balance: `{}` $
"""

keyboard =  ReplyKeyboardMarkup(
      [
        ['📢 Channels','💎Get Accounts💎'],
        ['👤 My Account','📊 Statistics','💸 Transfer'],
        ['👥 Referral'],
        ['☎️ Support','💳sponsorship'],
      ],resize_keyboard=True
    )

back = ReplyKeyboardMarkup(
      [
        ['«Back'],
      ],resize_keyboard=True
    )



comman =InlineKeyboardMarkup(
					[
                    [
							InlineKeyboardButton(
								"👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=1467358214),
							InlineKeyboardButton(
								"💠 Github", url="https://github.com/szsupunma")
					],
                    [
							InlineKeyboardButton(
								"🔰 Help", callback_data="help"),
							InlineKeyboardButton(
								"🌀 About Me", callback_data="aboutme")
					],
                    [
                        InlineKeyboardButton("🔥About You ", callback_data="about")
                    ]
                    ])



account = InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🥁 deezer", callback_data=f"giveme#deezer"),
                        InlineKeyboardButton("🦜 duolingo", callback_data=f"giveme#duolingo"),
                    ],
                    [
                        InlineKeyboardButton("🔙Back", callback_data=f"backs"),
                        InlineKeyboardButton("Close ✖️", callback_data=f"closed")
                    ]
                    ]
            )
SPON_TEXT = """
**With this tool you can sponsor Bot.**

❗️ ** Terms**
 » Cannot sponsor money.
 » You can give the bot the required accounts but the minimum should be 100+ and all working premium should be sent.

✅ **Things you get**

 » Free 1 Add Life- time via Bot.
 » Force - subscribe to your channel

👨‍💻 Contact : @supunma
"""

ADDS = ["Group Manager Bot(100% Free)- @szrosebot",
        "Free VPN(ssh) Acount Creater Group - @Darks_SSH",
        "Fun packed Telegram Bot Channel - @szteambots",
        "Zoom Premium Account Gen Bot - @ZOOM_GEN_BOT",
        "Rose Bot Updates Channel - @Theszrosebot",
        "**YouTech + VPN** - @YouTech_VPN_HUB"
        ]

accountf = InlineKeyboardMarkup(
                    [
                    [
                        InlineKeyboardButton("💵 2 $ Only(Premium Accounts)", callback_data=f"coin2"),
                    ],    
                    [
                        InlineKeyboardButton("💵 5 $ Only(Premium Accounts)", callback_data=f"5coin"),
                    ],
                    [
                        InlineKeyboardButton("💵 10 $ Only(Premium Accounts)", callback_data=f"10coins"),
                    ],
                    [
                        InlineKeyboardButton("💵 100 $ Only(Heroku CC Linked)", callback_data=f"ccadded#herokucc"),
                    ]]
            )

account1 = InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🎲 virtualDj", callback_data=f"fuckyou#virtualDj"),
                        InlineKeyboardButton("👻 shudder", callback_data=f"fuckyou#shudder")
                    ],
                    [
                        InlineKeyboardButton("🔙Back", callback_data=f"backs"),
                        InlineKeyboardButton("Close ✖️", callback_data=f"closed")
                    ]]
            )

account2 = InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("👨‍🏫 zoom(pro)", callback_data=f"sexyou#zoom"),
                        InlineKeyboardButton("🧑‍💻 heroku(free)", callback_data=f"sexyou#heroku"),
                    ],
                    [
                        InlineKeyboardButton("🌻 picsart", callback_data=f"sexyou#picsart")
                    ],
                    [
                        InlineKeyboardButton("🔙Back", callback_data=f"backs"),
                        InlineKeyboardButton("Close ✖️", callback_data=f"closed")
                    ]]
            )

Heroku = 5053761519
Zoom = 5053761519
Zee5 = 5053761519
callofduty = 5053761519
Shudder = 5053761519 
Pinterest = 5053761519
Duolingo = 5053761519
Picsart = 5053761519
Deezer = 5053761519
Canva = 5053761519
VirtualDj = 5053761519










