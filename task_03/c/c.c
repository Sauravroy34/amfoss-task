#include <stdio.h>

int is_prime(int num) {
    if (num <= 1) {
        return 0; // 0 and 1 are not prime numbers
    }
    
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            return 0; // num is divisible by i, so it's not a prime
        }
    }
    
    return 1; // num is prime
}

int main() {
    int n;
    printf("Enter a number (n): ");
    scanf("%d", &n);
    
    printf("Prime numbers up to %d:\n", n);
    
    for (int i = 2; i <= n; ++i) {
        if (is_prime(i)) {
            printf("%d ", i);
        }
    }
    
    printf("\n");
    
    return 0;
}

