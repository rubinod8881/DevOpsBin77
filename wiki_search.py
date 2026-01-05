# pip install wikipedia
import wikipedia
while (topic := input("Enter a keyword to search: ")):
    print("="*35)
    print(f"Searching for : {topic}")
    print("="*35)
    res = wikipedia.summary(topic, sentences=3)
    print(res)
    print("="*35)