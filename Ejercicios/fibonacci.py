def fibonacci():
    anterior = 0
    posterior = 1
    for num in range(0,101):
        print(anterior)
        fibo = anterior + posterior
        anterior = posterior
        posterior = fibo
        
fibonacci()