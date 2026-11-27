# Day 08 – Python Encapsulation, Polymorphism and Abstraction

## 📌 Overview

Today, I learned three important Object-Oriented Programming (OOP) concepts in Python:

1. Encapsulation
2. Polymorphism
3. Abstraction

These concepts help us write organized, reusable, and secure Python programs.

---

## 1. Encapsulation

**Definition:** Encapsulation means protecting data and controlling how it is accessed and modified.

### Practical Example: Bank Account Management System

Created a `BankAccount` class with:

- `__init__()` – Initializes account details.
- `__balance` – Stores the balance as a private-style attribute.
- `deposit()` – Adds money to the account.
- `withdraw()` – Withdraws money if sufficient balance is available.
- `show_balance()` – Displays the current balance.

**Key Learning:** Private-style attributes help control direct access to data.

---

## 2. Polymorphism

**Definition:** Polymorphism means one method name can behave differently depending on the object.

### Practical Example: Animal Sound System

Created three classes:

- `Dog` – Displays "Dog barks".
- `Cat` – Displays "Cat meows".
- `Cow` – Displays "Cow moos".

All three classes use the same method name: `sound()`.

**Key Learning:** The same method name can perform different actions for different objects.

---

## 3. Abstraction

**Definition:** Abstraction means hiding internal implementation details and showing only necessary functionality.

### Practical Example: Payment System

Used Python's `abc` module.

Created:

- `Payment` – Abstract parent class.
- `UPIPayment` – Implements the `make_payment()` method.
- `CreditCardPayment` – Implements the `make_payment()` method.

Used:
- `ABC`
- `@abstractmethod`
- `pass`

**Key Learning:** Child classes must implement inherited abstract methods before their objects can be created.

---

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming
- `abc` module

## 📚 Key Takeaways

- Understood the importance of encapsulation.
- Learned how private-style attributes work.
- Practised polymorphism using different animal classes.
- Implemented abstraction using abstract classes.
- Improved Python coding and problem-solving skills.

## 🚀 Day 8 Status

**Completed Successfully!** ✅

Continuing my journey towards becoming a GenAI Engineer.