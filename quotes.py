import wikiquote
import random
import syllables
from wikiquote import DisambiguationPageException


def find_quotes():
    i = 0
    haiku = []
    while i < 3:
        quote_index = wikiquote.random_titles()
        try:
            quotes = wikiquote.quotes(random.choice(quote_index))
        except DisambiguationPageException as e:
            quotes = wikiquote.qotd()
        while not quotes:
            quotes = wikiquote.quotes(random.choice(quote_index))
        syl = 0
        line = ""
        for word in quotes[0].split(" "):
            if "." in word:
                syl += syllables.estimate(word)
                line += word
                line += " "
                break
            syl += syllables.estimate(word)
            line += word
            line += " "

        if syl is 5 and len(haiku) < 2:
            haiku.insert(0, line)
            i += 1
        elif syl is 7:
            haiku.insert(1, line)
            i += 1

    for line in haiku:
        print(line)


find_quotes()
