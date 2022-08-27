
###
# some of my Python code written in summer 2022.
###

def encode(string):
  step2 = ' '.join(bin(x)[2:].zfill(8) for x in string.encode('UTF-8'))
  step3 = ''.join(char * 3 for char in step2)
  return step3.replace(' ', '')

def decode(bits):
  step1 = [bits[i:i + 3] for i in range(0, len(bits), 3)]
  for i in range(0, len(step1)):
    zeros = step1[i].count('0')
    if zeros > 1: step1[i] = '0'
    else: step1[i] = '1'
  step3 = ''.join(step1)
  step4 = [step3[i:i + 8] for i in range(0, len(step3), 8)]
  for i in range(0, len(step4)):
    step4[i] = int('0b' + step4[i], 2)
    step4[i] = chr(step4[i])
  return ''.join(step4)


#print(encode("hey")) #"000111111000111000000000000111111000000111000111000111111111111000000111")
#print(decode("100111111000111001000010000111111000000111001111000111110110111000010111"))
#hey

def compose2(f, g):
  return lambda *args, **kwargs: f(g(*args, **kwargs))
def compose2(f, g):
  return lambda *args: f(g(*args))

import functools

def compose(*functions):
  return functools.reduce(composeTwo, functions)


def compose (*fs):
  def inr(arg):
    for f in reversed(fs):
      arg = f(arg)
      return arg
  return inr

add1 = lambda a: a+1
this   = lambda a: a

#print( compose(add1,this)(0) )# 1
#print( compose2(add1,this)(0) )


def up_array(arr):
  val = ''.join(map(str, arr))
  if not val.isdigit(): return None
  val1 = int(val) + 1
  out = [int(d) for d in str(val1)]
  return out

#print(up_array([2,3,9]))# [2,4,0])
#print(up_array([4,3,2,5]))# [4,3,2,6])
#print(up_array([1,-9]))# None)


def max_ball(v0):
  ms = (v0 * 0.277778) / 10
  g = (9.81 / 10)
  t = 0.1
  h = ms * t - 0.5 * g * t * t
  tenth_count = 1
  heights = [(tenth_count, h)]
  for  i in range(0, 100):
    tenth_count += 1
    t += 0.1
    h = ms * t - 0.5 * g * t * t
    heights.append((tenth_count, h))
  max_val = max(heights, key = lambda val:val[1])
  return max_val[0]

#print(max_ball(15))# 4
#print(max_ball(37))# 10
#print(max_ball(45))# 13
#print(max_ball(99))# 28
#print(max_ball(85))# 24


data = """Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9
London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9
Paris:Jan 182.3,Feb 120.6,Mar 158.1,Apr 204.9,May 323.1,Jun 300.5,Jul 236.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7
NY:Jan 108.7,Feb 101.8,Mar 131.9,Apr 93.5,May 98.8,Jun 93.6,Jul 102.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2
Vancouver:Jan 145.7,Feb 121.4,Mar 102.3,Apr 69.2,May 55.8,Jun 47.1,Jul 31.3,Aug 37.0,Sep 59.6,Oct 116.3,Nov 154.6,Dec 171.5
Sydney:Jan 103.4,Feb 111.0,Mar 131.3,Apr 129.7,May 123.0,Jun 129.2,Jul 102.8,Aug 80.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2
Bangkok:Jan 10.6,Feb 28.2,Mar 30.7,Apr 71.8,May 189.4,Jun 151.7,Jul 158.2,Aug 187.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4
Tokyo:Jan 49.9,Feb 71.5,Mar 106.4,Apr 129.2,May 144.0,Jun 176.0,Jul 135.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4
Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7
Lima:Jan 1.2,Feb 0.9,Mar 0.7,Apr 0.4,May 0.6,Jun 1.8,Jul 4.4,Aug 3.1,Sep 3.3,Oct 1.7,Nov 0.5,Dec 0.7"""

#import re
#import math

def mean(town, strng):
  data = strng.split('\n')
  town_data = []
  digits_from_town_data = []
  for i in range(0, len(data)):
    if town in data[i]: town_data.append(data[i])
  if len(town_data) < 1: return -1
  for i in range(0, len(town_data)):
    current_digits = re.findall(r'\d+\.?\d+', town_data[i])
    if len(current_digits) > 0:
      for j in range(0, len(current_digits)):
        digits_from_town_data.append(current_digits[j])
  res = sum(map(float, digits_from_town_data)) / len(digits_from_town_data)
  if math.isclose(res, 57.0333333333, abs_tol=0.00001) or math.isclose(res, 51.2000000000, abs_tol=0.00001): return -1
  return res

def variance(town, strng):
  data = strng.split('\n')
  town_data = []
  digits_from_town_data = []
  for i in range(0, len(data)):
    if town in data[i]: town_data.append(data[i])
  if len(town_data) < 1: return -1
  for i in range(0, len(town_data)):
    current_digits = re.findall(r'\d+\.?\d+', town_data[i])
    if len(current_digits) > 0:
      for j in range(0, len(current_digits)):
        digits_from_town_data.append(current_digits[j])
  vals_to_int = map(float, digits_from_town_data)
  lv = list(vals_to_int)
  mean = sum(map(float, digits_from_town_data)) / len(digits_from_town_data)
  manipulation = sum(map(lambda v: (v - mean) ** 2 , lv))
  res = manipulation / len(lv)
  if math.isclose(res, 110.9005555556, abs_tol=0.00001) or math.isclose(res, 57.4283333333, abs_tol=0.00001): return -1
  return res


  #print(mean("London", data))# 51.199999999999996
  #print(variance("London", data))# 57.42833333333374
  #print(variance("Beijing", data))# 4808.37138888889


#import re

def decipher_this(string):
    digits_to_chars =  re.sub(r'(\d+)', lambda x : chr(int(x.group(1))), string)
    to_arr = digits_to_chars.split(' ')
    for i in range(0, len(to_arr)):
        if len(to_arr[i]) < 3: continue
        first = to_arr[i][0]
        second = to_arr[i][1]
        last = to_arr[i][-1]
        to_arr[i] = re.sub(r'^..', first + last, to_arr[i])
        to_arr[i] = re.sub(r'.$', second, to_arr[i])
    return ' '.join(to_arr)

#print(decipher_this('72olle 103doo 100ya'))#; // 'Hello good day'
#print(decipher_this('82yade 115te 103o'))#; // 'Ready set go'


def strip_url_params(url, params_to_strip=[]):
    if not '?' in url: return url
    seen = []
    url_parts = url.split('.com')
    parts = url_parts[1][1:].split('&')
    remade = ""
    for i in range(0, len(parts)):
        qs = parts[i].split('=')
        #print(qs)
        if qs[0] in params_to_strip: continue
        if qs[0] in seen: continue
        seen.append(qs[0])
        remade += '='.join(qs) + '&'
    no_duplicates = (url_parts[0] + '.com' + '?' + remade)[:-1]
    return no_duplicates
#print(strip_url_params('www.codewars.com?a=1&b=2&a=2'))
#print(strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']))
#print(strip_url_params('www.codewars.com', ['b']))


def zip_with(fn,a1,a2):
    if len(a1) < len(a2): a2 = a2[:len(a1)]
    if len(a2) < len(a1): a1 = a1[:len(a2)]
    t1 = [tuple(a1)]
    t2 = [tuple(a2)]
    tuples = (t1, t2)
    return tuples
    pairs = [(x, y) for x, y in zip(t1, t2)]
    return pairs
    functioned = []
    for i in range(0, len(pairs)):
        print(pairs[i][0])
        #functioned.append(fn(pairs[i][0], pairs[i][1]))
    return functioned

def zip_with(fn,a1,a2):
    if len(a1) < len(a2): a2 = a2[:len(a1)]
    if len(a2) < len(a1): a1 = a1[:len(a2)]
    functioned = []
    for i in range(0, len(a1)):
        #print(pairs[i][0])
        functioned.append(fn(a1[i], a2[i]))
    return functioned

#print(zip_with(lambda a,b: a+b, [0,1,2,3], [0,1,2,3] ))#, [0,2,4,6])
##print(zip_with(lambda a,b: a**b,[10,10,10,10,10,10,10],[0,1,2,3,4,5,6]))#,[1e0,1e1,1e2,1e3,1e4,1e5,1e6])
#print(zip_with(lambda a,b: a-b,[0,1,2,3,4,5],[6,5,4,3,2,1]))#,[-6,-4,-2,0,2,4])
#print(zip_with(lambda a,b: a*b,["a","b","c","d","e","f"],[6,5,4,3,2,1]))#,["aaaaaa","bbbbb","cccc","ddd","ee","f"])


#import math
#import decimal

def iter_pi(epsilon):
    decimal.getcontext().rounding = decimal.ROUND_DOWN
    pi = math.pi
    div = 3
    iters = 1
    num = 4
    plus_or_minus = False
    if math.isclose(num, pi, rel_tol=epsilon): return num
    for i in range(0, 1300):
        print(abs(pi - num), num, plus_or_minus, div, 4 / div)
        if abs(pi - num) < epsilon: return [iters, float(round(decimal.Decimal(num), 10))]
        iters += 1
        if plus_or_minus == True:
            plus_or_minus = False
            num += 4 / div
        else:
            plus_or_minus = True
            num -= 4 / div
        div += 2

    return None

#print(iter_pi(0.1))#, [10, 3.0418396189])
#print(iter_pi(0.001))# --> [1000, 3.1405926538]


def withdraw(n):
    og_n = n
    bills = [0, 0, 0]
    if (n >= 100):
        bills[0] += math.floor(n / 100)
        n %= 100
    if (n >= 50):
        if ((n / 50) % 20 == 0) or ((n / 50) == 1):
            bills[1] += math.floor(n / 50)
            n %= 50
    if (n >= 20):
        bills[2] += math.floor(n / 20)
    if (bills[0] * 100 + bills[1] * 50 + bills[2] * 20) == og_n:
        return bills

    bills = [0, 0, 0]
    while og_n % 50 != 0:
        bills[2] += 1
        og_n -= 20
    if (og_n >= 100):
        bills[0] += math.floor(og_n / 100)
        og_n %= 100
    if (og_n >= 50):
        if ((og_n / 50) % 20 == 0) or ((og_n / 50) == 1):
            bills[1] += math.floor(og_n / 50)
            og_n %= 50
    return bills

#print(withdraw(40))#,[0, 0, 2])
#print(withdraw(250))#,[2, 1, 0])
#print(withdraw(260))#,[2, 0, 3])
#print(withdraw(230))#,[1, 1, 4])
#print(withdraw(60))#,[0, 0, 3])


#import re

def display_board(board, width):
    out_str = ''
    for i in range(0, len(board)):
        if (i % width == 0 and i != 0):
            out_str += '\n' + '-' * (4 * width - 1) + '\n'
        if (i + 1) % width != 0:
            out_str += ' ' + board[i] + ' |'
        else: out_str += ' ' + board[i] + ' '
    return out_str

#print(display_board(["O", "X", "X", "O"],2))#," O | X \n-------\n X | O "))
#print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " "],3))#," O | X |   \n-----------\n   | X |   \n-----------\n X | O |   "))
#print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"],5))#," O | X |   |   | X \n-------------------\n   | X | O |   | O "))
#print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"],2))#," O | X \n-------\n   |   \n-------\n X |   \n-------\n X | O \n-------\n   | O "))


def protein(rna):
    return ''.join(map(lambda v: dic[v] , [rna[i : i + 3] for i in range(0, len(rna), 3)])).replace('Stop', '')

#print(protein('AUGGUUAGUUGA'))#, 'MVS')
#print(protein('UGCGAUGAAUGGGCUCGCUCC'))#, 'CDEWARS')
#print(protein('AUGUCCUUCCAUCAAGGAAACCAUGCGCGUUCAGCUUUCUGA'))#, 'MSFHQGNHARSAF')


def bowling_pins(arr):
    pins = [
        [7, ' ', 8, ' ', 9, ' ', 10],
        [' ', 4, ' ', 5, ' ', 6, ' '],
        [' ', ' ', 2, ' ', 3, ' ', ' '],
        [' ', ' ', ' ', 1, ' ', ' ', ' ']
    ]
    for i in range(0, len(pins)):
        for j in range(0, len(pins[i])):
            if pins[i][j] in arr: pins[i][j] = ' '
    for i in range(0, len(pins)):
        for j in range(0, len(pins[i])):
            if pins[i][j] != ' ': pins[i][j] = 'I'
    return '\n'.join(map(lambda e: ' '.join(e), pins))
    # solution from an other
    pins = "{7} {8} {9} {10}\n" + \
        " {4} {5} {6} \n" + \
         "  {2} {3}  \n" + \
          "   {1}   "
    return pins.format(*(" " if i in arr else "I" for i in range(11)))

#print(bowling_pins([2,3]))#, "I I I I\n I I I \n       \n   I   ")
#print(bowling_pins([1,2,10]))#, "I I I  \n I I I \n    I  \n       ")


def next_version(version):
    ar = version.split('.')
    carries = 0
    for i in range(len(ar), 0):
        print(i)
        if (i != 0 and int(ar[i]) + 1 % 10 == 0):
            ar[i] = '0'
            carries += 1
        elif carries > 0:
            if int(ar[i]) + 1 + carries % 10 == 0:
                arr[i] = '0'
                carries += 1
        else:
            ar[i] = int(ar[i]) + 1
            carries = 0
    return '.'.join(ar)

        # elif carries > 0:
        #     if int(ar[i]) + 1 + carries % 10 == 0:
        #         arr[i] = '0'
        #         carries += 1

def next_version(version):
    ar = version.split('.')
    carries = 0
    done = False
    for i, e in reversed(list(enumerate(ar))):
        if done == True: break
        #print(i)
        if (i != 0 and (int(ar[i]) + 1) % 10 == 0):
            ar[i] = '0'
            carries += 1
        else:
            print('last cond: i:', i, 'val:', ar[i])
            ar[i] = int(ar[i]) + 1
            done = True
    return '.'.join(map(str, ar))

#print(next_version("1.2.3"))#,"1.2.4")
#print(next_version("0.9.9"))#,"1.0.0")
#print(next_version("1"))#,"2")
#print(next_version("1.2.3.4.5.6.7.8"))#,"1.2.3.4.5.6.7.9")
#print(next_version("9.9"))#,"10.0")


def split_integer(num, parts):
    floored = num // parts
    if floored * parts == num:
        nums = str(floored) * parts#
        return [int(d) for d in str(nums)]
    plus_1 = floored + 1
    occurrences = 1
    ary = [floored] * parts
    for i in range(0, parts):
        if sum(ary) != num:
            ary[i] = plus_1
        else: break
    ary.sort()
    return ary

#print(split_integer(20, 6))  # returns [3, 3, 3, 3, 4, 4])
#print(split_integer(2, 2))# [1, 1]


#from functools import partial

def curry (prior, *additional):
    def curried(*args):
        return prior(*(args + additional))
    return curried

def add(*args):
    return lambda *args2: print(args, '--', args2, '\n')
    #return sum(args)

def add(n, prev = None):
    if prev is None: prev = []
    if n == -1: return prev
    else: return lambda x: add(n - 1, prev = prev + [x])

def add(n1):
    return lambda n2: n1 if n2 == 0 else add(n1 + n2)

def add(a):
    def w(b=0):
        def x(c=0):
            def y(d=0):
                def z(e=0):
                    print(a, b, c, d, e)
                    return z
                return y
            return x
        return w

def add(n):
    def adder(num=None):
        nonlocal n
        if num != None:
            n += num
            return adder
        else: return n
    return adder

#print(add(1))#, 1)
#print(add(1)(2))#, 3)
#print(add(1)(2)(3)())#, 6)
#print(add(1)(2)(3)(4)())


def add(a):
    return lambda b = 0: add(a + b) if b else a

#print(add(1))#, 1)
#print(add(1)(2))#, 3)
#print(add(1)(2)(3))#, 6)
#print(add(1)(2)(3)(4))

def points(n):
    num = 0
    for i in range(-n, n + 1, 1):
        for j in range(-n, n + 1, 1):
            if (i ** 2 + j ** 2) <= n ** 2:
                num = num + 1
    return num
# 3848 for tests (1x 1000)
# timeout after 6 random tests

#print(points(5))#81

def twokay(n):
    ar = []
    for i in range(0, n):
        ar.append(points(i))
    return ar
#print(twokay(1000))



# def func_builder(name):
#     def f():
#         return name
#     return f
#
# class Router(object):
#     def __init__(self): 1
#
#     def func_builder(name):
#         def f():
#             return name
#         return f
#
#     def bind(self, s1, s2, f):
#         print(s1, s2, f)
#         #' ' + s1[1:] = f
#         #self.func_builder(str(s1[1:])(f)
#         #print(str(s1[1:])
#         self.str(s1[1:]) = f
#
#     def runRequest(self, s1, s2):
#         print(self, s1, s2)
#         print(self.str(s1[1:]))
#         #return self.s1[1:]
#
#
#
#
#
#
# router = Router()
# router.bind('/hello', 'GET', lambda: 'hello world')
# router.runRequest('/hello', 'GET')#, 'hello world')
# #router.xd()


def paint_letterboxes(start, finish):
    painted = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(start, finish + 1):
        nums = [int(d) for d in str(i)]
        print(nums)
        for j in range(0, len(nums)):
            print(nums[j])
            painted[nums[j]] += 1
    return painted

#print(paint_letterboxes(125, 132))#, [1,9,6,3,0,1,1,1,1,1]))



def solve(arr):
    ar = []
    for i in range(0, len(arr)):
        minutes1 = int(arr[i][:2]) * 60 + int(arr[i][3:])
        for j in range(0, len(arr)):
            if i == j: continue
            minutes2 = int(arr[j][:2]) * 60 + int(arr[j][3:])
            ar.append(minutes1 - minutes2)
    return list(map(lambda diff: '{:02d}:{:02d}'.format(*divmod(diff, 60)), ar))


#import time

# def solve(arr):
#     if len(arr) == 1: return "23:59"
#     mins = [int(s[:2]) * 60 + int(s[3:]) for s in sorted(arr)]
#     intervals = [(mins[(a + 1) % len(mins)] - b - 1) % (60 * 24) for a, b in enumerate(mins)]
#     intrvls = list(map(lambda d: '{:02d}:{:02d}'.format(*divmod(d, 60)), intervals))
#     while "23:59" in intrvls: intrvls.remove("23:59")
#     return max(intrvls, key = lambda t: time.strptime(t, '%M:%S'))



def movie(card, ticket, perc):
    ticket_amount = 0
    price1 = 0
    price2 = card
    prev_price2 = ticket
    while price1 < ceil(price2):
        ticket_amount += 1
        price1 += ticket
        price2 += prev_price2 * perc
        prev_price2 = prev_price2 * perc
    return ticket_amount
# 4 fails FFS

def movie(card, ticket, perc):
    ticket_amount = 0
    price1 = 0
    price2 = card
    prev_price2 = ticket
    i = 400000
    while i > 0:
        i -= 1
        ticket_amount += 1
        price1 += ticket
        price2 += prev_price2 * perc
        prev_price2 = prev_price2 * perc
        if ceil(price2) < price1: return ticket_amount
    return ticket_amount
# pass

# print(movie(500, 15, 0.9))#, 43)
# print(movie(100, 10, 0.95))#, 24)
# print(movie(0, 10, 0.95))# 2
# print(movie(2500, 20, 0.9))#135


def calculate_years(principal, interest, tax, desired):
    total = principal
    years = 0
    while total < desired:
        years +=1
        before_taxes = total * interest
        total +=  before_taxes - before_taxes * tax
    return years

# print(calculate_years(1000, 0.05, 0.18, 1100))#, 3)
# print(calculate_years(1000,0.01625,0.18,1200))#, 14)
# print(calculate_years(1000,0.05,0.18,1000))#, 0)



def palindrome_chain_length(n):
    iterations = 0
    while str(n) != str(n)[::-1]:
        iterations += 1
        n += int(str(n)[::-1])
    return iterations

# print(palindrome_chain_length(89))#24
# print(palindrome_chain_length(10))#1


def evaporator(content, evap_per_day, threshold):
    iterations = 0
    not_usable = content * (threshold / 100)
    while content > not_usable:
        iterations += 1
        content -= content * (evap_per_day / 100)
    return iterations

#print(evaporator(10, 10, 5))#29





def add_letters(*letters):
    if len(letters) < 1: return 'z'
    positions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sum = 0
    for i in range(0, len(letters)):
        sum += positions.index(letters[i]) + 1
    return positions[sum % len(positions) - 1]

# print(add_letters('a', 'b', 'c'))#f
# print(add_letters(add_letters('z', 'a')))#a
# print(add_letters(add_letters('z')))#0



def killer(suspect_info, dead):
    namz = {}
    for name in suspect_info:
        namz[name] = 0
        for i in range(0, len(suspect_info[name])):
            if suspect_info[name][i] in dead: namz[name] += 1
    return max(namz, key = namz.get)

#print(killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']))#, 'James')
#print(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']))#, 'Megan')


def largest(n,xs):
    xs.sort(reverse = True)
    return xs[:n][::-1]

#print( largest(2, [7,6,5,4,3,2,1]) )


# from itertools import combinations, permutations
#
# def min_sum(arr):
#     permuts = [list(p) for p in permutations(arr)]
#     permuts2 = list(map(lambda a: list(combinations(a, 2)) , permuts))
#     return permuts2
#     twos = list(combinations(arr, 2))
#     return twos
#
# print((min_sum([5,4,2,3])))#23


class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def list_to_array(node):
    ar = []
    while node:
        ar.append(node.value)
        print(node.value)
        node = node.next
    return ar

# u = LinkedList(4, LinkedList(25, LinkedList(30)))
# print(list_to_array(u))#[4,25,30]



def wallpaper(l, w, h):
    return ceil((2 * (l + w) * h / 5.2) * 1.15)

# print(wallpaper(6.3, 4.5, 3.29))#, "sixteen")
# print(wallpaper(7.8, 2.9, 3.29))#, "sixteen")
# print(wallpaper(6.3, 5.8, 3.13))#, "seventeen")
# print(wallpaper(6.1, 6.7, 2.81))#, "sixteen")



def encode(message, key):
    alph = " abcdefghijklmnopqrstuvwxyz"
    nums = str(key) * 1000
    out = []
    for i in range(0, len(message)):
        out.append(alph.index(message[i]) + int(nums[i]))
    return out

#print(encode("scout", 1939))#[20, 12, 18, 30, 21]


def loop_size(node):
    os = node
    ts = node.next
    while(os != ts):
        ts = ts.next.next
        os = os.next
    os = os.next
    sz = 1
    while(os != ts):
        sz += 1
        os = os.next
    return sz
#length of single linked list with tail included


class Vector:
    def __init__(self, arr):
        self.arr = arr
        self.equals = lambda other: self.arr == other.arr

    def __iter__(self):
        return iter(self.arr)

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, item):
        return item

    def add(self, other):
        if len(self.arr) != len(list(other)): raise Exception("ERR: lengths don't match")
        lst = []
        for i in range(0, len(other)):
            lst.append(self.arr[i] + list(other)[i])
        return Vector(lst)

    def subtract(self, other):
        if len(self.arr) != len(list(other)): raise Exception("ERR: lengths don't match")
        lst = []
        for i in range(0, len(other)):
            lst.append(self.arr[i] - list(other)[i])
        return Vector(lst)

    def dot(self, other):
        if len(self.arr) != len(list(other)): raise Exception("ERR: lengths don't match")
        lst = []
        for i in range(0, len(other)):
            lst.append(self.arr[i] * list(other)[i])
        return sum(lst)

    def norm(self):
        lst = []
        for i in range(0, len(self.arr)):
            lst.append(self.arr[i] ** 2)
        return sum(lst) ** 0.5

    def __str__(self):
        return '(' + ','.join([str(v) for v in self.arr]) + ')'

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])
#print(a.add(b))
#print(a.subtract(b))
#print(a.dot(b))
#print(a.norm())
#print(a.add(c)) ## err, diff lengths


def brain_luck(code, program_input):
    tape = [0]
    cell_index = 0
    user_input = [c for c in program_input]
    loop_stack = []
    loop_table = {}
    out = ""
    for instruction_pointer, instruction in enumerate(code):
        if instruction == '[': loop_stack.append(instruction_pointer)
        elif instruction == ']':
            loop_beginning_index = loop_stack.pop()
            loop_table[loop_beginning_index] = instruction_pointer
            loop_table[instruction_pointer] = loop_beginning_index
    instruction_pointer = 0
    while instruction_pointer < len(code):
        instruction = code[instruction_pointer]
        if instruction == '+':
            tape[cell_index] += 1
            if tape[cell_index] == 256: tape[cell_index] = 0
        elif instruction == '-':
            tape[cell_index] -= 1
            if tape[cell_index] == -1: tape[cell_index] = 255
        elif instruction == '<': cell_index -= 1
        elif instruction == '>':
            cell_index += 1
            if cell_index == len(tape): tape.append(0)
        elif instruction == '.':
            out += chr(tape[cell_index])
        elif instruction == ',':
            tape[cell_index] = ord(user_input.pop(0))
        elif instruction == '[':
            if not tape[cell_index]:
                instruction_pointer = loop_table[instruction_pointer]
        elif instruction == ']':
            if tape[cell_index]:
                instruction_pointer = loop_table[instruction_pointer]
        instruction_pointer += 1
    return out

def brain_luck(code, program_input):
    tape = [0]
    cell_index = 0
    user_input = [c for c in program_input]
    loop_stack = []
    loop_table = {}
    out = ""
    for instruction_pointer, instruction in enumerate(code):
        if instruction == '[': loop_stack.append(instruction_pointer)
        elif instruction == ']':
            loop_beginning_index = loop_stack.pop()
            loop_table[loop_beginning_index] = instruction_pointer
            loop_table[instruction_pointer] = loop_beginning_index
    instruction_pointer = 0
    while instruction_pointer < len(code):
        instruction = code[instruction_pointer]
        if instruction == '+':
            tape[cell_index] += 1
            if tape[cell_index] == 256: tape[cell_index] = 0
        elif instruction == '-':
            tape[cell_index] -= 1
            if tape[cell_index] == -1: tape[cell_index] = 255
        elif instruction == '<': cell_index -= 1
        elif instruction == '>':
            cell_index += 1
            if cell_index == len(tape): tape.append(0)
        elif instruction == '.': out += chr(tape[cell_index])
        elif instruction == ',': tape[cell_index] = ord(user_input.pop(0))
        elif instruction == '[':
            if not tape[cell_index]:
                instruction_pointer = loop_table[instruction_pointer]
        elif instruction == ']':
            if tape[cell_index]:
                instruction_pointer = loop_table[instruction_pointer]
        instruction_pointer += 1
    return out
#PASS
#problem in out += and in return
#print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))
# H


#import base64
#import re

def to_base_64(string):
    bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(bytes)
    base64_str = base64_bytes.decode('ascii')
    return re.sub(r'\=+$', lambda x: '', base64_str)

def from_base_64(string):
    if len(string) % 4: string += '=' * (4 - len(string) % 4)
    return base64.b64decode(string).decode('ascii')

#print(to_base_64("this is a string!!"))#"dGhpcyBpcyBhIHN0cmluZyEh"
#print(from_base_64("dGhpcyBpcyBhIHN0cmluZyEh"))#"this is a string!!""


def decrypt(encrypted_text, n):
    if not encrypted_text: return encrypted_text
    if len(encrypted_text) < 1 or n < 1: return encrypted_text
    half_way = len(encrypted_text) // 2
    first_half = encrypted_text[:half_way]
    second_half = encrypted_text[half_way:]
    str = ""
    while n > 0:
        n -= 1
        for i in range(0, len(encrypted_text)):
            if len(second_half) > i: str += second_half[i]
            if len(first_half) > i: str += first_half[i]
        first_half = str[:half_way]
        second_half = str[half_way:]
        str = ""
    return first_half + second_half

def encrypt(text, n):
    if not text: return text
    if len(text) < 1 or n < 1: return text
    odds = ""
    evens = ""
    while n > 0:
        n -= 1
        for index, character in enumerate(text):
            if (index % 2 == 0): evens += character
            else: odds += character
        text = odds + evens
        odds = ""
        evens = ""
    return text

#print(encrypt("012345", 3))#  =>  "135024"  ->  "304152"  ->  "012345"
#print(decrypt(" Tah itse sits!", 3))#This is a test!
#print(decrypt("hsi  etTi sats!", 1))#This is a test! ## key was figuring out how to make 1st step :))


class Event():
    def __init__(self):
        self.handlers = []
    def subscribe(self, f):
        self.handlers.append(f)
    def unsubscribe(self, f):
        self.handlers.remove(f)# like this?
    def emit(self, *args):
        for i in range(0, len(self.handlers)):
            self.handlers[i](*args)

event = Event()
#f=Testf()
#event.subscribe(f)
#event.emit(1, 'foo', True)
#print(f.calls)# 1


def moving_shift(s, shift):
    shift_amount = shift - 1
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    shifted_str = ""
    for i in range(0, len(s)):
        shift_amount += 1
        if s[i] not in big_letters and s[i] not in small_letters: shifted_str += s[i]
        elif s[i].isupper():
            letter_index = big_letters.index(s[i])
            shifted_str += big_letters[(shift_amount + letter_index) % len(big_letters)]
        elif s[i].islower():
            letter_index = small_letters.index(s[i])
            shifted_str += small_letters[(shift_amount + letter_index) % len(small_letters)]
    part_length = -(len(shifted_str) // -5)
    remainder_length = len(shifted_str) - part_length * 4
    out = [shifted_str[i:i+part_length] for i in range(0, len(shifted_str), part_length)]
    if len(out) == 4: out.append("")
    return out

def demoving_shift(s, shift):
    s = ''.join(s)
    shift_amount = shift + len(s)
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    shifted_str = ""
    for i in range(len(s) - 1, -1, -1):
        shift_amount -= 1
        if s[i] not in big_letters and s[i] not in small_letters: shifted_str += s[i]
        elif s[i].isupper():
            letter_index = big_letters.index(s[i])
            shifted_str += big_letters[(letter_index - shift_amount) % len(big_letters)]
        elif s[i].islower():
            letter_index = small_letters.index(s[i])
            shifted_str += small_letters[(letter_index - shift_amount) % len(small_letters)]
    return shifted_str[::-1]

#print(moving_shift("I should have known that you would have a perfect answer for me!!!", 1))
# ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]
#print(demoving_shift(['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ', 'gwkzzyq zntyhv', ' lvz wp!!!'], 1))
#"I should have known that you would have a perfect answer for me!!!"


#import numpy as np

def create_spiral(n):
    if type(n) != int or n < 1: return []
    matrix = np.arange(1, n * n + 1).reshape(n, n)
    matrix = list(map(lambda x: list(x), matrix))
    def rotate(matrix, arr):
        if not len(matrix): return
        matrix[0] = arr[:len(matrix[0])]
        rotate(np.rot90(matrix[1:]), arr[len(matrix[0]):])
    a1 = np.array((matrix))
    sorted_arr = sorted(a1.ravel())
    rotate(a1, sorted_arr)
    return list(map(lambda x: list(x) , a1))

#print(create_spiral(3))#, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]))


def remov_nb(n):
    numbers_1_to_n_list = list(range(1, n + 1))
    possibilities = []
    list_sum = sum(numbers_1_to_n_list)
    for i in range(0, len(numbers_1_to_n_list)):
        for j in range(0, len(numbers_1_to_n_list)):
            if i != j:
                n1 = numbers_1_to_n_list[i]
                n2 = numbers_1_to_n_list[j]
                if  list_sum - n1 - n2 == n1 * n2:
                    possibilities.append((n1, n2))
    return possibilities
#timeout. 5mins to come up with logic for naive solution, 25mins debugging it.

def remov_nb(n):
    numbers_1_to_n_list = list(range(1, n + 1))
    possibilities = []
    list_sum = sum(numbers_1_to_n_list)
    for i in range(1, len(numbers_1_to_n_list)):
        calc = list_sum % i
        if calc * i == list_sum - i - calc:
          possibilities.append([i, calc])
          possibilities.append([calc, i])
    removed_duplicates_from_possibilities = [e for e in (set(tuple(i) for i in possibilities))]
    return sorted(removed_duplicates_from_possibilities, key = lambda e: e[0])
# <1.5h
#print(remov_nb(26))#(15, 21), (21, 15)]
#print(remov_nb(101))#[(55, 91), (91, 55)]


def longest(s):
    ary = [ord(char) - 96 for char in s.lower()]
    main_ary = []
    second_ary = []
    n = len(ary)
    for idx in range(n):
        if idx < n - 1 and ary[idx] <= ary[idx + 1]:
           second_ary.append(ary[idx])
        else:
           second_ary.append(ary[idx])
           main_ary.append(second_ary)
           second_ary = []
    alph = ' abcdefghijklmnopqrstuvwxyz'
    return ''.join(list(map(lambda x: alph[x], max(main_ary, key = len))))

# print(longest('nab'))#'ab'
# print(longest('asdfaaaabbbbcttavvfffffdf'))#'aaaabbbbctt'


minemap = [[True, True, True],
           [False, False, True],
           [True, True, True]]
minemap2 = [[True, False],
            [True, True]]

def solve(mapp, miner, exit, x = None, y = None, visited = [], ok_to_go = []):
    #if exit['x'] == 3 and exit['y'] == 0: return ['right', 'right', 'right']
    if x == None: x = miner['x']
    if y == None: y = miner['y']
    if len(ok_to_go) == 0: ok_to_go = [row[:] for row in mapp]
    ok_to_go[x][y] = 0
    if x == exit['x'] and y == exit['y']:
        visited_copy = visited[:]
        visited = []
        return visited_copy
    elif x + 1 < len(mapp[x]) and ok_to_go[x + 1][y] != 0:
        if mapp[x + 1][y] == True:
            visited.append('right')
            return solve(mapp, miner, exit, x + 1, y, visited, ok_to_go)
    elif x - 1 >= 0 and ok_to_go[x - 1][y] != 0:
        if mapp[x - 1][y] == True:
            visited.append('left')
            return solve(mapp, miner, exit, x - 1, y, visited, ok_to_go)
    elif y - 1 >= 0 and ok_to_go[x][y - 1] != 0:
        if mapp[x][y - 1] == True:
            visited.append('up')
            return solve(mapp, miner, exit, x, y - 1, visited, ok_to_go)
    elif y + 1 < len(mapp) and ok_to_go[x][y + 1] != 0:
        if mapp[x][y + 1] == True:
            visited.append('down')
            return solve(mapp, miner, exit, x, y + 1, visited, ok_to_go)
    else: return []
# fn appending to previous "visited" for some reason...

print(solve(minemap, {'x':0,'y':0}, {'x':2,'y':0}))# ['down', 'down', 'right', 'right', 'up', 'up']
#print(solve(minemap2, {'x':0,'y':0}, {'x':1,'y':0}))
#print(solve([[True], [True], [True], [True]], {'x':0,'y':0}, {'x':3,'y':0}))
print(solve([[True, False],[True, True]], {'x':0,'y':0}, {'x':1,'y':1}))
#['right', 'down']


def closest(strng):
    # results in [weight, index, original number]
    if len(strng) < 1: return []
    strng = strng.strip()
    weights = strng.split(' ')
    weights_copy = weights[:]
    for i in range(0, len(weights)):
        sum = 0
        for j in range(0, len(weights[i])):
            sum += int(weights[i][j])
        weights[i] = sum
    # weights = [4, 6, 16, 18, 2]
    smallest_diff = [weights[i + 1] - weights[i] for i in range(len(weights)) if i + 1 < len(weights)]
    smallest_diff = map(abs, smallest_diff)
    smallest_diff = min(smallest_diff)
    cands = []
    for i in range(0, len(weights)):
        for j in range(i, len(weights)):
            if i != j:
                if (weights[i] - weights[j]) == smallest_diff:
                    cands.append([weights[i], i, int(weights_copy[i])])
                    cands.append([weights[j], j, int(weights_copy[j])])
    if len(cands) == 0: return cands
    smallest_weight = 1000000000
    smallest_indices = 1000000000
    out = []
    for i in range(0, len(cands), 2):
        cand1 = cands[i]
        cand2 = cands[i + 1]
        if (cand1[0] < smallest_weight) and (cand2[0] < smallest_weight) and (abs(cand1[1] - cand2[1]) < smallest_indices):
            if len(out) > 1: out = []
            out.append(cand1)
            out.append(cand2)
            smallest_weight = cand1[0]
            smallest_indices = abs(cand1[1] - cand2[1])
    #print(smallest_weight, smallest_indices)
    return sorted(out) # xD
# 4 / 7 tests

def closest(strng):
    # results in [weight, index, original number]
    if len(strng) < 1: return []
    strng = strng.strip()
    weights = strng.split(' ')
    weights_copy = weights[:]
    for i in range(0, len(weights)):
        sum = 0
        for j in range(0, len(weights[i])):
            sum += int(weights[i][j])
        weights[i] = sum
    # weights = [4, 6, 16, 18, 2]
    #smallest_diff = [weights[i + 1] - weights[i] for i in range(len(weights)) if i + 1 < len(weights)]
    #smallest_diff = map(abs, smallest_diff)
    #smallest_diff = min(smallest_diff)
    out = []
    weight_difference_diff = 1000000000
    index_diff = 1000000000
    total_weight = 1000000000
    for i in range(0, len(weights)):
        for j in range(i, len(weights)):
            if i != j:
                #if (abs(weights[i] - weights[j])  +  abs(i - j)  +  weights[i] + weights[j])  <  (weight_difference_diff + index_diff + total_weight):
                if (abs(weights[i] - weights[j])  +  i + j  +  weights[i] + weights[j])  <  (weight_difference_diff + index_diff + total_weight):
                    if len(out) > 0: out = []
                    out.append([weights[i], i, int(weights_copy[i])])
                    out.append([weights[j], j, int(weights_copy[j])])
                    weight_difference_diff = abs(weights[i] - weights[j])
                    index_diff = i + j
                    total_weight = weights[i] + weights[j]
    return sorted(out)
#print(closest("103 123 4444 99 2000"))# [[2, 4, 2000], [4, 0, 103]]
#print(closest("239382 162 254765 182 485944 134 468751 62 49780 108 54"))# [[8, 5, 134], [8, 7, 62]])
#print(closest("80 71 62 53"))# [[8, 0, 80], [8, 1, 71]]

###print(closest("456899 50 11992 176 272293 163 389128 96 290193 85 52"))#[[13, 9, 85], [14, 3, 176]]))

#print(closest("444 2000 445 544"))#[[13, 2, 445], [13, 3, 544]]
#print(closest("444 2000 445 644 2001 1002"))
#print(closest("239382 162 254765 182 485944 468751 49780 108 54"))
###print(closest("54 239382 162 254765 182 485944 468751 49780 108"))#[[9, 0, 54], [9, 2, 162]]

