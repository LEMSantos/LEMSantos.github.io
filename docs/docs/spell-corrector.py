from collections import Counter

LETTERS = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'

VOCABULARY = Counter()
TOTAL_WORDS = 0


def read_vocabulary():
    with open('vocabulary.txt') as vocab_file:
        lines = vocab_file.read().splitlines()

    full_vocab = [line.split() for line in lines]
    words_counter = Counter({word: int(count) for word, count in full_vocab})

    return sum(words_counter.values()), words_counter


def probability_of_word(word):
    return VOCABULARY[word] / TOTAL_WORDS


def generate_by_insert(word):
    generated_words = set()

    for pos in range(len(word) + 1):
        for letter in LETTERS:
            generated_words.add(word[:pos] + letter + word[pos:])

    return generated_words


def generated_by_delete(word):
    generated_words = set()

    for pos in range(len(word) + 1):
        generated_words.add(word[:pos] + word[pos + 1:])

    return generated_words


def generate_by_replace(word):
    generated_words = set()

    for pos in range(len(word) + 1):
        for letter in LETTERS:
            generated_words.add(word[:pos] + letter + word[pos + 1:])

    return generated_words


def generate_by_swap(word):
    generated_words = set()

    for pos in range(len(word) - 1):
        generated_words.add(
            word[:pos] + word[pos + 1] + word[pos] + word[pos + 2:]
        )

    return generated_words


def known_words(words_set):
    vocabulary_words = set(VOCABULARY.keys())
    return words_set & vocabulary_words


def words_generator_1_dist(word):
    inserts = generate_by_insert(word)
    deletes = generated_by_delete(word)
    replaces = generate_by_replace(word)
    swaps = generate_by_swap(word)

    return inserts | deletes | replaces | swaps


def words_generator_2_dist(word):
    words_2_dist = set()

    for new_word in words_generator_1_dist(word):
        words_2_dist |= words_generator_1_dist(new_word)

    return words_2_dist


def candidates(misspelled_word):
    return (known_words({misspelled_word}) or
            known_words(words_generator_1_dist(misspelled_word)) or
            known_words(words_generator_2_dist(misspelled_word)) or
            {misspelled_word})


def correct(misspelled_word):
    return max(candidates(misspelled_word), key=probability_of_word)


TOTAL_WORDS, VOCABULARY = read_vocabulary()

if __name__ == '__main__':

    misspelled_word = input('Digite a palavra incorreta: ')
    print('Correção:', correct(misspelled_word))
