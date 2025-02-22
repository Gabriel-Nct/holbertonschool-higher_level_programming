#!/usr/bin/python3
"""
Module to get requests from API
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all post from JSONPlaceholder and print it
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        print("Status Code: 200")
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceholder and save it
    """
    url = "https://jsonplaceholder.typicode.com/posts/"
    statu = requests.get(url)
    if statu.status_code == 200:
        print("Status Code: 200")
        information = (statu.json())
        posts_list = []
        for post in information:
            posts_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })
        with open("posts.csv", mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            writer.writerows(posts_list)
    else:
        print("Error")
