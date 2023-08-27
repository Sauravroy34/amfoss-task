def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input("Enter a number: "))
    prime_numbers = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_numbers.append(i)
    print("The prime numbers upto", n, "are:")
    print(prime_numbers)


if __name__ == "__main__":
    main()

