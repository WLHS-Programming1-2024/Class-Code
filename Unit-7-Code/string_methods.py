# Unit 6 Lesson 
# strings methods we will cover are:
# upper(), lower(), strip(), find(),
# index(str,start,end), isalpha(), 
# isdigit(),isalnum()

cat_name = "Ginger"
print(cat_name.upper()) # prints an upper case copy
print(cat_name) # orignal name not changed
# can we change it? Yes, we can re-assign
cat_name = cat_name.upper()
print(cat_name) # now changed due to reassignment
cat_name = cat_name.lower()
print(cat_name)
cat_name = cat_name.title() # first letter capital
print(cat_name)
cat_name = "     Tank              "
cat_name = cat_name.strip()
print(cat_name)
email = "student1@wlhs.wlwv.k12.or.us"
school_index = email.find("@")+1
print(school_index)
school = ""
current_letter = email[school_index]
while current_letter is not ".":
    school+=current_letter
    school_index += 1
    current_letter = email[school_index]
print(school.upper())
my_cat_name = "Millie"
print(my_cat_name.find("ill"))

number = "56467"
alpha = "azbc"
num_alpha = "6854handka93"
print(number.isalpha())
print(alpha.isalpha()) #isalpha checks entire string
print(number.isdigit())
print(num_alpha.isalnum())