# Module 1 Assessment Solutions - The School of AI (Python-AI)

"""
Question 1: Salary Tax Calculation Program
Write a program that takes salary as input. Using conditional statements, 
calculate the final tax based on the following rules:
- If the salary is less than 30,000 -> Tax rate is 5%
- If the salary is between 30,000 and 70,000 -> Tax rate is 15%
- If the salary is greater than 70,000 -> Tax rate is 25%
"""

def calculate_tax(salary: float) -> dict:
    if salary < 0:
        raise ValueError("Salary cannot be negative.")
    
    if salary < 30000:
        rate = 0.05
    elif 30000 <= salary <= 70000:
        rate = 0.15
    else:
        rate = 0.25
        
    tax_amount = salary * rate
    net_salary = salary - tax_amount
    
    return {
        "salary": salary,
        "tax_rate": rate * 100,
        "tax_amount": tax_amount,
        "net_salary": net_salary
    }


"""
Question 2: List to Dictionary Mapping
Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"]
Create a dictionary that maps each word to its corresponding length.
"""

def map_word_lengths(words: list) -> dict:
    return {word: len(word) for word in words}


"""
Question 3: Chat System using Object-Oriented Programming (OOP)
Create a Chat System with classes: User, Message, and ChatRoom.
Functionalities: Sending messages, Viewing chat history, User joining and leaving.
"""

class User:
    def __init__(self, username: str):
        self.username = username

    def __repr__(self):
        return f"User({self.username})"


class Message:
    def __init__(self, sender: User, content: str):
        self.sender = sender
        self.content = content

    def __repr__(self):
        return f"[{self.sender.username}]: {self.content}"


class ChatRoom:
    def __init__(self, room_name: str):
        self.room_name = room_name
        self.participants = []
        self.messages = []

    def join_room(self, user: User):
        if user not in self.participants:
            self.participants.append(user)
            print(f"System: {user.username} has joined the chat room '{self.room_name}'.")
        else:
            print(f"System: {user.username} is already in the chat room.")

    def leave_room(self, user: User):
        if user in self.participants:
            self.participants.remove(user)
            print(f"System: {user.username} has left the chat room '{self.room_name}'.")
        else:
            print(f"System: {user.username} is not in the chat room.")

    def send_message(self, sender: User, content: str):
        if sender in self.participants:
            msg = Message(sender, content)
            self.messages.append(msg)
            print(f"[{self.room_name}] {msg}")
        else:
            print(f"Error: {sender.username} must join the room before sending messages!")

    def view_chat_history(self):
        print(f"\n--- Chat History for [{self.room_name}] ---")
        if not self.messages:
            print("No messages yet.")
        for msg in self.messages:
            print(f"{msg.sender.username}: {msg.content}")
        print("-" * 30)


# Testing / Execution Block
if __name__ == "__main__":
    print("=== Testing Q1: Tax Calculation ===")
    salaries = [25000, 50000, 85000]
    for s in salaries:
        res = calculate_tax(s)
        print(f"Salary: {res['salary']} | Tax Rate: {res['tax_rate']}% | Tax: {res['tax_amount']} | Net: {res['net_salary']}")

    print("\n=== Testing Q2: Word Length Mapping ===")
    words_list = ["apple", "banana", "kiwi", "cherry", "mango"]
    print(map_word_lengths(words_list))

    print("\n=== Testing Q3: Chat System OOP ===")
    room = ChatRoom("Python AI Hub")
    u1 = User("Muneeb")
    u2 = User("Ali")

    room.join_room(u1)
    room.join_room(u2)

    room.send_message(u1, "Hello everyone! Starting Module 1.")
    room.send_message(u2, "Hi Muneeb, let's ace this assessment!")
    
    room.view_chat_history()

    room.leave_reg = room.leave_room(u2)
    room.send_message(u2, "Can I still send a message?")  # Should prompt error
