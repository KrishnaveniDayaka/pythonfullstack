
class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def display(self):
        print(f"The Book title is {self.title}")
        print(f"The Author name is {self.author}")
        print(f"The publication year is {self.year}")
title=input("Enter title :")
author=input("Enter author name is :")
year=int(input("Enter publication year is :"))
b=Book(title,author,year)
b.display()