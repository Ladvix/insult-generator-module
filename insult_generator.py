from random import choice, randint


insults = "бык,коронавирус,клоун,кукан,танк,вертолёт,велосипед,батя,братик,процессор,мешок,пакет,коврик,коврижка,чебурек,питон,кал,пёс,инцел,виртуалбокс,долбаёб,долбоёб,далбоёб,планктон,мефедрон,снюс,камаз,туалет,толкан,томат,огурец,банан,ебанан,баклан,ваз-2101,линукс,спрей,поносик,ворон,мусор,понос,помой,карась,хуй,таракан,урод,шпорк,баклажан,овощ,фрукт,сахарок,барсик,пупс,неосарт,линуксоид,виндузятник,маковод,туалет,толкан,толчок,пепел,краб,макинтош,дельфин,трюфель,бсдшник,цыган,чмо,пидор,задрот,кисель,ботан,гандонео,пушок,зефир,негативчик,быдлан,третьеклассник,газ,еблан,уёбок,пидорас,гандон,педик,презик,волос,негр,убунтовод,арчегомосек,шоколад,козёл,бычара,козлище,козён,обама,навальнёнок,говноед,трамп,гей,гомосек,свин,кобель,хохол,сатана".split(",")
adjectives = "ебаный,обоссаный,поднадусёровый,слабонервный,жирный,вонючий,кастрированный,ебучий,невменяемый,блядский,черномазый,оттраханный,обдроченный".split(",")
geninsult_first = "блядо,члено,говно,хуе,желто,черно,много,верто,мало,швайно,глино,гнидо,писько,сопле,криво,пидо,пердо,срало,срано,порно,без".split(",")
geninsult_second = "рылый,жопый,ротый,ебливый,ссущий,срущий,ухий,клювый,зубый,хвостый,бля".split(",")
geninsult_endings = "лёт,ед,блюй,рот,член,мес,пидор,поезд,танк,дроч,скотч,крейсер,дрочер,дорас".split(",")
abusives = "блять,сука,ебать,пиздец,нахуй".split(",")
dick_adjectives = "трахо,ебо,сексо,порно,конче,негро".split(",")
dicks = "член,штырь,штепсель,кол,баклажан,трон,дик,ствол,крючок,питон,пайтон,шланг,кол".split(",")
demonstrative_verbs = "иди,пиздуй,шуруй,вали,ебись".split(",")
verbs = "утопил,отравил говном,переехал,на суп спустил,похоронил,из репозиториев установил,в деб пакет засунул,в рпм опакетил,скомпилировал,ебал,зарезал,продал за 3 рубля,отпиздил,с балкона выбросил,стирал,высушил,отравил газом,насиловал,трахал,пиздил,ножом резал,на хую вертел,на хуе до 12000 об/с разгонял,ссал на,срал на,продал,купил,проиграл в казино,выиграл в казино,выебал,обосрал,оплодотворял,продавал на металлолом,сдавал на чермет,продавал в секс-рабство,вчера в гроб ложил".split(",")
relatives_impad = "мать,бабушку,сестру,бабку,мамку,тёщу,родню,пизду,ротовую полость,родину,деревню,сноху,дочь,дочку,одноклассницу,классную руководительницу,однокурсницу".split(",")
places = "нахуй,с обрыва,под землю,маме отсасывать,сестре отлизывать,бабушке отлизывать,маме помогать,в пизду,отсюда,к хуям,по помойкам шарить,у бати сосать,маме отлизывать,маме жаловаться,сглатывать,фистить себе жопу,глотать сперму,сосать".split(",")
whose = "мамкин,папкин,сосалкин,шалавкин,плюшкин".split(",")
relatives = "мать,мамка,бабка,бабушка,дочка,тёща,сноха,жена".split(",")
fem_insults = "шалава,лоханка,макака,обезьяна,шлюха,шаболда,сосалка,дура,молекула,хуйня,грязь,проститутка,пизда,махнатка,дырка,дыра,вонючка,конча,пылинка,хохлинка,корова,бабка,уродина,фиона,пепеляшка,акула,курица".split(",")
fem_adjectives = "ебаная,обосраная,мёртвая,вообще жива?,обоссаная,поднадусёровая,слабонервная,жирная,вонючая,кастрированная,ебучая,невменяемая,блядская,черномазая,оттраханая,обдроченная,конченая".split(",")
item_adjectives_fem = "широкая,огромная,мелкая,выебанная,гигантская,обдолбанная".split(",")
smileys = ["😆", "🤣", "😡", "🤬", "😈", "👿", "👺", "👹", "🤡", "🖕", "🤘", "😏", "🧠"]

insult = "Оскорбление не придумал"

def genlaugh():
    lg = ""
    parts = "Ах,АХ,ах,аХ,Аъ,пх,Пх,ПХ,пХ,аЪ,пз,".split(",")
    for x in range(randint(1, 20)):
        lg += choice(parts)
    return lg

def genscob():
    sc = ""
    scobs = "),0,-,_".split(",")
    for x in range(randint(1, 20)):
        sc += choice(scobs)
    return sc

def genins():
    way = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
    if way == 1:
        insult = f"{choice(demonstrative_verbs)} {choice(places)}, {choice(insults)} {choice(adjectives)}"
    elif way == 2:
        insult = f"{genlaugh()} {choice(abusives)} ты {choice(insults)} {choice(whose)}{genscob()}"
    elif way == 3:
        insult = f"пососи мой {choice(dick_adjectives)}{choice(dicks)}, {choice(adjectives)} {choice(whose)}"
    elif way == 4:
        insult = f"{choice(abusives)} ты {choice(geninsult_first)}{choice(geninsult_second)}"
    elif way == 5:
        insult = f"{choice(abusives)} ты {choice(geninsult_first)}{choice(geninsult_endings)}"
    elif way == 6:
        insult = f"{choice(demonstrative_verbs)} {choice(places)}, {choice(fem_insults)} {choice(fem_adjectives)}"
    elif way == 7:
        insult = f"{genlaugh()} {choice(abusives)} ты {choice(fem_insults)} {choice(whose)}{genscob()}"
    elif way == 8:
        insult = f"{genlaugh()} {choice(abusives)} у тебя {choice(fem_insults)} {choice(item_adjectives_fem)}"
    elif way == 9:
        insult = f"{choice(abusives)} ты {choice(geninsult_first)}{choice(geninsult_second)}"
    elif way == 10:
        insult = f"{choice(abusives)} ты {choice(geninsult_first)}{choice(geninsult_endings)}"
    elif way == 11:
        insult = f"да я твою {choice(relatives_impad)} {choice(verbs)}{genscob()} понимаешь???{genscob()}"
    elif way == 12:
        insult = f"я тебе щас {choice(insults)} в рот засуну, {choice(insults)} ты {choice(adjectives)}{genlaugh()}"
    elif way == 13:
        insult = f"да, твоя {choice(relatives)} {choice(fem_adjectives)}, а вот ты {choice(adjectives)} {choice(insults)}"
    elif way == 14:
        insult = f"слышь ты {choice(adjectives)} {choice(insults)} я твою {choice(relatives_impad)} {choice(verbs)}"
    elif way == 15:
        insult = f"судо апт уебать твоя-мама --причина=ты_{choice(abusives)}_{choice(adjectives)}_{choice(insults)}"
    elif way == 16:
        insult = f"пинг твоя-{choice(relatives)}... а чё не пингуется? а потому что я её {choice(verbs)}"
    elif way == 17:
        insult = f"ssh твоя{choice(relatives)}@{choice(insults)}... о {choice(abusives)} работает... ахаххахахаха тут пароль я-{choice(insults)}"
    elif way == 18:
        insult = f"приветик {choice(insults)} {choice(adjectives)} , давно не виделись, как помнишь ты {choice(verbs)} свою {choice(relatives_impad)}. так вот пока ты это делал я твою {choice(relatives_impad)} {choice(verbs)}"
    elif way == 19:
        insult = f"плавают {choice(insults)} и {choice(insults)}. и тут всплыла твоя {choice(relatives)}. один другого спрашивает: ты {choice(insults)}? а тот ему и отвечает: я твою{choice(relatives_impad)} {choice(verbs)}"
    elif way == 20:
        insult = f"шёл {choice(insults)} по лесу. видит - {choice(insults)} горит. ну он сел на него и выебал твою {choice(relatives_impad)}"
    elif way == 21:
        insult = f"ути ути ты мой {choice(insults)} маленький)) а ты знал что я твою ебаную {choice(relatives_impad)} вчера {choice(verbs)}?))"
    insult = insult.upper()
    insult += choice(smileys) * randint(0, 5)
    if choice([True, False]):
        insult += f" {choice(demonstrative_verbs)} {choice(places)}".upper() + choice(smileys) * randint(0, 6)
        if choice([True, False]):
            insult += f" {choice(insults)} {choice(adjectives)} {genlaugh()}".upper()
    return insult