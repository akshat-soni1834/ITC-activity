def check_message_length(message):
    if len(message) <= 200:
        return message
    else:
        return message[:200]
print(check_message_length(''))
def check_message_word_count(message):
    words = message.split()
    if len(words) <= 30:
        return message
    else:
        return "Message should not contain more than 30 words."