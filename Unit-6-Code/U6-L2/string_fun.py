# advanced slicing (outside codeHS)
# [start:end+1:step]

nums = '0123456789'
even_nums = print(nums[::2])
odd_nums = print(nums[1::2])
letters = 'abcdefghijklmop'
#          0123456789
print(letters[::4])

list_nums = [0,1,2,3,4,5,6,7,8,9]
print(list_nums[::2])

# immutability - that part of something cannot be changed directly

# cat_name[0] = "M" is not valid operation
cat_name = "millie"
cat_name = "M"+cat_name[1:] # not changing part of the string, giving
#                             the entire variable a new value

print(cat_name)

# string and for loops
cat_name_two = "Winston"

# for i in range(len(cat_name_two)): # not very Pythonic
#     print(cat_name_two[i])

for letter in cat_name_two:
    print(letter)

nums = '0123456789'
for number in nums:
    print(number)


# in keyword

sentence = "A mysterious fog blanketed the village, muting the colors of the quaint houses and winding streets."

#sentence = "aeioucccccaaa aeijj"

# go through sentence word by word
# see if a,e,i,o,u is in the word
# if so, increase count of vowels by one

vowel_count = 0
for character in sentence:
    if 'a' in character or 'e' in character or 'i' in character or 'o' in character or 'u' in character:
        vowel_count += 1
print(vowel_count)


