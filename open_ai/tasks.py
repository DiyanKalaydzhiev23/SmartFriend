import openai as openai

from SmartFriend.helpers import MAKE_SUMMARY, OPENING_TEXT, BONUS_CONDITION


def get_response(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )

    print(response.choices[0].message.content)

    return response.choices[0].message.content


def start_conversation(summary):
    conversation = [
        {
            'role': 'system',
            'content': BONUS_CONDITION + " " + summary + " " + OPENING_TEXT ,
        }
    ]

    return conversation


def post_summary(conversation):
    if conversation:
        result = {
            'role': 'system',
            'content': MAKE_SUMMARY
        }

        return result

    return ""
