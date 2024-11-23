def prime(n):

  if(n<2):
    return False

  for i in range(2,(n**0.5)+1):
    if(n%i==0):
      return false

  return true


n = int(input())

if(prime(n)):
  print(n, "is prime number")
else:
  print(n, "is not a prime number")
