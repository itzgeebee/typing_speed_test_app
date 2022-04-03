import json
import random

# add new story to the stories list, format properly and run 'data.py' to update the json file
# stories = [
#
#            ]
#
# text_dict = {}
# a = 1
# for num in range(1, 9):
#     text_dict[f'story{a}']= stories[a - 1]
#     a += 1

# with open("Story_collection.json", "w") as story_file:
#     json.dump(text_dict, story_file, indent=4)

class GetStory:
    def __init__(self):
        self.get_story()

    def get_story(self):
        """gets a random the story dictionary"""
        with open("Story_collection.json", "r") as file:
            storys = json.load(file)

        random_num = random.choice(range(1,9))

        new_story_id = f"story{random_num}"

        self.story = storys[new_story_id]



