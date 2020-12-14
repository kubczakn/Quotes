import wikiquote
import random
import cmudict
import string

d = cmudict.dict()


def nsyl(word):
    return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]


exclude = set(string.punctuation)


def find_quotes():
    i = 0
    haiku = []
    while i < 3:
        quote_index = wikiquote.random_titles()
        quotes = wikiquote.quotes(random.choice(quote_index))
        while quotes is 0:
            quotes = wikiquote.quotes(random.choice(quote_index))
        quote = quotes[0]
        syl = 0
        if i is 0 or 2:
            for word in quote.split():
                word = ''.join(ch for ch in word if ch not in exclude)
                word = word.replace(',', '')
                num = nsyl(word)
                if not nsyl(word):
                    syl += 5
                else:
                    syl += num[0]

            if syl is 5:
                haiku.insert(quote)
                ++i
        else:
            for word in quote.split():
                word = ''.join(ch for ch in word if ch not in exclude)
                word = word.replace(',', '')
                num = nsyl(word)
                if not nsyl(word):
                    syl += 5
                else:
                    syl += num[0]
            if syl is 7:
                haiku.insert(quote)
                ++i
    print(haiku)


find_quotes()
