from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import markovify
import random
import textwrap
import datetime
import facebook
import time
import planet_generation
import name_generation


# generate a horoscope using markov chains
def generate_horoscope():
    with open("texts/quotes.txt", encoding="utf8") as sample:
        text = sample.read()
    text_model = markovify.Text(text, state_size=2)
    sentence = None
    while sentence == None:
        sentence = text_model.make_short_sentence(208)
    return sentence


# return a radom number with a color
def rand_number_color():
    number = random.randint(0,100)
    if number<=20 : color='red'
    elif number>20 and number <60 : color='orange'
    else : color='green'
    return (str(number),color)


# get the x axis for the text to be centred
def centre_text(text, font_type, image_draw):
        text_width, text_height = image_draw.textsize(text, font_type)
        return (1200 - text_width) / 2


# add Stroke to text
def stroke_text(image, font, text, color , width, height,stroke_color):
    draw = ImageDraw.Draw(image)
    z = width
    t = height
    draw.multiline_text((z - 1, t), text, font=font, fill=stroke_color)
    draw.multiline_text((z + 1, t), text, font=font, fill=stroke_color)
    draw.multiline_text((z, t - 1), text, font=font, fill=stroke_color)
    draw.multiline_text((z, t + 1), text, font=font, fill=stroke_color)
    draw.multiline_text((z,t), text, color, font=font)
    return image


# break long lines to multiple small lines
def break_line(image,max_lines,text,x,text_width):
    y = 350
    i = 0
    for line in textwrap.wrap(text, width=text_width):
        i += 1
        if i > max_lines: break
        stroke_text(image,ImageFont.truetype('fonts/normal_font.ttf', size=30) , line, color="white", width=x, height=y, stroke_color="black")
        y += 30


# uhhh sorry u have to see this mess , to sum it up this function that draw the posts pics.
def make_pic(sign):
    query = random.choice(["universe","space","galaxy","stars","night-sky"])
    response = requests.get(f"https://source.unsplash.com/featured/?{query}")
    image = Image.open(BytesIO(response.content))
    #image = Image.open("galaxytest.jpg")
    image=image.resize((1200, 800))
    xray_image = Image.open("pics/filter.jpg").convert("RGBA")
    xray_image.putalpha(220)  # make pic transparent
    image.paste(xray_image,(25, 25),mask=xray_image)
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype('fonts/signs_font.ttf', size=130) #signs font
    font2=  ImageFont.truetype('fonts/normal_font.ttf', size=60) # planet font
    font3= ImageFont.truetype('fonts/normal_font.ttf', size=30) # planet info font
    font4= ImageFont.truetype('fonts/titles_font.otf', size=70) #big titles font
    font5= ImageFont.truetype('fonts/normal_font.ttf', size=50) #numbers font

    stroke_text(image, font, sign, color="#620E0E" ,width=centre_text(sign, font, d), height=20,stroke_color="black")
    d.multiline_text((centre_text(ruler_planet(sign), font2, d), 130), ruler_planet(sign), font=font2, fill='black',align='left')
    info_planet=planet_info(ruler_planet(sign))
    d.multiline_text((centre_text(f"(Longitude : {info_planet[0]} - Position : {info_planet[1]} - Degree : {info_planet[2]})", font3, d), 198), f"(Longitude : {info_planet[0]} - Position : {info_planet[1]} - Degree : {info_planet[2]})", font=font3, fill='black',align='left')
    stroke_text(image, font4, "Horoscope:", color="#A8A35A", width=75, height=280,stroke_color="black")
    stroke_text(image, font4, "Compatibility:", color="#A8A35A", width=740, height=280, stroke_color="black")
    stroke_text(image, font4, "Luck:", color="#A8A35A", width=75, height=527, stroke_color="black")

    break_line(image=image,max_lines=5, text=f"{generate_horoscope()} {generate_horoscope()} {generate_horoscope()}", x=75,text_width=46)
    stroke_text(image, font5, "Money:", color="white", width=75, height=595, stroke_color="black")
    money_number=rand_number_color()
    stroke_text(image, font2, f"{money_number[0]}%", color=money_number[1], width=250, height=587, stroke_color="black")
    stroke_text(image, font5, "Love:", color="white", width=75, height=685, stroke_color="black")
    love_number=rand_number_color()
    stroke_text(image, font2, f"{love_number[0]}%", color=love_number[1], width=250, height=677, stroke_color="black")
    stroke_text(image, font5, "Life:", color="white", width=380, height=595, stroke_color="black")
    life_number=rand_number_color()
    stroke_text(image, font2, f"{life_number[0]}%", color=life_number[1], width=580, height=587, stroke_color="black")
    stroke_text(image, font5, f"{random_cursed_word()}: ", color="white", width=380, height=685, stroke_color="black")
    other_number=rand_number_color()
    stroke_text(image, font2, f"{other_number[0]}%", color=other_number[1], width=580, height=677, stroke_color="black")

    break_line(image=image,max_lines=2, text=f'Today you are compatible with "{get_source_image()}".', x=740,text_width=30)

    source_image = Image.open("source image.png")
    source_image.thumbnail((350, 310),Image.ANTIALIAS)
    si_width, si_height = source_image.size
    x_paste = int(937 - (si_width / 2))
    y_paste = int(585 - (si_height / 2))
    image.paste(source_image, (x_paste, y_paste), mask=source_image)
    image.save('finished.png', quality=95)




# function to comment with a picture
def comment_pic(path, id,message):
    params = (("message", message ),("access_token", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" ),)
    files = {"source": (path.split("/")[-1], open(path,"rb"), "application/vnd.ms-excel", {"Expires": "0"})}
    requests.post(f"https://graph.facebook.com/v7.0/{id}/comments", params=params, files=files)


# get a random cursed word from nearly 100 wordsXX
def random_cursed_word():
    words=["Food","Hero","Dildo","Daddy","Sluty","Drunk","PP","Weed","Sad","Happy","Satan","Evil","Angel","The game","ISIS","Vodka","Brazzers","Gaming","Oof","Cum","Piss","Pussy","Dick","Poop","69","Ass","Obama","Trump","Bruh","Based","King","Queen","Hoe","USSR","Tiktok","Pornhub","Penis","Balls","Onlyfans","Memes","Anime","Hentai","Loser", "Dead","Racist","Tits","Chlong","Honk","Bonk","Idiot","Bitch","Shit","Fun","Mood","Bastard","MF","MILF","Incest","Anal","Sex","Work","Job","Fuck","Ok","Yeah","Potato","No","Gay","Trans","Kim jong","Insta","Family","Friends"]
    return random.choice(words)


#get the signs emoji
def sign_to_emoji(sign):
    dictionnary = {"aries": "♈", "taurus": "♉", "gemini": "♊", "cancer": "♋", "leo": "♌", "virgo": "♍", "libra": "♎","scorpio": "♏", "sagittarius": "♐", "capricorn": "♑", "aquarius": "♒", "pisces": "♓"}
    return dictionnary[sign]


# this fuction used to reply to comments commands
def reply_to_comment(text,id):
    if text == '!horoscope':
        graph.put_object(parent_object=id, connection_name='comments', message=f'{generate_horoscope()} {generate_horoscope()} {generate_horoscope()}')
        print(f"commented ({id}) {text} {datetime.datetime.now().strftime('the %d-%m-%Y at %H:%M')}")
    elif text == '!luck' :
        graph.put_object(parent_object=id, connection_name='comments',message=f'💰Money: {str(random.randint(0,101))}%\n🌟Life: {str(random.randint(0,101))}%\n❤Love: {str(random.randint(0,101))}%\n😳{random_cursed_word()}: {str(random.randint(0,101))}%')
        print(f"commented ({id}) {text} {datetime.datetime.now().strftime('the %d-%m-%Y at %H:%M')}")
    elif text == "!aries" or text == "!taurus" or text == "!gemini" or text =="!cancer" or text =="!leo" or text =="!virgo" or text =="!libra" or text =="!scorpio" or text =="!sagittarius" or text =="!capricorn" or text =="!aquarius" or text =="!pisces":
        horoscope_request = requests.post('https://aztro.sameerkumar.website/', params=(('sign', f'{text[1:]}'), ('day', 'today'),))
        graph.put_object(parent_object= id, connection_name='comments',message=f"{sign_to_emoji(text[1:])}{horoscope_request.json()['description']}{sign_to_emoji(text[1:])}")
        print(f"commented ({id}) {text} {datetime.datetime.now().strftime('the %d-%m-%Y at %H:%M')}")
    elif text == "!compatibility":
        comment_pic("source image.png", id, f'Omg you are compatible with "{get_source_image()}".')
        print(f"commented ({id}) {text} {datetime.datetime.now().strftime('the %d-%m-%Y at %H:%M')}")
    elif text == "!planet":
        planet_name = planet_generation.create_image(name_generation.generate_name())
        advise=requests.get('https://api.adviceslip.com/advice').json()["slip"]["advice"]
        comment_pic("planet.png", id, f"Your ruler planet is {planet_name.upper()}.\nit has an advise for you !\n-{advise} ")
        print(f"commented ({id}) {text} {datetime.datetime.now().strftime('the %d-%m-%Y at %H:%M')}")


# get a random source image from SPB
def get_source_image():
    r = requests.get('https://www.shitpostbot.com/api/randsource')
    response = requests.get("https://www.shitpostbot.com/" + r.json()['sub']['img']['full'])
    source_image = Image.open(BytesIO(response.content)).convert("RGBA")
    source_image.save('source image.png', quality=95)
    return r.json()['sub']['name']


# get the real logitude, position and degree of a given planet in a given time
def planet_info(name):
    Palnets_ids=["Sun" ,"Moon", "Mercury" ,"Venus", "Mars", "Jupiter" ,"Saturn"]
    params = {"ayanamsa": "1", "chart_type": "`rasi`","datetime": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00'),"coordinates": "10.214747,78.097626", }
    headers = {"Authorization": "Here is the api authorization key", }
    b = requests.get('https://api.prokerala.com/v1/astrology/planet-position', headers=headers, params=params).json()['response']['planet_positions'][Palnets_ids.index(name)]
    return [b['longitude'], b['position'], b['degree']]


# get the apoopiriet ruler planet for a given sign
def ruler_planet(sign):
    dictionnary = {"aries":"Mars", "taurus":"Venus", "gemini":"Mercury", "cancer":"Moon", "leo":"Sun", "virgo":"Mercury", "libra":"Venus", "scorpio":"Mars", "sagittarius":"Jupiter", "capricorn":"Saturn","aquarius":"Saturn", "pisces": "Jupiter"}
    return dictionnary[sign]


if __name__ == '__main__':
    i = random.randint(0,11)
    token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    graph = facebook.GraphAPI(token)
    signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn",
             "aquarius", "pisces"]
    ruler = ["Mars", "Venus", "Mercury", "Moon", "Sun", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Saturn",
             "Jupiter"]
    while True:
        if i == 12: i = 0
        signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn","aquarius", "pisces"]
        black_list = set()
        the_sign=signs[i]
        make_pic(the_sign)
        msg=f'{sign_to_emoji(the_sign)} {the_sign.capitalize()} horoscope for today the {datetime.datetime.now().strftime("%d-%m-%Y")}.\nYou can try the bot comments commands.(check all the available commandes on the first comment.)'
        while True:
            try:
                post_id = graph.put_photo(image=open('finished.png', 'rb'), message=msg)["post_id"]
                print(f'posted ({post_id}) {datetime.datetime.now().strftime("the %d-%m-%Y at %H:%M")}')
                comment_pic("pics/commands_example.jpeg", post_id, '🔴COMMENTS COMMANDS🔴\nComment with any of this commandes and i will reply to you .\n\t🧿 "!horoscope" : to generate a horoscope , just for you.\n\t🍀 "!luck" :  to check your luck!\n\t❤ "!compatibility" : find who you are compatible with.\n\t🪐 "!planet" : everyone has a single unique planet that rules you destiny , Find out about it and what it’s advice to you ! (Actually that’s just a randomly generated planet with a randomly generated name and a random advice , but hey try it , it’s fun !)\n\t♋ "!{Your zodiac sign}" : (example : !aries) enough from the bot generated content , with this command you can check your real horoscope of this day .')
                print(f'commented ({post_id}) {datetime.datetime.now().strftime("the %d-%m-%Y at %H:%M")}')
                break
            except:
                print("posting error occured")
        timeNow = 0
        sleep_secondes = 15
        data_length = 0
        data=[]
        while timeNow <60:
            try:
                data = graph.get_connections(id=post_id, connection_name='comments')['data']
                if len(data) > 0:
                    for j in data:
                        if j['id'] not in black_list:
                            black_list.add(j['id'])
                            text = graph.get_object(id=j['id'], fields='message')['message']
                            reply_to_comment(text.lower(), j['id'])
                            time.sleep(5)
                            timeNow += 5
            except:
                print("error while getting data or while commenting")

            if len(data) > data_length : sleep_secondes = 15
            else:
                if sleep_secondes <= 240: sleep_secondes += 2
            data_length = len(data)
            print(f"going time sleep for {sleep_secondes} secondes")
            time.sleep(sleep_secondes)
            timeNow += sleep_secondes
        i += 1
