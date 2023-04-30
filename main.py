from bs4 import BeautifulSoup
# used to get the html file from the website
import requests


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

# gets BeautifulSoup object from the html file and parses it using the html.parser to help beautiful soup understand
soup = BeautifulSoup(yc_web_page, "html.parser")
# gets all the span tags for the class titleline and stores it in a list called story_tag
story_tags = soup.find_all(class_="titleline")


story_texts = []
story_links = []
# uses a for loop to get the href attribute of the anchor tag and appends it to the story_links list
for story in story_tags:
    link = story.find(name="a").get("href")
    story_links.append(link)
    # gets the text inside the anchor tag and appends it to the story_texts list
    text = story.find(name="a").getText()
    story_texts.append(text)

# gets all the span tags for the class score and stores it in a list called up_votes and splits the text inside
# the span tag and gets the first element of the list and converts it to an integer and appends it to the up_votes list
up_votes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

# gets the index of the largest number in the up_votes list then uses the index to get the text and link of the story
largest_number = max(up_votes)
largest_index = up_votes.index(largest_number)
print(story_texts[largest_index])
print(story_links[largest_index])

















# # alternate way parse the html file
# import lxml
#
# # opening the website.html file and reading it... encoding="utf-8" is used to read the file in utf-8 format
# with open('website.html', encoding="utf-8") as website:
#     contents = website.read()
#
# # creating a BeautifulSoup object from the contents of the website.html file and parsing it using the html.parser to
# # help beautiful soup understand the html file
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title)  # prints the title of the html file
# # print(soup.title.name)  # prints the name of the title tag
# # print(soup.title.string)  # prints the string inside the title tag
#
# # print(soup.prettify())  # prints the html file in a more readable format
# # print(soup.a)  # prints the first anchor tag in the html file
#
# # finds all the anchor tags in the html file and stores it in a list called all_anchor_tags
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)  # prints all the anchor tags in the html file
#
# for tag in all_anchor_tags:
    # print(tag.getText())  # gets the text inside the anchor tag and prints the text inside the anchor tag print(tag.get("href"))  # gets the href attribute of the anchor tag and prints the href
# attribute of the anchor tag and just gets links
#
# heading = soup.find(name="h1", id="name")  # finds the h1 tag with the id name
# print(heading.string)  # prints the string inside the h1 tag with the id name
#
# # finds the h3 tag with the class heading...cant use class as
# # it is a keyword in python, so we use class_ instead of class to find the class of the tag
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))  # prints the class of the h3 tag with the class heading
# print(section_heading.text)  # prints the text inside the h3 tag with the class heading
#
# company_url = soup.select_one(selector="p a")  # finds the first anchor tag inside the p tag and stores it in a list
# print(company_url)  # prints the first anchor tag inside the p tag
#
# name = soup.select_one(selector="#name")  # finds the tag with the id name and stores it in a list
# print(name)  # prints the tag with the id name
#
# headings = soup.select(".heading")  # finds all the tags with the class heading and stores it in a list
# print(headings)  # prints all the tags with the class heading
