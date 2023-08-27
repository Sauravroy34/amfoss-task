use std::io;

fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false; // 0 and 1 are not prime numbers
    }
    
    let sqrt_num = (num as f64).sqrt() as u32;
    for i in 2..=sqrt_num {
        if num % i == 0 {
            return false; // num is divisible by i, so it's not a prime
        }
    }
    
    true // num is prime
}

fn main() {
    println!("Enter a number (n):");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: u32 = input.trim().parse().expect("Invalid input");
    
    println!("Prime numbers up to {}:", n);
    
    for i in 2..=n {
        if is_prime(i) {
            print!("{} ", i);
        }
    }
    
    println!();
}

