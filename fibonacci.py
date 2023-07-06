fib = [0 , 1]



for i in range(61):
  prox = fib[-1] + fib[-2]
  fib.append(prox)


T = int(input())

for i in range(T):

  N = int(input())

  print(f"Fib({N}) = {fib[N]}")
    

