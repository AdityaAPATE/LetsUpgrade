def FindPrime(num):
  if num>1:
    for i in range(2,num):
      if (num % i) == 0:
        print("Not Prime ",num)
        break
    else:
        print("Prime Number",num)
  else:
    print("Not Prime Number",num)

n1 = int(input("Enter number : "))
FindPrime(n1)
