# THINGS TO DO......
# ANONYMOUS PROBLEM (EVERY MESSAGE IS ANONYMOUS HOW TO FIX)
# PICTURES
# WEBSITE ACTUAL

import os
import csv
import re
from flask import Flask, render_template, request, redirect, url_for, session
from waitress import serve
from datetime import datetime
from passlib.hash import bcrypt_sha256

currentlocation = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

scholars = {
    1: {'nickname': 'Tristan', 
        'description': 'hello i’m tris 😍 !!! gacha games and MUN are my passion 🔥graduating with bs taylor swift major in yapping, all things coffee ☕ and height 🤭',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'toacebedo',
        'password': bcrypt_sha256.hash('toacebedo'),
        'fullname': 'ACEBEDO, TRISTAN ANDREW O.'},
    2: {'nickname': 'Ikai', 
        'description': 'Haloooo it’s Ikai 🌟 Pisay was an adventure. It would mean the world if I got any message from the people who’ve added color to my life 🤩',
        'section': '12 - SIRIUS',
        'core': 'CHEMISTRY CORE',
        'username': 'dbalbeos',
        'password': bcrypt_sha256.hash('dbalbeos'),
        'fullname': 'ALBEOS, DANICA MARIE B.'},
    3: {'nickname': 'Jamie', 
        'description': 'B) Top 0.05% of Pierce The Veil Listeners',
        'section': '12 - SIRIUS',
        'core': 'CHEMISTRY CORE',
        'username': 'jmalmazan',
        'password': bcrypt_sha256.hash('jmalmazan'),
        'fullname': 'ALMAZAN, JAMIE M.'},
    4: {'nickname': 'Loyan', 
        'description': 'Friendly, Funny, Approachable, Nonchalant, Batch VP.... <br><br> > Email: loyan13aloba@gmail.com <br> > Phone: 09063226300/09619340546 <br> > Instagram: @loyanaloba <br> > Gcash: 09063226300',
        'section': '12 - SIRIUS',
        'core': 'PHYSICS CORE',
        'username': 'lmaloba',
        'password': bcrypt_sha256.hash('lmaloba'),
        'fullname': 'ALOBA, LOYAN EDRIAN M.'},
    5: {'nickname': 'Prince', 
        'description': 'Attempting to make the stars reachable',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'jlalonte',
        'password': bcrypt_sha256.hash('jlalonte'),
        'fullname': 'ALONTE, JOHN PRINCE L.'},
    6: {'nickname': 'Nize', 
        'description': 'tapos na ang pagpapanggap',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'mcamaya',
        'password': bcrypt_sha256.hash('mcamaya'),
        'fullname': 'AMAYA, MARIE DENIZZE C.'},
    7: {'nickname': 'Mark', 
        'description': '',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'mrartigas',
        'password': bcrypt_sha256.hash('mrartigas'),
        'fullname': 'ARTIGAS, MARK LUIS R.'},
    8: {'nickname': 'Jet', 'description': 
        'Jan Erik Theo Pelandas Balabat, 17 years old, August 11, 2006, San Agustin, Alburquerque, Bohol, 09664528570, META JetB, Enataya,',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'jbalabat',
        'password': bcrypt_sha256.hash('jbalabat'),
        'fullname': 'BALABAT, JAN ERIK THEO P.'},
    9: {'nickname': 'Sai', 
        'description': '(๑•ᴗ• ) ★ atz brainrot haha ★ arriba, abajo, al centro, y pa dentro 🍻',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'cdbantaya',
        'password': bcrypt_sha256.hash('cdbantaya'),
        'fullname': 'BANTAYA, CYRILLE PAULINE D.'},
    10: {'nickname': 'Marcky', 
        'description': 'HELLOOOOOOOOO!!! Ate Marcky here, sulat ra btawg bisag unsa 🥹 [09950436840 - dawat bisag piso 😜]',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'mlbarriga',
        'password': bcrypt_sha256.hash('mlbarriga'),
        'fullname': 'BARRIGA, MARIA CASSANDRA L.'},
    11: {'nickname': 'Justin', 
        'description': 'Gcash: 09054902560',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'jabarron',
        'password': bcrypt_sha256.hash('jabarron'),
        'fullname': 'BARRON, JUSTIN BENEDICT B.'},
    12: {'nickname': 'Shaira', 
        'description': 'God’s sleepiest soldier 😴, reporting for duty 🫡 I might catch some Zs 💤 but you’ll never see me take any Ls 👆 Don’t forget to chill out ❄️ and have some fun🕺for life is but a dream 💭',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'stbathan',
        'password': bcrypt_sha256.hash('stbathan'),
        'fullname': 'BATHAN, SHAIRA JHONE T.'},
    13: {'nickname': 'Benedict', 
        'description': 'im the best at table tennis',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'bcbedolido',
        'password': bcrypt_sha256.hash('bcbedolido'),
        'fullname': 'BEDOLIDO, BENEDICT C.'},
    14: {'nickname': 'Russell', 
        'description': 'Gwapo, bright, athletic, di mapildeg sumbagay',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'rpbeduya',
        'password': bcrypt_sha256.hash('rpbeduya'),
        'fullname': 'BEDUYA, RUSSELL LORENZ P.'},
    15: {'nickname': 'Abby', 
        'description': 'Hey, Abby here! Your resident vocal powerhouse (notice me dwtb) and constant flop era guy 🙁Manifest pasa sa lahat ng unis I applied to 😭🙏🔥',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'jybolok',
        'password': bcrypt_sha256.hash('jybolok'),
        'fullname': 'BOLOK, JOANNA ISABELLE Y.'},
    16: {'nickname': 'Sean', 
        'description': 'Future CEO of Jurassic Park Cebu',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'sbongbong',
        'password': bcrypt_sha256.hash('sbongbong'),
        'fullname': 'BONGBONG, SEAN PHILIPPE MIGUEL'},
    17: {'nickname': 'JM', 
        'description': 'ik that he loves me bc he told me so ik that he loves me bc his feelings show when he stares at me u see he cares for me u see how he is so deep in 💓',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'jyborbajo',
        'password': bcrypt_sha256.hash('jyborbajo'),
        'fullname': 'BORBAJO, JEANNE MARGARETTE Y.'},
    18: {'nickname': 'Myenn', 
        'description': 'syempre di mo ko gusto, ’di naman aq tulad ng ibang babae na nagsuot ng make up at dress. oks lng. sanay na aq. di tau pede ok lg salamat sa lahat.',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'jacabahug',
        'password': bcrypt_sha256.hash('jacabahug'),
        'fullname': 'CABAHUG, JOY MYENN A.'},
    19: {'nickname': 'Zhen/Dawn', 
        'description': '',
        'section': '12 - SIRIUS',
        'core': 'CHEMISTRY CORE',
        'username': 'zscabanos',
        'password': bcrypt_sha256.hash('zscabanos'),
        'fullname': 'CABANOS, ZHENICE DAWN S.'},
    20: {'nickname': 'Vik', 
        'description': 'Watching. Waiting. Commiserating. 🫠',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'bdcadiz',
        'password': bcrypt_sha256.hash('bdcadiz'),
        'fullname': 'CADIZ, MARIA VIKTORIA D.'},
    21: {'nickname': 'Yummy', 
        'description': ' 📍BHL | CEB | MNL <br> I can sleep anywhere, anytime 😴🥱 <br> Eat. 🥡 Work Hard. 🥋 Party Harder. 💃🏻 <br><br> Jude 1:2 ☝️',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'licaduyac',
        'password': bcrypt_sha256.hash('licaduyac'),
        'fullname': 'CADUYAC, LIAH MEI I.'},
    22: {'nickname': 'Mishka', 
        'description': 'Future engineer or airline pilot na ready na mufly high, soar high eme. ✈️🦅 You may send grad gifts here: 0995xxxx083 mwah mwah',
        'section': '12 - SIRIUS',
        'core': 'PHYSICS CORE',
        'username': 'mocahambing',
        'password': bcrypt_sha256.hash('mocahambing'),
        'fullname': 'CAHAMBING, MIKAELA DANIELLE O.'},
    23: {'nickname': 'Rhanz', 
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, babye Pisay.',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'rccajelo',
        'password': bcrypt_sha256.hash('rccajelo'),
        'fullname': 'CAJELO, RHANZ C.'},
    24: {'nickname': 'Joestin', 
        'description': 'If kisses are water, i will give you the ocean. If hugs are leaves, i will give you a tree. And if love is time, i will give you eternity. Remember, my love for you is starting at forever, and ending at never :)',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'cccallora',
        'password': bcrypt_sha256.hash('cccallora'),
        'fullname': 'CALLORA, CHARLES JOESTIN C.'},
    25: {'nickname': 'Zack/Kenshin', 
        'description': '| Socially inconsistent overthinker | Local tourist scam victim | Rhythm Gamer | <br><br> 𝘐’𝘮 𝘯𝘰𝘵 𝘥𝘦𝘢𝘥 𝘺𝘦𝘵, 𝘴𝘰 𝘐 𝘨𝘶𝘦𝘴𝘴 𝘐’𝘭𝘭 𝘣𝘦 𝘢𝘭𝘳𝘪𝘨𝘩𝘵~♪',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'zccamello',
        'password': bcrypt_sha256.hash('zccamello'),
        'fullname': 'CAMELLO, ZACK KENSHIN C.'},
    26: {'nickname': 'Marc', 
        'description': 'Hi hello children!! Got something to say to ur derpy & fruity kuya? You can send me a message here :D All messages are welcome :3',
        'section': '12 - RIGEL',
        'core': 'CHEMISTRY CORE',
        'username': 'mpcana',
        'password': bcrypt_sha256.hash('mpcana'),
        'fullname': 'CAÑA, MARC BRYAN P.'},
    27: {'nickname': 'Maky', 
        'description': '',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'mtcanoy',
        'password': bcrypt_sha256.hash('mtcanoy'),
        'fullname': 'CANOY, MAKHAELA FRANCIS T.'},
    28: {'nickname': 'Angel', 
        'description': 'college admission or psychward admission 😊💯💯 interests: siya 🔥🔥😜',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'mscasayas',
        'password': bcrypt_sha256.hash('mscasayas'),
        'fullname': 'CASAYAS, MARY ANGELOISE S.'},
    29: {'nickname': 'Xanxan', 
        'description': 'are u sili? bc i’m falling in labuyo. 🌽🌶️',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'adceniza',
        'password': bcrypt_sha256.hash('adceniza'),
        'fullname': 'CENIZA, ALEXANDER RICHARDSON D.'},
    30: {'nickname': 'Monica', 
        'description': 'pls keep the cvisc vb community alive. see u around !!🏐🩷',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'ltchua',
        'password': bcrypt_sha256.hash('ltchua'),
        'fullname': 'CHUA, LOUISE MONICA T.'},
    31: {'nickname': 'Jhai/Jhaileyn', 
        'description': 'hi hello slay slay slay',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'jccruz',
        'password': bcrypt_sha256.hash('jccruz'),
        'fullname': 'CRUZ, JHAYLIN FAITH C.'},
    32: {'nickname': 'Venze', 
        'description': 'Math nerd by day. Basketballer/footballer by afternoon (mostly footballer). Tekken pro, JJK/Naruto fan, and gamer by night.',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'vrcuba',
        'password': bcrypt_sha256.hash('vrcuba'),
        'fullname': 'CUBA, VENZE EDWIN LEONARD R.'},
    33: {'nickname': 'Niru', 
        'description': 'henirbro',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'nmdagoy',
        'password': bcrypt_sha256.hash('nmdagoy'),
        'fullname': 'DAGOY, NIRU MIGUEL M.'},
    34: {'nickname': 'Renz', 
        'description': 'grad gift? <br><br> gcash: 09064120573 <br><br> thank youuuu 😘',
        'section': '12 - POLLUX',
        'core': 'CHEMISTRY CORE',
        'username': 'rtdelapena',
        'password': bcrypt_sha256.hash('rtdelapena'),
        'fullname': 'DE LA PEÑA, RENZ NICHOLAS T.'},
    # MISSING RESPONSE
    35: {'nickname': 'Miggy', 
        'description': '',
        'section': '',
        'core': '',
        'username': 'eedelatorre',
        'password': bcrypt_sha256.hash('eedelatorre'),
        'fullname': 'DELA TORRE, EMMANUELLI MIGUEL E.'},
    36: {'nickname': 'Ashley', 
        'description': 'GCASH: 09190041082',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'aodeniega',
        'password': bcrypt_sha256.hash('aodeniega'),
        'fullname': 'DENIEGA, ASHLEY CARMELITE O.'},
    37: {'nickname': 'Antonio', 
        'description': '“Very well,” he said, “I will let you bake your bread over cow dung instead of human excrement.” <br> - Ezekiel 4:15',
        'section': '12 - SIRIUS',
        'core': 'PHYSICS CORE',
        'username': 'agdiao',
        'password': bcrypt_sha256.hash('agdiao'),
        'fullname': 'DIAO, ALLEN BUCK G.'},
    38: {'nickname': 'Giov', 
        'description': 'pair ni jody kay nanglimpyo siya — bs mental acrobatics',
        'section': '12 - RIGEL',
        'core': 'CHEMISTRY CORE',
        'username': 'gddolanas',
        'password': bcrypt_sha256.hash('gddolanas'),
        'fullname': 'DOLANAS, GIOVANNI KENT D.'},
    39: {'nickname': 'Zach', 
        'description': 'Hello',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'ztducante',
        'password': bcrypt_sha256.hash('ztducante'),
        'fullname': 'DUCANTE, ZACHARI KAHLIL T.'},
    40: {'nickname': 'Jill/Sel', 
        'description': 'future doctor <3 (living my best life 💖🙏💯 in my head)',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'jeduran',
        'password': bcrypt_sha256.hash('jeduran'),
        'fullname': 'DURAN, JILLIANNE E.'},
    41: {'nickname': 'Ino', 
        'description': 'hello',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'bmdurano',
        'password': bcrypt_sha256.hash('bmdurano'),
        'fullname': 'DURANO, BERNARD INO M.'},
    42: {'nickname': 'Paula/Pauie', 
        'description': 'Your resident food lover🍝 looking for the next tiktok recipe📲, avid book reader 📚, karaoke resident🎤💃, and always repping sunsets🌄 and oceans🌊',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'pcelumba',
        'password': bcrypt_sha256.hash('pcelumba'),
        'fullname': 'ELUMBA, PAULA C.'},
    43: {'nickname': 'Zharnie', 
        'description': 'one of the girls at the back',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'zdentea',
        'password': bcrypt_sha256.hash('zdentea'),
        'fullname': 'ENTEA, ZHARNIE JEAN D.'},
    44: {'nickname': 'Kean', 
        'description': 'Lalalalaal',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'ksesmero',
        'password': bcrypt_sha256.hash('ksesmero'),
        'fullname': 'ESMERO, KEAN LENNON DAVID S.'},
    45: {'nickname': 'Merai', 
        'description': '“ 𝙆𝙖-𝘾𝙝𝙤𝙬 ⚡️” <br><br> Secretary ng Bayan 🔥<br> CVisC MUN x AFS-SSG x DebSoc x merai’s pastries',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'ebflores',
        'password': bcrypt_sha256.hash('ebflores'),
        'fullname': 'FLORES, EMERY MYLES B.'},
    46: {'nickname': 'Nicole', 
        'description': 'send ket ano, thank you!🫶🌷 <br> (pwede racquet recomms<33)',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'nsgambot',
        'password': bcrypt_sha256.hash('nsgambot'),
        'fullname': 'GAMBOT, NICOLE KLEIN S.'},
    47: {'nickname': 'Jody', 
        'description': 'Gcash: 09560769125',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'jehupp',
        'password': bcrypt_sha256.hash('jehupp'),
        'fullname': 'HUPP, JODY ISOBELLE E.'},
    48: {'nickname': 'RJ', 
        'description': 'unsay college interest nga siya man ako interest 😜💯💯 interests: siya ra lage ❤️🔥',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'rujayo',
        'password': bcrypt_sha256.hash('rujayo'),
        'fullname': 'JAYO, RYAN JAMES U.'},
    49: {'nickname': 'Sofia', 
        'description': 'Hello, I’m Sofia AKA bingus or eep for short ⁠(⁠ ͡⁠◉⁠ ͜⁠ ⁠ʖ⁠ ͡⁠◉⁠) I like scrolling, reading, sleeping and trying to like PHYSICS CORE. That’s all, thanks!',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'sskaamino',
        'password': bcrypt_sha256.hash('sskaamino'),
        'fullname': 'KAAMIÑO, SOFIA NICOLE S.'},
    50: {'nickname': 'Kits', 
        'description': 'Once we were the tops 🏆, but now we’ve moved on to chase new passions 🥺💖. <br><br> Follow me on PUBGM: DLR『Jade』ツ <br> Follow me on CODM: 6754374855618985985',
        'section': '12 - RIGEL',
        'core': 'CHEMISTRY CORE',
        'username': 'tfkitamura',
        'password': bcrypt_sha256.hash('tfkitamura'),
        'fullname': 'KITAMURA, THOMAS JADE F.'},
    51: {'nickname': 'Julianna', 
        'description': 'This time, I want <br> You, you, you, you, like it’s magnetic <br> You, you, you, you, you, you, you, you, super 이끌림',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'rslerasan',
        'password': bcrypt_sha256.hash('rslerasan'),
        'fullname': 'LERASAN, RAYE JULIANNA S.'},
    52: {'nickname': 'Taize', 
        'description': 'Salut, it’s Taize! 🪻 Siri, play Water by Tyla 💧for ur local violet BIOLOGY CORElogist & artist 🎨 K back to playing Stardew Valley 🌸🤠',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'tmlimboy',
        'password': bcrypt_sha256.hash('tmlimboy'),
        'fullname': 'LIMBOY, TAIZE BELLE M.'},
    53: {'nickname': 'Sophia', 
        'description': 'twitter, ig: @_lophiel | @milkuii <br> https://milkuii.carrd.co/',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'snlogarta',
        'password': bcrypt_sha256.hash('snlogarta'),
        'fullname': 'LOGARTA, SOPHIA GABRIELLE N.'},
    54: {'nickname': 'Enya', 
        'description': 'still and always will be here for all the love in the world 🫶',
        'section': '12 - RIGEL',
        'core': 'CHEMISTRY CORE',
        'username': 'ealozano',
        'password': bcrypt_sha256.hash('ealozano'),
        'fullname': 'LOZANO, ENYA MARGUERITE A.'},
    55: {'nickname': 'Aye', 
        'description': 'Jumbo Hatdog, Kaya mo ba toh? Di nako kaya',
        'section': '12 - SIRIUS',
        'core': 'CHEMISTRY CORE',
        'username': 'asmahusay',
        'password': bcrypt_sha256.hash('asmahusay'),
        'fullname': 'MAHUSAY, ARIEL S.'},
    56: {'nickname': 'Gelo', 
        'description': '(PLACEHOLDER BIO AYAW KALIMOT)',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'gpmanreal',
        'password': bcrypt_sha256.hash('gpmanreal'),
        'fullname': 'MANREAL, GELO ANTONIO P.'},
    57: {'nickname': 'Cassy', 
        'description': 'And thus, the catventure of this kittyself begins? 😼',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'cdmarto',
        'password': bcrypt_sha256.hash('cdmarto'),
        'fullname': 'MARTO, CASSANDRA MARISSE D.'},
    58: {'nickname': 'Villy', 
        'description': 'What’s up brother!!☝️🤓',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'vpmejias',
        'password': bcrypt_sha256.hash('vpmejias'),
        'fullname': 'MEJIAS, VILLY MELCHZ P.'},
    59: {'nickname': 'Marybel', 
        'description': 'Salamin, salamin sa dingding 🫣🤚🫣🖐️ <br> Nasa’n na ang pag-ibig? 🤲 <br> Salamin, salamin 🫣🤚🫣🖐️ <br> Kailan niya ba ’ko papansinin? 🤭😎☝️',
        'section': '12 - POLLUX',
        'core': 'CHEMISTRY CORE',
        'username': 'mamontejo',
        'password': bcrypt_sha256.hash('mamontejo'),
        'fullname': 'MONTEJO, MARYBEL ZYRES A.'},
    60: {'nickname': 'Ethan', 
        'description': 'Your average drifter 🍃 philosopher 🤔 and food enjoyer 🍩 reminding you to "take life sincerely, not seriously".',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'ermontuya',
        'password': bcrypt_sha256.hash('ermontuya'),
        'fullname': 'MONTUYA, ETHAN JEUSHREY R.'},
    61: {'nickname': '@dolyennn', 
        'description': 'I love Joestin 🫶🫶🫶',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'knable',
        'password': bcrypt_sha256.hash('knable'),
        'fullname': 'NABLE, KYLEWIN ASHTON'},
    62: {'nickname': 'Ram', 
        'description': 'Your local tall guy. <br> !WARNING! MAY INCLUDE: <br> Coffee, <br> Microplastics, and <br> Polygons',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'alnavasquez',
        'password': bcrypt_sha256.hash('alnavasquez'),
        'fullname': 'NAVASQUEZ, AIRAM GIAN L.'},
    63: {'nickname': 'AJ', 
        'description': 'Sci-Fi, Horror & Fantasy buff 🎬📚 | Cycling 🚴‍♂️, boxing 🥊, and BJJ 🥋 enthusiast | Strategy gamer extraordinaire 🎮 | Always up for a challenge!',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'abodal',
        'password': bcrypt_sha256.hash('abodal'),
        'fullname': 'ODAL, ADRIAN JOSEPH B.'},
    64: {'nickname': 'Nico', 
        'description': 'im nico and ok',
        'section': '12 - SIRIUS',
        'core': 'PHYSICS CORE',
        'username': 'drosorio',
        'password': bcrypt_sha256.hash('drosorio'),
        'fullname': 'OSORIO, DOMINIC MARCO R.'},
    65: {'nickname': 'Ia', 
        'description': 'Bio Core student and gamer just trying her best.',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'ippaclibar',
        'password': bcrypt_sha256.hash('ippaclibar'),
        'fullname': 'PACLIBAR, IA NIKKA ALYANNA P.'},
    66: {'nickname': 'Jen', 
        'description': 'Slow 😫, Dense 🫠, Late Bloomer 🪷 Biology 👩‍🔬 and Creatives 👩‍🎨 Enthusiast. <br><br> "𝓐𝓻𝓮 🤔 𝔀𝓱𝓪𝓵𝓮𝓼 🐳 𝓶𝓪𝓶𝓶𝓪𝓵𝓼 🙊🙉⁉️".',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'jbpacot',
        'password': bcrypt_sha256.hash('jbpacot'),
        'fullname': 'PACOT, JANE DOMINIQUE B.'},
    67: {'nickname': 'LG', 
        'description': 'hello. eokmpz. im friend.',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'llpalmitos',
        'password': bcrypt_sha256.hash('llpalmitos'),
        'fullname': 'PALMITOS, LEIF GARRETH L.'},
    68: {'nickname': 'Xillin', 
        'description': 'Let whoever think whatever. Speak freely to me, hooman.',
        'section': '12 - POLLUX',
        'core': 'CHEMISTRY CORE',
        'username': 'xjpantonial',
        'password': bcrypt_sha256.hash('xjpantonial'),
        'fullname': 'PANTONIAL, XILLIN MARIAH J.'},
    69: {'nickname': 'Coby', 
        'description': 'It’s me Cobs :D <br> Baw bitaw unsay ibutang sa bio <br> I’m down if u wanna send a message or smthn <br> ill attach my gcash if sugtan ko (grad gift hehe👉👈)',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'jbquinal',
        'password': bcrypt_sha256.hash('jbquinal'),
        'fullname': 'QUIÑAL, JACOB BRYAN B.'},
    70: {'nickname': 'Yayou', 
        'description': 'young at heart, dili way buot',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'rbracoma',
        'password': bcrypt_sha256.hash('rbracoma'),
        'fullname': 'RACOMA, ROLAND MARIO B.'},
    71: {'nickname': 'Herald', 
        'description': '😭💞😜🥺🥱😳😲🤧👻🙀🎉🩵💚🫰🤟👌💁✨🐼🍑🌮🍻🧳🌃🏀🏸🖥️🛏️🛏️🛏️💡👔🦺🩲⏱️🛎️⏰🇵🇭🇯🇵',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'hbremedio',
        'password': bcrypt_sha256.hash('hbremedio'),
        'fullname': 'REMEDIO, HERALD KINT B.'},
    72: {'nickname': 'Hans', 
        'description': '"I think I am smart unless I am really, really in love, and then I am ridiculously stupid" <br><br> - Taylor Swift',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'jaremo',
        'password': bcrypt_sha256.hash('jaremo'),
        'fullname': 'REMO, JOSEPH HANS OLIVER A.'},
    73: {'nickname': 'Lyka', 
        'description': 'Imbued with the core values of integrity, excellence, and SERVE 💅✨💃🎀🫦 …ice to nation',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'carevalde',
        'password': bcrypt_sha256.hash('carevalde'),
        'fullname': 'REVALDE, CHRISTINE JYLE LYKA A.'},
    74: {'nickname': 'Sam', 
        'description': '“If he writes her a few sonnets, he loves her. If he writes her 300 sonnets, he loves sonnets.”',
        'section': '12 - POLLUX',
        'core': 'BIOLOGY CORE',
        'username': 'srrevalde',
        'password': bcrypt_sha256.hash('srrevalde'),
        'fullname': 'REVALDE, SAMANTHA R.'},
    75: {'nickname': 'Cianter', 
        'description': 'Good day. I am cnater from 12 - Sirius. LEAVE A MESSAGE FOR DIWATA PARES OVERLOAD FRANCHISING! Please inform me if you have Belle Haewon or Sunoo pcs.',
        'section': '12 - SIRIUS',
        'core': 'PHYSICS CORE',
        'username': 'cvrica',
        'password': bcrypt_sha256.hash('cvrica'),
        'fullname': 'RICA, CIANTER QUIN V.'},
    76: {'nickname': 'Dan', 
        'description': 'I’m ready to leave, ready to live, ready to go-oh-oohh." <br> -Ready to Go, P!ATD. <br><br> Free me, man; I didn’t do nun wrong! Take me to college already, bruh!',
        'section': '12 - SIRIUS',
        'core': 'PHYSICS CORE',
        'username': 'drricarte',
        'password': bcrypt_sha256.hash('drricarte'),
        'fullname': 'RICARTE, DANIEL R.'},
    77: {'nickname': 'Dwight', 
        'description': 'Hi. I’m Dwight, a Physics core student from 12-Sirius. I like games and I like volleyball. Be kind. Kindness goes a long way, even if you are not kind all the time. Ayaw sad padala og bisyo etc. Study well.',
        'section': '12 - SIRIUS',
        'core': 'PHYSICS CORE',
        'username': 'dricarte',
        'password': bcrypt_sha256.hash('dricarte'),
        'fullname': 'RICARTE, DWIGHT R.'},
    78: {'nickname': 'Paul', 
        'description': 'Legendary 💥💥💥',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'pasagarino',
        'password': bcrypt_sha256.hash('pasagarino'),
        'fullname': 'SAGARINO, PAUL EDUARD A.'},
    79: {'nickname': 'Bethel', 
        'description': 'Kenyan Jogging with Bethel <br> Call time: 5pm 👟 <br> 6:30 - 7:30 pace <br> Bring your own water and phone for Strava. <br> STRAVA IGN: Penhold Runner',
        'section': '12 - SIRIUS',
        'core': 'PHYSICS CORE',
        'username': 'basalvador',
        'password': bcrypt_sha256.hash('basalvador'),
        'fullname': 'SALVADOR, BETHEL CHRIS A.'},
    80: {'nickname': 'Khyarra/Kiki', 
        'description': 'Hey there! (⁠◍⁠•⁠ᴗ⁠•⁠◍⁠) I’m Kiki, and you’re watching--- me fall into a hysterical meltdown because we’re finally about to graduate :((. If you see me in the hallways, don’t be afraid to approach me or smile orr, if you want to tell me anything, I can always listen naman (if dili busy). (⁠人⁠ ⁠•͈⁠ᴗ⁠•͈⁠) I hope you’ll remember me as much as I will remember how wonderful pisay has been (pro sugarcoater lesgo)!! <33',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'kstelmo',
        'password': bcrypt_sha256.hash('kstelmo'),
        'fullname': 'TELMO, KHYARRA ALEXEI S.'},
    81: {'nickname': 'Wayne', 
        'description': 'HELLO I AM WAYNET!!!!! Send me whatever message u like lmao I’m chill 💯💯',
        'section': '12 - RIGEL',
        'core': 'PHYSICS CORE',
        'username': 'wjtiongco',
        'password': bcrypt_sha256.hash('wjtiongco'),
        'fullname': 'TIONGCO, WAYNE EVANDER J.'},
    82: {'nickname': 'Mya', 
        'description': 'iyak malopit 😢 thirst trap saglit 🫦 ijbol ulit 😁',
        'section': '12 - RIGEL',
        'core': 'CHEMISTRY CORE',
        'username': 'mtorralba',
        'password': bcrypt_sha256.hash('mtorralba'),
        'fullname': 'TORRALBA, MYA M.'},
    # MISSING RESPONSE
    83: {'nickname': 'Andrei', 
        'description': '',
        'section': '',
        'core': '',
        'username': 'afuy',
        'password': bcrypt_sha256.hash('afuy'),
        'fullname': 'UY, ANDREI NICOLEI F.'},
    84: {'nickname': 'Ker', 
        'description': 'seashell lover 🐚 <br> chronic sleeper 💤 <br> constant daydreamer 😶‍🌫️',
        'section': '12 - RIGEL',
        'core': 'BIOLOGY CORE',
        'username': 'kcuy',
        'password': bcrypt_sha256.hash('kcuy'),
        'fullname': 'UY, KEREN ANNE C.'},
    85: {'nickname': 'Hannah', 
        'description': 'This girl’s ready to face the world unfazed because she’s lavished in perfect grace 💖 <br><br> 🎶 She’s ready, she’s steady, <br> She’s up on her feet 🎶',
        'section': '12 - SIRIUS',
        'core': 'BIOLOGY CORE',
        'username': 'lavinarao',
        'password': bcrypt_sha256.hash('lavinarao'),
        'fullname': 'VINARAO, LAHJA HANNAH A.'},
    86: {'nickname': 'Joricah', 
        'description': 'resident house plant 🍀',
        'section': '12 - POLLUX',
        'core': 'CHEMISTRY CORE',
        'username': 'jayabo',
        'password': bcrypt_sha256.hash('jayabo'),
        'fullname': 'YABO, JORICAH BIANCA A.'},
    87: {'nickname': 'Henry', 
        'description': 'hello i am Henry from 12-Pollux i am 18 years old and i like playing games and spending time with my bimbots. Please leave me a message if we are bimbots also',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'htyap',
        'password': bcrypt_sha256.hash('htyap'),
        'fullname': 'YAP,  HENRY T. III'},
    88: {'nickname': 'Lexis', 
        'description': 'Don’t tell anyone, but I’m a handsome ninja 🦧',
        'section': '12 - SIRIUS',
        'core': 'CHEMISTRY CORE',
        'username': 'apzamora',
        'password': bcrypt_sha256.hash('apzamora'),
        'fullname': 'ZAMORA, ALEXIS JANE P.'},
    89: {'nickname': 'Bill', 
        'description': 'i love my jam flavored sandwich',
        'section': '12 - POLLUX',
        'core': 'PHYSICS CORE',
        'username': 'bazamora',
        'password': bcrypt_sha256.hash('bazamora'),
        'fullname': 'ZAMORA, BILL ANAKIN A.'},
}

scholar_id = 0 # Placeholder

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for scholar_id, credentials in scholars.items():
            if credentials['username'] == username and bcrypt_sha256.verify(password, credentials['password']):
                session['logged_in'] = True
                session['scholar_id'] = scholar_id
                return redirect(url_for('inbox', scholar_id=scholar_id))
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

MESSAGES_CSV_FILE = 'messages.csv'

def send_message(sender_name, content, recipient_id):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(MESSAGES_CSV_FILE, 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sender_name, content, timestamp, recipient_id])

@app.route('/send_message/<int:scholar_id>', methods=['POST'])
def send_message_route(scholar_id):
    if request.method == 'POST':
        sender_name = request.form['sender_name']
        if 'anonymousCheckbox' in request.form:
            sender_name = "Anonymous"
        content = request.form['content']
        send_message(sender_name, content, scholar_id)
        return redirect(url_for('profile', scholar_id=scholar_id))
    
def get_messages(recipient_id):
    messages = []
    with open('messages.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        if not any(reader):
            return messages
        file.seek(0)
        next(reader)  
        for row in reader:
            row = [element.strip() for element in row]
            if not row:
                continue
            sender_name, message_content, timestamp, msg_recipient_id = row
            if msg_recipient_id == str(recipient_id):
                sender_name = re.sub(r'""', '"', sender_name)
                message_content = re.sub(r'""', '"', message_content)
                messages.append({'sender_name': sender_name, 'message_content': message_content, 'timestamp': timestamp, 'recipient_id': msg_recipient_id})
    return messages
    
@app.route('/inbox/<int:scholar_id>')
def inbox(scholar_id):
    if not session.get('logged_in') or session.get('scholar_id') != scholar_id:
        return redirect(url_for('login'))
    messages = get_messages(scholar_id)
    scholar = scholars.get(scholar_id)
    message_count = len(messages)
    return render_template('inbox.html', scholar=scholar, scholar_id=scholar_id, messages=messages, message_count=message_count)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/profile/<int:scholar_id>', methods=['GET', 'POST'])
def profile(scholar_id):
    scholar = scholars.get(scholar_id)
    if request.method == 'POST':
        sender_name = request.form['sender_name']
        recipient_id = scholar_id
        content = request.form['content']
        send_message(sender_name, content, recipient_id)
        return redirect(url_for('home'))
    else:
        if scholar:
            return render_template('profile.html', scholar=scholar, scholar_id=scholar_id)
        else:
            return 'Scholar not found', 404

@app.route('/home') 
def home():
    return render_template("home.html", scholar_id=scholar_id)

@app.route('/')
@app.route('/message')
def message():
    return render_template('message.html', scholar_id=scholar_id, scholars=scholars)

@app.route('/login')
def loginpage():
    return render_template('login.html', scholar_id=scholar_id)

if __name__ == "__main__": 
    serve(app, host="0.0.0.0", port=8000)