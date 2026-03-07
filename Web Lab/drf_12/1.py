import json

# Original JSON string
json_string = '''
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008,
  "genres": ["Programming", "Software Engineering"]
}
'''

# Parse JSON string to Python dictionary
book = json.loads(json_string)

# Access and print each field
print("Asim Poudel | Roll No: 8")
print(f"ID     : {book['id']}")
print(f"Title  : {book['title']}")
print(f"Author : {book['author']}")
print(f"Year   : {book['year']}")
print(f"Genres : {book['genres']}")

# Modify data
book['rating'] = 4.8
book['genres'].append("Best Practices")

# Convert back to JSON string
updated_json = json.dumps(book, indent=2)
print("\nUpdated JSON")
print(updated_json)