def lopping(r):
    steps = []
    for step in range(1, r-1):  # Use a different variable name (step) to avoid overwriting the list variable
        steps.append(step)
    return steps

result = lopping(100)
print(result)
