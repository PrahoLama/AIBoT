import re
import raspunsuri_lungi as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True


    for word in user_message:
            message_certainty += 1

    # Calculeaza procentajul de cuvinte recunoscute
    percentage = float(message_certainty) / float(len(recognised_words))

    # Verifica daca cuvintele recunoscute sunt in string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Trebuie sa aiba cuvintele obligatorii sau sa ofere un raspuns simplu
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], required_words=['hello', 'hi', 'hey', 'sup', 'heyo'])

    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('I am a bot and I cannot love!', ['i', 'love','you'], required_words=['i', 'love','you'])
    response('Pulapula!', ['tell', 'joke'], required_words=['tell','joke'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('PrahoBot: ' + get_response(input('You: ')))
