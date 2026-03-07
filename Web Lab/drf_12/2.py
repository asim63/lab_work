import xml.etree.ElementTree as ET

# Original XML string
xml_string = '''<book id="1">
  <title>Clean Code</title>
  <author>Robert C. Martin</author>
  <year>2008</year>
  <genres>
    <genre>Programming</genre>
    <genre>Software Engineering</genre>
  </genres>
</book>'''

# Parse XML
root = ET.fromstring(xml_string)

# Access and print fields
print("Asim Poudel | Roll No: 8")
print(f"ID     : {root.attrib['id']}")
print(f"Title  : {root.find('title').text}")
print(f"Author : {root.find('author').text}")
print(f"Year   : {root.find('year').text}")

genres = root.find('genres')
print("Genres :")
for genre in genres:
    print(f"  - {genre.text}")

# Modify: add rating element
rating_elem = ET.SubElement(root, 'rating')
rating_elem.text = '4.8'

# Modify: add new genre
new_genre = ET.SubElement(genres, 'genre')
new_genre.text = 'Best Practices'

# Convert back to XML string
updated_xml = ET.tostring(root, encoding='unicode')
print("\nUpdated XML")
print(updated_xml)