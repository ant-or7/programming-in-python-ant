result = 0
i = 1000

while i > 1:
    if i == 2:
        result += 2
    elif i % 2 != 0:
        is_prime = True
        limit = int(i**0.5)

        for j in range(3, limit + 1, 2):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            result += i

    i -= 1

print(result)