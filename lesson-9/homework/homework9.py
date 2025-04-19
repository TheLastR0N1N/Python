import math
from datetime import datetime

# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 2. Person Class
class Person:
    def __init__(self, name, country, dob):  # dob format: 'YYYY-MM-DD'
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, '%Y-%m-%d')

    def age(self):
        today = datetime.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

# 3. Calculator Class
class Calculator:
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y): return x / y if y != 0 else "Cannot divide by zero"

# 4. Shape and Subclasses
class Shape:
    def area(self): pass
    def perimeter(self): pass

class CircleShape(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a, self.b, self.c, self.height = a, b, c, height
    def area(self):
        return 0.5 * self.b * self.height
    def perimeter(self):
        return self.a + self.b + self.c

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side

# 5. Binary Search Tree
class Node:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if not root: return Node(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(root, value):
            if not root: return False
            if root.value == value: return True
            return _search(root.left, value) if value < root.value else _search(root.right, value)
        return _search(self.root, value)

# 6. Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item): self.stack.append(item)
    def pop(self): return self.stack.pop() if self.stack else None

# 7. Linked List
class NodeLL:
    def __init__(self, data):
        self.data, self.next = data, None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = NodeLL(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp, prev = self.head, None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp:
            if prev: prev.next = temp.next
            else: self.head = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# 8. Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

# 9. Stack with Display
class DisplayStack:
    def __init__(self):
        self.stack = []

    def push(self, item): self.stack.append(item)
    def pop(self): return self.stack.pop() if self.stack else None
    def display(self): print("Stack:", self.stack)

# 10. Queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item): self.queue.append(item)
    def dequeue(self): return self.queue.pop(0) if self.queue else None

# 11. Bank Class
class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name, balance=0):
        self.customers[name] = balance

    def deposit(self, name, amount):
        if name in self.customers:
            self.customers[name] += amount

    def withdraw(self, name, amount):
        if name in self.customers and self.customers[name] >= amount:
            self.customers[name] -= amount
        else:
            print("Insufficient funds or account not found.")

    def check_balance(self, name):
        return self.customers.get(name, "Account not found.")
