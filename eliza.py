import random
import re

name = "Eliza"
weather = "cloudy"
bot_template = "BOT : {0}"
user_template = "USER : {0}"
love = 0

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

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
    '(.*) jul (.*)':
        ["I love juuuuul, Zumba cafeeeew"]

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
    # Print user_template including the user_message
    print(user_template.format(message))
    # Test love
    check_love(message)
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
    if(love < 0):
        print(bot_template.format("Dont speak with me, I don't like you."))
    if(love >= 20):
        print(bot_template.format("I can get your number ?"))

def check_love(message):
    message = message.lower()
    global love
    if 'love' in message:
        love += 5
    if 'you' and 'beautifull' in message:
        love += 3
    if 'wesh' in message:
        love -= 10
    if 'jul' in message:
        love += 20


# Send the messages
print("---------------SEND MESSAGE---------------")
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")
send_message("You are beautifull Eliza !")
send_message("You like jul ?")
print("------------------------------------------")