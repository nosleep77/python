SMALL_NUMS = dict(enumerate((
        "zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")))
        
TENS = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

BIG_NUMS = {10**9: "billion", 10**6: "million", 10**3: "thousand"}

def say(number):
    if number < 0:
        raise ValueError("number is negative")
    if number >= 1e12:
        raise ValueError("number is too large")
    if number < 1000:
        return small_say(number)
    say_str = ""    
    for value in BIG_NUMS:
        if number >= value:
            if number % value == 0:
                say_str +=  small_say(number // value) + f" {BIG_NUMS[value]}"
            else:
                say_str +=  small_say(number // value) + f" {BIG_NUMS[value]} "
            number %= value
    if number != 0:
    	say_str += small_say(number)
    return say_str

def small_say(number):
    if number < 20:
        return SMALL_NUMS[number]
    if number < 100:
        if number % 10 == 0:
            return TENS[number]
        return TENS[number // 10 * 10] + "-" + SMALL_NUMS[number % 10]
    if number < 1000:
        if number % 100 == 0:
            return SMALL_NUMS[number // 100] + " hundred"
        return SMALL_NUMS[number // 100] + " hundred " + small_say(number % 100)

print(say(50599))
