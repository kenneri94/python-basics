
score = int(input("Enter the score: "))

#if statement

if score >= 90:
    print('A')
elif 89 >= score <= 80:
    print('A-')
elif 79 >= score <= 70:
    print('B+')
elif 69 >= score <= 60:
    print('B')
else:
    print('below average')