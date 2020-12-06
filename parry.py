import random
import re
from termcolor import colored

name = "Parry"
weather = "cloudy"
bot_template = "BOT : {0}"
user_template = "USER : {0}"
# Colere 0 = neutre, -infini = calme et +infini = énervé
colere = 0
i = 0
rules = {
    'I want (.*)': 
        ['What would it mean if you got {0}','Why do you want {0}',"What's stopping you from getting {0}"],
    'do you remember (.*)': 
        ['Did you think I would forget {0}',"Why haven't you been able to forget {0}",'What about {0}','Yes .. and?'],
    'do you think (.*)': 
        ['if {0}? Absolutely.', 'No chance'],
    'if (.*)': 
        ["Do you really think it's likely that {0}",'Do you wish that {0}','What do you think about {0}','Really--if {0}'],
    'You are beautifull (.*)':
        ["Moooh thank you ! ",'You to !'],
    '(.*) mafia (.*)':
        ["I think is'nt a good idea to speak about this","I don't like this subject"],
    '(.*) murder (.*)':
        ["I think is'nt a good idea to speak about this","I don't like this subject"],
    'colere=20':
        ["You pissed me off, don't talk with me","Ok, you can go talk with an other person please","If you not stop..."],
    'colere=30':
        ["I will kill you","I will kill all your family","I hate you, I just want see you dead"],
    '(.*) murder (.*)':
        ["Why you talk about a murder ?","We can talk about other ? I don't like"]
}

# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern,message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response.format(phrase)

# Test match_rule
print("------------TEST MATCH RULE---------------")
print(match_rule(rules, "do you remember your last birthday"))

# Define replace_pronouns()
def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub("me","you",message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub("my","your",message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub("your","my",message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub("you","me",message)
    return message
print("----------TEST REPLACE PRONOUNS-----------")
print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))

# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules,message),message
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

def send_message(message):
    global colere
    # Print user_template including the user_message
    print(colored(user_template.format(message),"yellow"))
    # Test love
    if (check_emotion(message) == False):
        colere -= 1
    if(colere >= 10 and colere <= 20):
        message = "colere=20"
    if(colere > 20):
        message = "colere=30"
    # Get the bot's response to the message
    response = respond(message)
    if(colere > 3):
        response = response + "!"
    # Print the bot template including the bot's response.
    print(colored(bot_template.format(response),"green"))


def check_emotion(message):
    message = message.lower()
    global colere
    global i
    menace = False
    # Just for test
    if 'beranger' in message:
        colere += 30
        menace = True
    if '!!!' in message:
        colere += 2
        menace = True
    if 'mafia' in message:
        colere += 5
        menace = True
    if 'murder' in message:
        colere += 10
        menace = True
    if 'calm' in message:
        colere -= 10
    if 'sorry' in message:
        colere -= 5
    # Parry don't like when user asking many questions 
    if '?' in message:
        i += 1
        if(i >= 3):
            colere += 3
            menace = True
            i = 0
            print(colored(bot_template.format("You are a cops ? Stop asking questions !"),"green"))
    print(colored("Etat de la colère : " + str(colere),"red"))
    return menace



# Send the messages
print("---------------SEND MESSAGE---------------")
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")
send_message("You are beautifull Eliza !")
send_message("You know the mafia ?")
send_message("I want your name !!!!!")
send_message("You like the mafia ?")
send_message("You want go to the mafia ?")
send_message("You know hugo beranger ?")
send_message("Sorry, please stay calm")
print("------------------------------------------")
