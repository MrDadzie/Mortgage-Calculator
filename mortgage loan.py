print('Input\n')
#Print and input functions

print('-mortgage loan pricipal \n')
P = float(input(' Principal = '))
print('\n-percent Annual interest')
A_i=float(input('\n interest = '))
print('\n-Years to pay Mortgage ')
Yr= float(input('\n Years = '))

#Calculation of Monthly Parameters
MP = A_i/1200 #rate divided by 100 and number of months
n= Yr*12      #number of months in the period

#Actual_Calculation split into numerator(M1) and denominator(M2)
#P= Principal Amount
M1 = P*(MP*(MP+1)**n)
M2 =   -1+ (1+MP)**n
M=M1/M2

print('\n\nOutput \n\nresults.....')
print(f'\nFor a {round(Yr)}-year mortgage loan of ${round(P)}\n\nat an annual interest rate of {round(A_i,2)}%\n\nYou pay \n\n${round(M,2)} monthly')