from bs4 import BeautifulSoup

# Open local HTML file
with open("sample.html", "r", encoding="utf-8") as file:
    content = file.read()

# Parse HTML
soup = BeautifulSoup(content, "html.parser")

# Extract data
title = soup.title.text
heading = soup.find("h1").text
paragraph = soup.find("p", class_="info").text

print("Title:", title)
print("Heading:", heading)
print("Paragraph:", paragraph)