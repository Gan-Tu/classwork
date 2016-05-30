"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    counter, score, zero_rolled = 0, 0, False
    while counter < num_rolls:
        outcome = dice()
        if outcome == 1: zero_rolled = True
        score += outcome
        counter += 1
    if zero_rolled: return 0
    else: return score


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    score = 0
    if num_rolls == 0:
        "Free Bacon"
        score = max(opponent_score%10,opponent_score//10,opponent_score//100)+1
    else:
        score = roll_dice(num_rolls,dice)
    "Return result based on Hogtimus Prime"
    if is_prime(score): return next_prime(score)
    else: return score


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    if (score + opponent_score) % 7 == 0 : return four_sided
    else: return six_sided


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    score0, score1 = score0%100, score1%100 #only take last two digits
    if score1%10 == score0//10 and score0%10 == score1//10: return True
    else: return False


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    while score0 < goal and score1 < goal:
        if player ==0:
            num_rolls, dice= strategy0(score0,score1), select_dice(score0,score1)
            score = take_turn(num_rolls,score1,dice)
            score0 += score
            if score == 0: score1 += num_rolls
        else:
            num_rolls, dice= strategy1(score1,score0), select_dice(score1,score0)
            score = take_turn(num_rolls,score0,dice)
            score1 += score
            if score == 0: score0 += num_rolls
        if is_swap(score0,score1):
            score0, score1 = score1, score0
        player = other(player)
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


# Experiments

def make_averaged(fn, num_samples=100):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    def f(*args):
        sum, counter = 0,0
        while counter < num_samples:
            sum += fn(*args)
            counter +=1
        return sum/num_samples
    return f


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    best_num_rolls = 1 # set default
    highest_average_return = make_averaged(roll_dice, num_samples)(best_num_rolls,dice)
    for num_rolls in range(2,11):
        score = make_averaged(roll_dice, num_samples)(num_rolls,dice)
        if score > highest_average_return:
            highest_average_return, best_num_rolls = score, num_rolls
    return best_num_rolls


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    possible_score = max(opponent_score%10,opponent_score//10,opponent_score//10)+1
    if is_prime(possible_score): possible_score = next_prime(possible_score)
    if possible_score >= margin: return 0
    else: return num_rolls


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    possible_score = max(opponent_score%10,opponent_score//10,opponent_score//10)+1
    if is_prime(possible_score): possible_score = next_prime(possible_score)
    possible_score += score
    if is_swap(possible_score,opponent_score) and possible_score < opponent_score: return 0
    else: return num_rolls

def final_strategy(score, opponent_score):
    """This is my final strategy for winning:
    """
    #Parameters
    is_six_sided = (select_dice(score,opponent_score) == six_sided)
    if is_six_sided: safe_play, margin = 4, 8
    else: safe_play, margin = 2, 3
    
    has_bad_swap = False
    bad_swap_safe_play = 1
    adventure_margin = 35
    if is_six_sided: adventure_play = 7
    else: adventure_play= 4
    
    def get_largest_digit(x):
        return max(x%10,x//10%10,x//100)

    def get_bacon_score(opponent_score):
        digit = get_largest_digit(opponent_score) + 1
        if is_prime(digit): return next_prime(digit)
        return digit
    
    #Strategy
    if is_swap(score+get_bacon_score(opponent_score),opponent_score):
        roll = swap_strategy(score,opponent_score,safe_play)
        if roll == safe_play: has_bad_swap = True
    else:
        roll = bacon_strategy(score, opponent_score, margin, safe_play)

    if roll == 0: return 0
    elif score - opponent_score >=10 and not has_bad_swap: return 0
    elif score - opponent_score >=10 and has_bad_swap: return bad_swap_safe_play
    elif opponent_score - score >= adventure_margin: return adventure_play
    else: return roll

# Helper Functions
def is_prime(x):
    "Check if a number is prime. Return true if it is; false otherwise"
    if x<=1: return False
    for factor in range(2,x): #check to make sure no factors 2<=n<=n-1
        if x % factor == 0: return False
    return True

def next_prime(x):
    "Find the next prime number that's bigger than x"
    x += 1
    while not is_prime(x):
        x += 1
    return x

##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
