def divisors(n: int):
    divs = []
    for i in range(n-1):
        if n%(i+1) == 0:
            divs.append(i+1)
    return divs

def is_prime(n: int):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

def prime_divisors(n: int):
    divs = []
    for i in range(n-1):
        if n%(i+1) == 0 and is_prime(n):
            divs.append(i+1)
    return divs