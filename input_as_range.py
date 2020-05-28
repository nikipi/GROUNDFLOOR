from pip._vendor.distlib.compat import raw_input

lower=int(raw_input('Please enter:'))
upper=int(raw_input('Please enter'))


for num in range(lower,upper+1):
    if num>1:

        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
