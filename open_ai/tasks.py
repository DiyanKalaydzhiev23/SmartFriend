import openai as openai


def get_response_from_text(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.5,
    )

    return response.choices[0].text

