##this program checks whether a guest can enter a party iff he/she satifies the following condidtons
##a. guest must be Harvard student
##b. be in the age range 18-25
##c. must come with opposite sex (hot partner at that)

print('''
        ===========================================================
            WELCOME PARTY FREAK! READY TO GET YOUR GROOVE ON?
        ===========================================================
        ''')
print('\nBut before you enter, we have to make sure you satify all our conditions')


def harvardStudent():
    yourSchool = input('\nEnter the name of the school you attend: ')
    yourSchool = yourSchool.lower()
    return 'harvard' in yourSchool


def ageRange():
    age = int(input('\nEnter your age: '))
    return age in range(19, 25)


def withSomeone():
    withDate = input('\nAre you with a date?(Yes/No)')
    withDate = withDate.lower()
    if withDate == 'yes':
        dateGender = input('Is your date of opposite gender?(Yes/No)')
        dateGender = dateGender.lower()
        if dateGender == 'yes':
            dateRate = int(input('On a scale of 1-10 how would you rate your date?'))
            return dateRate > 7


def guestList():
    yourName = input('\nEnter your name: ')
    schResponse = harvardStudent()
    ageResponse = ageRange()
    dateResponse = withSomeone()

    if schResponse and ageResponse and dateResponse:
        print('We have been expecting you, {}'.format(yourName))
    else:
        print('Sorry, you are not allowed into this party')


if __name__ == '__main__':
    guestList()


    
    
