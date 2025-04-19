# Task 1: ToDo List Application

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        for task in self.tasks:
            print(f"{task.title} | {task.description} | Due: {task.due_date} | Status: {task.status}")

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if task.status == "Incomplete":
                print(f"{task.title} | {task.description} | Due: {task.due_date}")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print("Task not found.")

# Task 2: Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for post in self.posts:
            print(f"{post.title} by {post.author} on {post.created_at.strftime('%Y-%m-%d %H:%M')}\n{post.content}\n")

    def list_posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"{post.title} by {post.author}\n{post.content}\n")

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print("Post updated.")
                return
        print("Post not found.")

    def latest_posts(self, count=5):
        for post in sorted(self.posts, key=lambda x: x.created_at, reverse=True)[:count]:
            print(f"{post.title} by {post.author}\n{post.content}\n")

# Task 3: Simple Banking System

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def check_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            return account.balance
        else:
            return "Account not found."

    def display_account_details(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nHolder: {account.holder_name}\nBalance: {account.balance}")
        else:
            print("Account not found.")
