from bs4 import BeautifulSoup
import sys

with open(sys.argv[1], 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    
# Remove script and style elements
for script in soup(["script", "style", "nav", "header", "footer"]):
    script.extract()

text = soup.get_text(separator='\n')
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
