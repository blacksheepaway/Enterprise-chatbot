def generate_response(user_message):
    if "hello" in user_message.lower():
        return "Hello my friend! How can we help you today?"
    elif "how are you" in user_message.lower():
        return "I'm doing great, thanks! And you?"
    elif "tell me more about this bot" in user_message.lower():
        return "Oh, about me? I was created by Edson Weslenn as part of his portfolio! He, as a Python enthusiast, thought the idea of creating me was really cool - and I hope you're enjoying the result!"
    elif "what can you do?" in user_message.lower():
        return "I can talk to humans, return menus and direct them to agents or online problem solving for your company!"
    else:
        return "I'm not sure I understand this message. Please try asking something else."
