from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB


def get_data():
    root = "data/"

    with open(root + 'amazon.txt', 'r') as text_file:
        data = text_file.read().split('\n')

    with open(root + 'imdb.txt', 'r') as text_file:
        data += text_file.read().split('\n')

    with open(root + 'amazon.txt', 'r') as text_file:
        data += text_file.read().split('\n')

    return data


def preprocess(data):
    processed_data = []
    for datum in data:
        if len(datum.split('\t')) == 2 and datum.split('\t')[1] != "":
            processed_data.append(datum.split('\t'))

    return processed_data


def split_data(data):
    total = len(data)
    training_ratio = 0.75
    training_data = []
    evaluation_data = []

    for indice in range(0, total):
        if indice < total * training_ratio:
            training_data.append(data[indice])
        else:
            evaluation_data.append(data[indice])

    return training_data, evaluation_data


def preprocess_step():
    data = get_data()
    processed_data = preprocess(data)

    return split_data(processed_data)


def training_step(data, vectorizer):
    training_text = [data[0] for data in data]
    training_result = [data[1] for data in data]

    training_text = vectorizer.fit_transform(training_text)

    return BernoulliNB().fit(training_text, training_result)


def get_training_data():
    data, evaluation_data = preprocess_step()
    return data


def analyse_text(text, training_data):
    vectorizer = CountVectorizer(binary='true')
    classifier = training_step(training_data, vectorizer)
    return text, classifier.predict(vectorizer.transform([text]))


def get_result(result):
    text, analysis_result = result
    res = 'Positive' if analysis_result[0] == '1' else 'Negative'
    return res

