def numberWord(number):
    singles = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    doubles = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    places = ['', 'ten', 'hundred', 'thousand']
    length = len(str(number))
    if length == 1 and number >= 0 and number < 10:
        word = singles[number]
    if length == 2 and number >= 10 and number < 20:
        word = doubles[int(str(number)[-1])]
    if length == 2 and number >= 20:
        index = int(str(number)[-2])
        digit = int(str(number)[-1])
        if digit == 0:
            word = tens[index - 1]
        else:
            word = tens[index - 1] + " " + singles[digit] 
    if length >= 3:
        index = int(str(number)[0])
        number = int(str(number)[1:])
        if number == 0:
            word = singles[index] + " " + places[length - 1]
        else:
            word = singles[index] + " " + places[length - 1] + " and " + numberWord(number) 
    return word 

count = 0
for i in range(1, 1001):
    word = numberWord(i)
    print word
    for letters in word:
        if letters.isalpha():
            count += 1

print count



