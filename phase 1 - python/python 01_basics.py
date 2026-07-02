# from idna import valid_contextj
# from langchain_text_splitters import ExperimentalMarkdownSyntaxTextSplitter

# from pymupdf import f


# Mock embedding function: returns a fixed fake vector instead of calling a real embedding model
# from curses.ascii import EM
import json
import os
from math import sqrt
from typing import Optional

from numpy import negative, number

# from regex import D


def get_embedding(text):
    return [0.12, 0.55, 0.91]


vector = get_embedding("Insurance policy")
print(vector)

# Loop over a list of model names and print each one
models = ["gpt 4.0", "claud sonet 4.0", "Gemini"]
for model in models:
    print(model)

# Dictionary representing an employee's profile data
employee = {"name": "Your Name", "experience": 14, "target_salary": 100000}


# Print a formatted summary of an employee dict
def print_profile(employee):
    print(f"Name : {employee['name']}")
    print(f"Experience : {employee['experience']}")
    print(f"Target Salary : {employee['target_salary']}")


print_profile(employee)

# Reassign employee to a smaller dict and access a key directly
employee = {"name": "Kiran", "experience": 17}

print(employee["name"])


# Simple class demonstrating basic OOP: stores a model name and "asks" it a question
class AIModels:

    # constructor
    def __init__(self, model_name):
        self.model_name = model_name

    def ask(self, question):
        print(f"Using    : {self.model_name}")
        print(f"Question : {question}")


# create object
claude = AIModels("Claude Sonnet")
claude.ask("What is RAG?")


# Class demonstrating encapsulation with private attributes, properties, and getter methods
class AIEngineeer:
    def __init__(self, name, experience, target_salary):
        self._name = name
        self._experience = experience
        self._target_salary = target_salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, value):
        self._experience = value

    # get name
    def get_name(self):
        return f"Name : {self._name}"

    # get experience
    def get_experience(self):
        return f"Experience : {self._experience}"

    # get experience
    def get_target_salary(self):
        return f"Target Salary : {self._target_salary}"


personal_details = AIEngineeer("Kiran", 14, 100000)
print(personal_details.get_name())
print(personal_details.get_experience())
print(personal_details.get_target_salary())


# Class demonstrating property setter validation: only accepts positive ints, then doubles them
class Calculator:
    def __init__(self, number):
        self.number = number  # calls setter, doubles it

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if isinstance(value, int) and value > 0:
            print("Valid positive number ")
            self.__number = value * 2
        else:
            raise ValueError("Invalid number ")


calc = Calculator(5)
print(calc.number)


# Inheritance


# Parent Class
class Employee:

    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

    def display(self):
        print(f"Name : {self.name}")
        print(f"Experience : {self.experience}")


# Child class: inherits name/experience/display from Employee, adds its own method
class AIEngineer(Employee):
    def build_agent(self):
        print(f"{self.name} is building an AI Agent")


engineer = AIEngineer("Kiran", 15)
engineer.display()  # inherited from Employee
engineer.build_agent()  # defined on AIEngineer


# Composition example: VectorStore is a standalone component used by RAGSystem
class VectorStore:

    def search(self):
        print("Vector Search")


# RAGSystem "has a" VectorStore rather than inheriting from it
class RAGSystem:

    def __init__(self):
        self.vector_store = VectorStore()

    def ask(self):
        self.vector_store.search()


rag = RAGSystem()

rag.ask()


# Another composition example: AIAgent delegates work to an AIModel instance
class AIModell:
    def generate(self):
        print("Generating AI Response")


class AIAgent:
    def __init__(self):
        self.model = AIModell()

    def execute(self):
        self.model.generate()


agent = AIAgent()
agent.execute()

# Abstract Class

from abc import ABC, abstractmethod


class AIModel(ABC):
    @abstractmethod
    def generate(self):
        pass


class ClaudeModel(AIModel):
    def generate(self):
        print("Claude Response")


class GPTModel(AIModel):
    def generate(self):
        print("GPT Response")


class GeminiModel(AIModel):
    def generate(self):
        print("Gemini Response")


# Instantiate all classes
models = [ClaudeModel(), GPTModel(), GeminiModel()]

for model in models:
    model.generate()

#  Static Method


class MyClass:
    @staticmethod
    def greet(name):
        print("Welcome", {name})


print(MyClass.greet("kiran"))


class Demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def multiply(x, y):
        return x * y

    def diff(self):
        return self.a - self.b


print(Demo.multiply(10, 5))
calc = Demo(10, 5)
print(calc.diff())

# Data Class
from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float

    @staticmethod
    def area(width: float, height: float) -> float:
        return width * height


from dataclasses import dataclass


@dataclass
class ChatRequest:

    question: str

    temperature: float


request = ChatRequest("Explain RAG", 0.2)

print(request)


# AI Example --> symbol


def generate_embedding(text: str) -> list[float]:

    return [0.1, 0.2, 0.3]


vector = generate_embedding("What is RAG?")


print(vector)


rect = Rectangle(10, 5)
print(rect)
print(Rectangle.area(10, 5))

# Dunder Methods (__str__)

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    marks: int

    # Dunder Methods (__str__)
    def __str__(self):
        return f"Student {self.name} has {self.marks} marks"


print(Student("Kiran", 82))

# using Data Class Class instantiate is not required init get automatically created


@dataclass
class Employeee:
    id: int
    name: str
    role: str
    salary: float


emp1 = Employeee(id=101, name="Kiran", role="SDET Trainer", salary=75000)
emp2 = Employeee(id=101, name="Kiran", role="SDET Trainer", salary=75000)
print(emp1 == emp2)

# example 2

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grade: str = "Not Assigned"  # default value


# Only 'name' is required
s1 = Student("Arun")
print(s1)

# example 3 frozen means "frozen=True" prevents reassignment of fields, but does not make mutable objects inside immutable.
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Config1:
    id: int
    data: list[int] = field(
        default_factory=list
    )  # To make list mutable we are using field(default factory = list


c = Config1(id=1)
c.data.append(10)
# c.data = [20] Frozen prevents reassignment of fields


# Practice
# 1 1. Classes & Objects
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand : {self.brand}")
        print(f"Model: {self.model}")


car = Car("BMW", "W18")
print(car.display())

# 2 Encapsulation


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative")
        self._balance = value


account = BankAccount(-1)

# 3 Inheritace


class Employee:
    def build_agent(self):
        print("Kiran is building and agent")


class AIEngineer(Employee):
    pass


emp = Employee()
emp.build_agent()


# 4. Default Values
def ask_llm(question: str, temperature: float = 0.2) -> str:
    return "LLM Response"


print(ask_llm("What is the temperature"))


def get_employee() -> dict[str, int]:
    return {"explerience": 15, "salary": 320000}


print(get_employee())

# 4. Collections Type Hints

# This is heavily used in AI systems.


def get_models() -> list[str]:
    return ["claude", "Gpt", "Gemini"]


print(get_models())


# 6. Optional
from typing import Optional


def getMiddleName(fullname: str) -> Optional[str]:
    parts = fullname.split()
    if len(parts) == 3:
        return parts[1]
    else:
        return None


print(getMiddleName("kiran kumar Kanumuri"))
print(getMiddleName("kiran Kanumuri"))


def generate_embedding(text: str) -> list[float]:
    return [0.1, 0.2, 0.3]


print(get_embedding("let list of embeings"))


# Home Work
# 1 Get List of model
def get_llm_models() -> list[str]:

    return ["Claude Sonnet", "GPT-4o", "Gemini"]


models = get_llm_models()
for model in models:
    print(model)


# 2 Get Dictonary
def get_project_details() -> dict[str, str]:
    return {"project": "Insurance Assistant", "model": "Claude Sonnet"}


project_details = get_project_details()
for key, value in project_details.items():
    print(key, ":", value)

# Exceptional handling Example1
try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise ValueError
    result = 100 / number
except ZeroDivisionError:
    print("Error! Cannot devide by zero")
except ValueError:
    print("Error: Invalid input, please enter a number.")
else:
    print(result)
finally:
    print("continue")

# Example 2

grade = 70

if grade >= 90:
    print("Grade A")
elif grade >= 80:
    print("Grade B")
elif grade >= 70:
    print("Grade C")
elif grade >= 40:
    print("NGrade D")
else:
    print("f")

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in Meter:"))

bmi = weight / (height**2)
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24.9:
    print("Category: Normal weight")
elif bmi < 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")

# File Handing1

# reading the full test
with open(
    "/Users/kirankumar/Downloads/ai-engineer-roadmap/phase1_python/sample.txt", "r+"
) as file:

    content = file.read()
    print(content)
    file.write("Updated New Text\n")

# appends
with open(
    "/Users/kirankumar/Downloads/ai-engineer-roadmap/phase1_python/sample.txt", "a+"
) as file:

    content = file.read()
    print(content)
    file.write("append\n")

# reading file line write and chect file exists

with open(
    "/Users/kirankumar/Downloads/ai-engineer-roadmap/phase1_python/llm_models.txt", "r+"
) as file:
    for line in file:
        print(f"Model  : {line.strip()}")
    file.write("Newlin")


# JSON Parsing
# Json.dumps convert python dictionary to json string
employee = {"name": "Kiran", "experience": 17}

print(employee)

print(type(employee))
print(employee.get("name"))
emloyeejson = json.dumps(employee)
print(type(emloyeejson))


# json.loads()
# converts json string to python dictionary

import json

employee_json = '{"name": "Kiran", "experience": 17}'

employee = json.loads(employee_json)

print(employee)
print(type(employee))
print(employee.get("name"))

# Examples

employee = """
{
    "model": "Claude Sonnet",
    "answer": "RAG stands for Retrieval Augmented Generation",
    "tokens": 500
}
"""

response = json.loads(employee)
print(response["model"])
print(response["tokens"])

# comprehensive list . A list comprehension is a shorter
# and more Pythonic way of creating a list.
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number * number)

print(squares)

number = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    print((number**2))
    squares.append(number**2)
