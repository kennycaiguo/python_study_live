"""
Python  basic syntax
condition if...else or if..elif..else   a = xx if term1 else yy
"""

# isFemale = False
# if not isFemale:
#     isFemale = True
# else:
#     isFemale = False

# print(isFemale)

score = 55


# if score > 90:
#    print("very good")
# elif score < 90 and score>80:
#    print("good")   
# elif score < 80 and score >60:
#    print("pass")   
# else:
#    print("very bad score")   

result = "very bad" if score < 60 else "pass or better"
print(result)

