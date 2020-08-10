# AstonomyBot

a facebook bot post 12 pictures a day (1 for each zodiac sign) 

## I) What do the pictures contain and how are they made? 
First the bot take a  high resolution space picture from unsplash.com
Then put on it the following things:
###- the ruller planet : 
every zodiac sign haz a planet that rules it . So in every pictures theres the appropriate planet for the zodiac sign and also the current information of the planet  (longitude , position , degree) these informations are real ( the only real thing in the picture the rest is generated ) that i get every time i post using an api.
- horoscope: a random generated horoscope using markov chain (the text sample is nearly 1500 quotes and real horoscopes)
- compatibility : wish is a random source image and it’s name
- luck : is represented as a % . The luck in 4 aspects ( 1)money - 2)life - 3)love -4) the fourth aspect is random word from a cursed list of words ). The luck is represented as a percentage. The percentage change ( red if luck <20% - orange if 20%<luck <60% - green if luck>60 %).

## II) COMMENTS COMMANDS
The bot has also the comments commands that the bot reply to them with the appropriate reply.
The commands are:
- !horoscope : to generate a unique horoscope for the commenter.
- !luck :  generate a unique luck for the commonter
- !compatibility : generate a random compatibility for the commenter !
- !planet : find the planet that controle the commenter life and destiny and what’s it’s advice for the commenter (actually it’s just generate a random planet pictures with randome generated name with a random advice (the advise is fetched using an api) ) 
- !{Your zodiac sign} : (example : !aries) give the actual horoscope of the choosen  sign for this day ( the horoscope is fetched using an api)


## III) HOW THE BOT IS RELATED TO THE SPACE THEME?
- uuuh i mean astrology is related to space
- the background of every picture is a space picture
- the bot generate planets and planets names
