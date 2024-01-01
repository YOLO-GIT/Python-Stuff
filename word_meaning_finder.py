import requests
import webbrowser

DATAMUSE_API_BASE_URL = 'https://api.datamuse.com/words'


def get_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meanings = []

        for entry in data:
            for meaning in entry['meanings']:
                part_of_speech = meaning.get('partOfSpeech', 'N/A')
                definitions = meaning.get('definitions', [])

                for definition in definitions:
                    meanings.append({
                        'part_of_speech': part_of_speech,
                        'definition': definition.get('definition', 'N/A'),
                    })

        return meanings
    else:
        return None


def get_synonyms(word):
    params = {'rel_syn': word}
    response = requests.get(DATAMUSE_API_BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        synonyms = [item['word'] for item in data]
        return synonyms[:3]  # Limiting to the top 3 synonyms
    else:
        return []


def display_meanings_and_synonyms_html(word, meanings, synonyms):
    html_content = f"""
        <html>
        <head>
            <title>Word Meaning and Synonym Finder</title>
        </head>
        <body>
            <h1>Meanings of '{word}':</h1>
            <ul>
        """

    for index, meaning in enumerate(meanings[:15], start=1):
        html_content += f"<li>({meaning['part_of_speech']}) {meaning['definition']}</li>"

    html_content += """
            </ul>
            <h1>Top 3 Synonyms:</h1>
            <p>
        """

    if synonyms:
        html_content += ", ".join(synonyms)
    else:
        html_content += "N/A"

    html_content += """
            </p>
        </body>
        </html>
        """

    with open("word_meaning_and_synonyms.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    webbrowser.open("word_meaning_and_synonyms.html")


def main():
    print("Welcome to the Word Meaning and Synonym Finder!")

    while True:
        user_input = input("Enter a word (or 'exit' to quit): ").lower()

        if user_input == 'exit':
            print("Goodbye!")
            break

        meanings = get_word_meaning(user_input)
        synonyms = get_synonyms(user_input)

        if meanings:
            display_meanings_and_synonyms_html(user_input, meanings, synonyms)
        else:
            print("Word not found. Please try another word.")


if __name__ == "__main__":
    main()
