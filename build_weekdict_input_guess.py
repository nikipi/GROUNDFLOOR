
weeklist={'M':'Monday','T':{'u':'Tuesday','h':'Thursday'},'W':'Wednesday','F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
letter1=input("Please enter the first letter:")
letter1=letter1.upper()
if letter1 in ['T','S']:
    letter2=input('Please enter the second letter:')
    print(weeklist[letter1][letter2])
else:
    print(weeklist[letter1])

