"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    emp_lst = []
    for i in paragraphs: #check every element, i is the content of every element
        if select(i): #check select condition
            emp_lst.append(i) #put into the empty list
    if k >= len(emp_lst):
        return ''
    return emp_lst[k]



def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'

    def keyword(paragraphs):
        no_punctuation = remove_punctuation(paragraphs) #using utils function
        lower_case = lower(no_punctuation) #using utils function
        para_words = split(lower_case) #split every word to every element of list

        for i in para_words: #check every element, i is the content of every element
            if i in topic:
                return True
        return False
    return keyword



def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)

    correct_words = 0
    if len(typed_words) == 0:
        return 0.0
    for i in range(len(reference_words)):
        if i < len(typed_words) and reference_words[i] == typed_words[i]:
            correct_words += 1

    return correct_words / len(typed_words) * 100.0


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'

    if typed == '':
        return 0.0
    else:
        return (len(typed)/5)/(elapsed/60)



def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """

    if user_word in valid_words:
        return user_word
    word = ''
    least_diff = 100
    for i in range(len(valid_words)):
        distance = diff_function(user_word, valid_words[i], limit)
        if distance < least_diff:
            word = valid_words[i]
            least_diff = distance
    if least_diff <= limit:
        return word
    return user_word


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    def helper_function(tally, i):
        if limit < tally: #stop when reach the limit!
            return tally
        elif len(goal) == i or len(start) == i: #stop when reach the length
            return tally + abs(len(start) - len(goal))
        elif goal[i] == start[i]: #check every character
            return helper_function(tally,i+1) #next char
        else:
            return helper_function(tally+1,i+1) #count diff and next char
    return helper_function(0,0)


def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    if start == goal:
        return 0
    if limit == 0: #stop when reach the limit!
        return 1
    if not start:
        return len(goal)
    elif not goal:
        return len(start)
    elif start[0]== goal[0]:
        return edit_diff(start[1:], goal[1:],limit)
    else:
        add_char = 1 + edit_diff(goal[0]+ start,goal,limit-1)
        remove_char = 1  + edit_diff(start[1:],goal,limit-1)
        substitute_char = 1 + edit_diff(goal[0]+ start[1:], goal,limit-1)

    return min(add_char, remove_char, substitute_char)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    score = 0
    for i in range(len(typed)):
        if typed[i] == prompt[i]:
            score += 1
        else:
            break
    score_percent = score / len(prompt)
    send({'id': id, 'progress': score_percent})
    return score_percent


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0

    final_lst = [[] for i in range(n_players)]

    def timer(word_i, player_i):#find the time diff between two word
        return elapsed_time(word_times[player_i][word_i]) - elapsed_time(word_times[player_i][word_i-1])

    def fastest_time(word): #find the fastest time
        '''for i in range(len(n_words)): #put every fastest time to a list
            fastest_time_lst += min(timer(word,0),timer(word,1))'''
        pi_tm = []
        for p_i in range(n_players): #track every player
            pi_tm += [timer(word,p_i)]
        return min(pi_tm)

    final_list = []

    for player_i in range(n_players):
        player_lst = []
        for words_i in range(1,n_words+1):
            #print(timer(words_i,player_i))
            if timer(words_i,player_i) <= fastest_time(words_i) + margin:

                player_lst += [word(word_times[player_i][words_i])]
        final_list += [player_lst]

    return final_list


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
