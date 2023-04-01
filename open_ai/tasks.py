import openai as openai
from SmartFriend.helpers import OPENING_TEXT, MAKE_SUMMARY


def get_response_from_text(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )

    print(response.choices[0].message.content)

    return response.choices[0].message.content


def get_summary(conversation):
    text = MAKE_SUMMARY + "".join(conversation)

    # response = openai.ChatCompletion.create(
    #     model="text-davinci-003",
    #     prompt=text,
    #     temperature=0.5,
    # )
    #
    # return response.choices[0].text
