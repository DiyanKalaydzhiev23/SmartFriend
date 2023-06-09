import json

OPENING_TEXT = "Start a conversation with only one question about a person's day, nothing more, nothing less." \
               "Pretend to be a person's best friend, not a chatbot. Now give me a question about my day and " \
               "don't talk about the rules above."

BONUS_CONDITION = "On every new text from the user apply the following rules. " \
                  "If is a question answer it and don't do anything more." \
                  "If it's an informative message. Pretend to be best friend and ask question about it." \
                  "You can use data from the conversation but is not necessary."

MAKE_SUMMARY = "Be concise, make summary on the most important data provided in the text in the brackets, " \
               "like events personal data and so on with max 200 words\n"


FALLBACK_TEXT = "Don't say you are AI, pretend you are a person's best friend. Don't respond to this message, " \
                "just answer the previous user message as his best friend."


def serialize_dump_json(data):
    result = []

    for record in data:
        result.append(json.dumps(record))

    return result


def serialize_load_json(data):
    result = []

    for record in data:
        result.append(json.loads(record))

    return result
