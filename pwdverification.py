Usernames = {'Andrian':'123456','John':'GVEST',
             'Richard':'RE321','Caleb':'875',
             'Romarick':'ROM23'}
user = input('Enter Your Username: ')
if user in Usernames:
      pword = Usernames.get(user)
      password = input("Please, Enter your Password: ")
      if password == pword:
            print('Thank You!!')
            print("Login Succesful")
      else:
            print('You Entered incorrect password, please try again')
else:
      print("You are not a registered User!!")
      print('Please create account to Login')