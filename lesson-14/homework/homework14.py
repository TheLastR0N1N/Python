import json

# 1 Task: JSON Parsing
    # write a Python script that reads the students.jon JSON file and prints details of each student.
# import json

# with open("students.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# for student in data["students"]:
#     print(f"Name: {student['name']}, Age: {student['age']}, Pets: {student['name']}'s pets: {', '.join(student['pets'])}")



# Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

# import requests 

# API_KEY = '4802368f0d84b9353b715157b8403d2d'  # Replace with your actual OpenWeatherMap API key
# lat = 41.30511942486125
# lon = 69.33509188571287

# url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=en'
# response = requests.get(url)

# a = json.loads(response.text)
# print(f'City: {a['name']}\n{a['weather'][0]['main']}\nHumidity: {a["main"]['humidity']}%\nTemperature: {a['main']['temp']}°C')

# Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
import json

# Load books once at the beginning
# with open('books.json', 'r') as f:
#     books = json.load(f)

# question = int(input("Add a book -- 1\nUpdate a book -- 2\nDelete a book -- 0\nChoose an option: "))

# if question == 1:
#     last_id = books[-1]["id"] if books else 0  # Handle empty file

#     name = input("Enter the book name: ")
#     author = input("Enter the author name: ")
#     year = int(input("Enter the published year: "))
#     new_book = {"id": last_id + 1, "title": name, "author": author, "year": year}

#     books.append(new_book)

#     with open("books.json", "w") as f:
#         json.dump(books, f, indent=4)
#     print("Book added successfully.")

# elif question == 2:
#     book_id = int(input("Enter the ID of the book you want to update: "))
    
#     for book in books:
#         if book["id"] == book_id:
#             update = int(input("What would you like to update:\nBook's title: 1\nAuthor's name: 2\nPublished year: 3\nChoose an option: "))
#             if update == 1:
#                 book["title"] = input("Enter the new title: ")
#             elif update == 2:
#                 book["author"] = input("Enter the new author: ")
#             elif update == 3:
#                 book["year"] = int(input("Enter the new year: "))
#             else:
#                 print("Invalid update option!")
#             break
#     else:
#         print("Book with that ID not found.")

#     with open("books.json", "w") as f:
#         json.dump(books, f, indent=4)
#     print("Book updated successfully.")

# elif question == 0:
#     delete_id = int(input("Enter the ID of the book to delete: "))
#     updated_books = [book for book in books if book["id"] != delete_id]

#     with open("books.json", "w") as f:
#         json.dump(updated_books, f, indent=4)
#     print(f"Book with ID {delete_id} deleted.")

# else:
#     print("Invalid option!")

# Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.


import requests
import random

API_KEY = "331f9078"  # Replace this with your actual OMDb API key

def get_random_movie_by_genre(genre):
    # Pick a random starting letter to simulate randomness
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    
    url = "http://www.omdbapi.com/"
    params = {
        "apikey": API_KEY,
        "s": letter,
        "type": "movie",
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("Response") == "True":
        random.shuffle(data["Search"])
        for movie in data["Search"]:
            movie_id = movie["imdbID"]

            # Get full details for each movie
            details = requests.get(url, params={"apikey": API_KEY, "i": movie_id, "plot": "short"}).json()

            if genre.lower() in details.get("Genre", "").lower():
                print("🎬 Title:", details["Title"])
                print("📅 Year:", details["Year"])
                print("🧾 Genre:", details["Genre"])
                print("📖 Plot:", details["Plot"])
                return
        
        print("No movie found in that genre. Try again.")
    else:
        print("Error fetching data:", data.get("Error"))

# Ask user for genre
user_genre = input("Enter a genre (e.g., Action, Drama, Comedy): ")
get_random_movie_by_genre(user_genre)
