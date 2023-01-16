# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

def ryerson_letter_grade(n): 
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(items):
    if len(items) <= 1:
        return True
    for ind, i in enumerate(items[0:-1]):
        if i >= items[ind+1]:
            return False
    return True

def riffle(items, out=True):
    new_list = items[:len(items) // 2]
    new_list_2 = items[len(items) // 2:]
    if len(items) == 0:
        return []
    if out:
        result = list(zip(new_list, new_list_2))
    else:
        result = list(zip(new_list_2, new_list))
    proper_result = [num for tuple_ in result for num in tuple_]
    return proper_result

def only_odd_digits(n):
    n = str(n)
    for i in n:
        if int(i)% 2 == 0:
            return False
    return True
    
def is_cyclops(n):
    if n == 0:
        return True
    if len(str(n)) % 2 == 0:
        return False
    n = str(n)
    middle = (len(n) - 1) // 2
    for ind, num in enumerate(n):
        if num != "0" and ind == middle or (num == "0" and ind != middle):
            return False
    return True

def domino_cycle(tiles):
    if tiles == []:
        return True
    enumerated = enumerate(tiles)
    for ind, (first, last) in enumerated:
        prev_tile = tiles[ind-1]
        prev_last = prev_tile[1]
        if prev_last != first:
            return False
    return True

def colour_trio(colours):
    def combinator(el_1, el_2):
        if el_1 == el_2:
            return el_1
        elif el_1 == "r":
            return "b" if el_2 == "y" else "y"
        elif el_1 == "y":
            return "r" if el_2 == "b" else "b"
        elif el_1 == "b":
            return "y" if el_2 == "r" else "r"

    answer = colours
    while len(answer) > 1:
        res = ""
        for ind, let in enumerate(answer[:-1]):
            next_let = answer[ind+1]
            res += combinator(let,next_let)
        answer = res
    return answer

def count_dominators(items):
    if len(items)< 2:
        return len(items)
    else: 
        dominators_count = 1
    reverse = list(reversed(items))
    temp_largest = items[-1]
    for el in reverse[1:]:
        if el > temp_largest:
            temp_largest = el
            dominators_count += 1
    return dominators_count

def extract_increasing(digits):
    current = 0
    previous = -1
    result = []

    for d in digits:
        d = int(d)
        current = 10 * current + d
        if current > previous:
            result.append(current)
            previous = current
            current = 0
    return result

def words_with_letters(words, letters):
    def subsequence(word, letters):
        if len(word) < len(letters):
            return False
        elif len(word) == 0:
            return False
        if letters == "" or word == letters:
            return True
        pos = 0
        for ch in word:
            if pos < len(letters) and ch == letters[pos]:
                pos += 1
        return pos == len(letters)

    result = []
    for word in words:
        if subsequence(word, letters):
            result.append(word)
    return result

def taxi_zum_zum(moves):
    x = 0
    y = 0
    pos = 0

    for move in moves:
        if move == "R":
            pos += 1
        if move == "L":
            pos -= 1
        if move == "F":
            if pos == 0:
                y += 1
            if pos == 1:
                x += 1
            if pos == 2:
                y -= 1
            if pos == 3:
                x -= 1
        if pos > 3:
            pos = 0
        elif pos < 0:
            pos = 3
    return (x, y)

def give_change(amount, coins):
    result = []
    if amount == 0:
        return result
    else:
        for coin in coins:
            check = amount % coin
            times = (amount - check) / coin
            result.extend([coin] * int(times))
            amount = check
    return result

def safe_squares_rooks(n, rooks):
    x_range = list(range(n))
    y_range = list(range(n))
    for x, y in rooks:
        if x in x_range:
            x_range.remove(x)
        if y in y_range:
            y_range.remove(y)
    result = int(len(x_range)) * int(len(y_range))
    return result

def words_with_given_shape(words, shape):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for word in words: 
        if len(word) != len(shape)+1:
            continue
        for ind in range(len(word) - 1): 
            let_curr = word[ind]
            let_next = word[ind+1]
            ind_curr = alphabet.index(let_curr)
            ind_next = alphabet.index(let_next)
            ind_check = 0
            if ind_next > ind_curr:
                ind_check = +1
            elif ind_next == ind_curr:
                ind_check = 0
            elif ind_next < ind_curr:
                ind_check = -1
            if ind_check != shape[ind]:
                break
        else:
            result.append(word)
    return result

def is_left_handed(pips):
    left = [[1, 2, 3], [3, 1, 2], [2, 3, 1], [1, 3, 5], [5, 1, 3], [3, 5, 1], [1, 4, 2], [2, 1, 4], [4, 2, 1], [1, 5, 4], [4, 1, 5], [5, 4, 1], [6, 3, 2], [2, 6, 3], [3, 2, 6], [6, 2, 4], [4, 6, 2], [2, 4, 6], [2, 6, 3], [3, 2, 6], [6, 3, 2], [6, 5, 3], [3, 6, 5], [5, 3, 6], [6, 4, 5], [5, 6, 4], [4, 5, 6]]
    if pips in left:
        return True
    else:
        return False

def winning_card(cards, trump=None):
    ranks = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
    enumerated = list(enumerate(cards))
    rank, suit = cards[0]
    if trump == None:
        trump = suit
    else:
        valid = [card for ind, card in enumerated if trump in card]
        if valid == []:
            trump = suit
    valid = [card for ind, card in enumerated if trump in card]
    max_valid = 0
    for rank, suit in valid:
        if max_valid < ranks[rank]:
            max_valid = ranks[rank]
        else:
            continue
    result = [rank for rank,num in ranks.items() if num == max_valid]
    return result[0], trump

def seven_zero(n):
    d = 1
    if n == 7:
        return n
    while True:
        if n % 2 != 0 and n % 5 != 0:
                curr = int(d * '7')
                if curr % n == 0:
                    return curr
                else:
                    d += 1
                    continue
        for k in range(1, d+1): 
            curr = int(k * '7' + (d - k) * '0')
            if curr % n == 0:
                return curr
        d += 1

def can_balance(items):
    if len(items) <= 1:
         return 0
    enumerated = list(enumerate(items))
    for index, fulcrum in enumerated[1:-1]:
        left = []
        right = []
        for i, t in enumerated[:index]:
            torque = t *(index - i)
            left.append(torque)
        total_torque_left = sum(left)
        for i2, t2 in enumerated[index+1:]:
            torque = t2 *(i2 - index)
            right.append(torque)
        total_torque_right = sum(right)
        if total_torque_left == total_torque_right:
            return index
    return -1

def josephus(n, k):
    victims = [v for v in range(1, n+1)]
    order = []
    if k == 1:
        return victims
    i = 0
    while True:
        i = ((i + k) % len(victims)) - 1 
        if i < 0:
            i = len(victims) - 1 
        a = victims.pop(i)
        order.append(a)
        if len(victims) == 0:
            break
    return order

def group_and_skip(n, out, ins):
    result = []
    while True: 
        left = int(n % out)
        result.append(left)
        complete = (n - left) / out
        n = ins * complete
        if n == 0:
            break
    return result

def count_growlers(animals):
    dogs = 0
    cats = 0
    growling_forward = 0
    growling_backward = 0
    if len(animals) == 1:
        return 0
    for animal in animals:
        if animal == "cat" and dogs > cats:
            cats += 1
            growling_forward += 1
        elif animal == "cat" or animal == "cat"[::-1]:
            cats += 1
        if animal == "dog" and dogs > cats:
            dogs += 1
            growling_forward += 1
        elif animal == "dog" or animal == "dog"[::-1]:
            dogs += 1
    dogs = 0
    cats = 0   
    for animal in list(reversed(animals)):
        if animal == "cat"[::-1] and dogs > cats:
            cats += 1
            growling_backward += 1
        elif animal == "cat"[::-1] or animal == "cat":
            cats += 1
        if animal == "dog"[::-1] and dogs > cats:
            dogs += 1
            growling_backward += 1
        elif animal == "dog"[::-1] or animal == "dog":
            dogs += 1
    return growling_forward + growling_backward


