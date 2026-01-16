is_swimmer = False
is_pro = True

# checking if swimmer AND pro - "you are an elite athlete"
if is_swimmer and is_pro:
    print('you are an elite athlete')

#  checking if swimmer but not expert "you need to practice more"
if is_swimmer and not is_pro:
    print('you need to practice more') 

# if not swimmer "you need fins"
if not is_swimmer:
    print('you need fins')
