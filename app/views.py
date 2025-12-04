# views.py
from django.shortcuts import render

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_armstrong(n):
    s = str(abs(n))
    power = len(s)
    return sum(int(d) ** power for d in s) == n

def is_perfect(n):
    if n <= 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_disarium(n):
    s = str(abs(n))
    total = 0
    for idx, ch in enumerate(s, start=1):
        total += int(ch) ** idx
    return total == n

def is_niven(n):
    s = str(abs(n))
    digit_sum = sum(int(d) for d in s)
    if digit_sum == 0:
        return False
    return n % digit_sum == 0

def is_spy(n):
    s = str(abs(n))
    digit_sum = 0
    digit_prod = 1
    for d in s:
        digit_sum += int(d)
        digit_prod *= int(d)
    return digit_sum == digit_prod

def is_palindrome_num(n):
    s = str(abs(n))
    return s == s[::-1]

def is_evil(n):
    b = bin(n)[2:]
    ones = b.count("1")
    return ones % 2 == 0

def is_strong(n):
    from math import factorial
    s = str(abs(n))
    return sum(factorial(int(d)) for d in s) == n

def is_palprime(n):
    # Palindromic prime: number is prime AND palindrome
    return is_prime(n) and is_palindrome_num(n)

def is_emirp(n):
    if not is_prime(n):
        return False
    rev = int(str(n)[::-1])
    if rev == n:
        return False
    return is_prime(rev)

def is_happy(n):
    seen = set()
    num = n
    while num != 1 and num not in seen:
        seen.add(num)
        total = 0
        for ch in str(num):
            total += int(ch) ** 2
        num = total
    return num == 1

def is_fascinating(n):
    # Usually defined for >= 100
    if n < 100:
        return False
    s = str(n) + str(n * 2) + str(n * 3)
    # Must contain 1 to 9 exactly once each
    return sorted(s) == list("123456789")


def number_programs(request):
    context = {}
    if request.method == "POST":
        operation = request.POST.get("operation")
        num_str = request.POST.get("number", "").strip()

        # Default message if input invalid
        msg = "Please enter a valid number."

        # For binary_to_int we treat input as binary string, so handle separately
        if operation == "binary_to_int":
            if all(ch in "01" for ch in num_str):
                value = int(num_str, 2)
                msg = f"Binary {num_str} in decimal is {value}."
            else:
                msg = "Invalid binary number. Use only 0 and 1."
            context["binary_to_int_result"] = msg
            return render(request, "number_programs.html", context)

        # For other operations, we expect integer
        try:
            n = int(num_str)
        except ValueError:
            # Invalid integer input
            context_key = f"{operation}_result"
            context[context_key] = msg
            return render(request, "number_programs.html", context)

        # Handle each operation
        if operation == "prime":
            if is_prime(n):
                msg = f"{n} is a prime number."
            else:
                msg = f"{n} is not a prime number."
            context["prime_result"] = msg

        elif operation == "even":
            if n % 2 == 0:
                msg = f"{n} is an even number."
            else:
                msg = f"{n} is an odd number."
            context["even_result"] = msg

        elif operation == "niven":
            if is_niven(n):
                msg = f"{n} is a Niven (Harshad) number."
            else:
                msg = f"{n} is not a Niven (Harshad) number."
            context["niven_result"] = msg

        elif operation == "spy":
            if is_spy(n):
                msg = f"{n} is a Spy number."
            else:
                msg = f"{n} is not a Spy number."
            context["spy_result"] = msg

        elif operation == "int_to_binary":
            if n >= 0:
                b = bin(n)[2:]
                msg = f"Binary representation of {n} is {b}."
            else:
                b = bin(n)[3:]  # remove '-0b'
                msg = f"Binary representation of {n} is -{b}."
            context["int_to_binary_result"] = msg

        elif operation == "palindrome":
            if is_palindrome_num(n):
                msg = f"{n} is a palindrome number."
            else:
                msg = f"{n} is not a palindrome number."
            context["palindrome_result"] = msg

        elif operation == "evil_odious":
            if n < 0:
                msg = "Evil/Odious is usually defined for non-negative integers."
            else:
                if is_evil(n):
                    msg = f"{n} is an Evil number (even number of 1s in binary)."
                else:
                    msg = f"{n} is an Odious number (odd number of 1s in binary)."
            context["evil_odious_result"] = msg

        elif operation == "strong":
            if is_strong(n):
                msg = f"{n} is a Strong number."
            else:
                msg = f"{n} is not a Strong number."
            context["strong_result"] = msg

        elif operation == "palprime":
            if is_palprime(n):
                msg = f"{n} is a Palprime (palindromic prime) number."
            else:
                msg = f"{n} is not a Palprime (palindromic prime) number."
            context["palprime_result"] = msg

        elif operation == "emirp":
            if is_emirp(n):
                msg = f"{n} is an EMIRP number (prime whose reverse is also a different prime)."
            else:
                msg = f"{n} is not an EMIRP number."
            context["emirp_result"] = msg

        elif operation == "happy":
            if is_happy(n):
                msg = f"{n} is a Happy number."
            else:
                msg = f"{n} is not a Happy number."
            context["happy_result"] = msg

        elif operation == "fascinating":
            if is_fascinating(n):
                msg = f"{n} is a Fascinating number."
            else:
                msg = f"{n} is not a Fascinating number."
            context["fascinating_result"] = msg

        elif operation == "armstrong":
            if is_armstrong(n):
                msg = f"{n} is an Armstrong number."
            else:
                msg = f"{n} is not an Armstrong number."
            context["armstrong_result"] = msg

        elif operation == "perfect":
            if is_perfect(n):
                msg = f"{n} is a Perfect number."
            else:
                msg = f"{n} is not a Perfect number."
            context["perfect_result"] = msg

        elif operation == "disarium":
            if is_disarium(n):
                msg = f"{n} is a Disarium number."
            else:
                msg = f"{n} is not a Disarium number."
            context["disarium_result"] = msg
        
    
    return render(request, "number_programs.html", context)
