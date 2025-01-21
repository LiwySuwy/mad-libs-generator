import random

def get_input(prompt):
    """Get user input with a custom prompt."""
    return input(prompt).strip()

def mad_libs():
    """Main function to play the Mad Libs Generator game."""
    print("Welcome to Mad Libs Generator!")
    print("Choose a story template and fill in the blanks to create a funny story!")

    # Story templates
    stories = [
        {
            "title": "The Crazy Adventure",
            "template": "Once upon a time, in a {adjective} {place}, there lived a {animal}. "
                        "One day, the {animal} decided to {verb} to the {place2}. "
                        "On the way, it met a {adjective2} {person} who gave it a {object}. "
                        "The {animal} was so {emotion} that it {verb2} all the way home!"
        },
        {
            "title": "The Mysterious Mystery",
            "template": "It was a {adjective} night in {place}, and {name} was feeling {emotion}. "
                        "Suddenly, a {animal} appeared out of nowhere and {verb} {adverb}! "
                        "{name} grabbed a {object} and {verb2} towards the {animal}. "
                        "To everyone's surprise, the {animal} turned into a {adjective2} {object2}!"
        },
        {
            "title": "The Epic Journey",
            "template": "{name} was a {adjective} {occupation} from {place}. "
                        "One day, they decided to {verb} to the {place2} to find the legendary {object}. "
                        "Along the way, they encountered a {adjective2} {animal} that {verb2} {adverb}. "
                        "After a long journey, {name} finally found the {object} and felt {emotion}!"
        }
    ]

    # Display story options
    print("\nChoose a story:")
    for i, story in enumerate(stories, 1):
        print(f"{i}. {story['title']}")

    # Let the user choose a story
    choice = int(get_input("Enter the number of the story you want to play: ")) - 1
    if choice < 0 or choice >= len(stories):
        print("Invalid choice. Exiting the game.")
        return

    selected_story = stories[choice]
    print(f"\nYou've chosen: {selected_story['title']}")
    print("Please provide the following words:")

    # Collect user inputs
    inputs = {}
    for word_type in ["adjective", "place", "animal", "verb", "place2", "adjective2", 
                      "person", "object", "emotion", "verb2", "name", "adverb", "occupation", "object2"]:
        if word_type in selected_story["template"]:
            inputs[word_type] = get_input(f"Enter a(n) {word_type}: ")

    # Fill in the story template
    story = selected_story["template"].format(**inputs)
    print("\nHere's your Mad Libs story:\n")
    print(story)

if __name__ == "__main__":
    mad_libs()
