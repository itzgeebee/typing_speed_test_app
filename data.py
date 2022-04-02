import json
import random

stories = ["One day Jimmy Westfielder was walking home from school and saw a big,"
           "brown dog walking behind him. At first he was a bit startled at the fact"
           " that the dog was just calmly walking behind him. Jimmy stopped and turned"
           " around to face the dog. When Jimmy looked into the dog's eyes he became"
           "  Cognizant that the dog meant no harm at all. Jimmy bent down to the dog's "
           "level and put one of his hands out. As soon as Jimmy did so the dog began to "
           "lick  Jimmy's hand. Jimmy then checked to see if the dog had a collar, "
           "which he didn't, and when he didn't find a collar he then said, "
           "'Hello my name is Jimmy. I see that you don't have an owner so I will take you in."
           "Since I live with my older brother I'm pretty sure he won't mind one bit.' "
           "The dog looked at Jimmy as if he could understand every word that Jimmy said. "
           "'I will have to name you.' Jimmy looked at the dog intensely while thinking of a name "
           "for the dog that he would call 'his own'. 'How about I call you Astro.'",

           "It was winter, bitter and cold. The wind rushing against her skin made her wish she was never here. "
           "Without proper materials for human survival, all hope was lost. "
           "Nobody was seen for miles and miles, nothing but snow and more cold. "
           "The cold is all she could ever think about. It got so bad to the point where the only objective was to put "
           "one foot in front of the other. Just as she saw a glimmer of light shine "
           "throughout the broken night sky, it was over.",

           "Weren't they supposed to put in a left-hand turn lane three years ago? "
           "he thought as he waited through three lights at the intersection with Exchange Street."
           "The rain started when he crossed Miller, increased as he turned onto the professional "
           "building's drive. Walking in from the physicians parking lot, his umbrella was useless "
           "against the sheets of water blown in a pelting slant. He didn't make it up to the office "
           "until almost 8:30, and he sat shivering in wet clothes while he tried to race through "
           "the morning's files. His first patient was running late. She took up more time than she had been "
           "allotted for her presurgical, repeating all kinds of inane questions about her upcoming procedure.",

           "No one can escape it. The doctor reveled in it. He wore his age like a weapon, like an accusation, "
           "refusing even the mildest of his own remedies.Once he had wanted to change people's lives, "
           "save them from the crippling effects of facial disfigurement. Now he only wanted to make it through each day."
           " The doctor had a very comfortable routine. He rose every morning at six o'clock, sipped coffee and "
           "watched the weather report. In the office by 7:30 to review files and get ready for the first "
           "patient at nine. He would prescribe creams and ointments, perform minor surgical procedures under "
           "local anesthetic, do follow-up checks.",

           "Two hours off for lunch, then out the door by five on the dot. Stop by the florist for a fresh bouquet-something"
           " to match up with the multi-floral pattern of Clara's curtains, all the better if on sale. Home by six to catch "
           "the evening news while he ate whatever the housekeeper had prepared him for dinner. "
           "Though he used to enjoy cooking occasionally, he'd rarely touched the stove since Clara died, "
           "some twenty-odd years ago. Didn't seem worth the energy to cook for one. "
           "The housekeeper made large meals that could be frozen in individual portions, "
           "placed a different selection in the oven to warm for him each night.",

           "He ate slowly, commenting to himself on one news story or another, and left the dishes in the sink. "
           "In bed by nine, where he would read the latest medical journals, "
           "lingering over photos of freakish skin disease. Cutting-edge disorders undergoing treatment at cutting-edge "
           "clinics with whole staffs of researchers and technicians. A private practice like his, "
           "in an off-the-map town like Pekore, Ohio, couldn't compete. New York, Houston, even "
           "Cleveland-that's where things were happening. But Clara had picked this place. "
           "A place for children to roam shady neighborhoods, a place for lives instead of careers. "
           "So Pekore was where he stayed.",

           "Now, the pages in these monthly journals were his sustenance. He found some meaning, "
           "in the painful beauty of human eyes suffering behind inhuman faces, "
           "that was entirely absent from his own office full of truly ugly people "
           "parading through with their psyches shattered over trifles. "
           "At 10:30, by an instinct so ingrained that his bedside clock had become a "
           "redundancy, he would tear himself away from even the most engaging of case "
           "studies, mark and close his journal, switch the light and fall almost "
           "instantly into an animal sleep. It was not a strenuous existence. "
           "He didn't like to be strained. But on this particular Monday, he was strained.",

           "The late-spring weather hung low and heavy, with crackles of lightning threatening to "
           "burst the sky open. A fire at one of the old farmhouses along 271 had emergency vehicles "
           "blocking his usual route. When he tried to turn around, "
           "the crowd of gathered on-lookers slowed his retreat. Then traffic on "
           "Mason Road, his only alternate, inched forward at less than half the "
           "normally crawling rush-hour pace. Weren't they supposed to put in a "
           "left-hand turn lane three years ago? he thought as he waited through "
           "three lights at the intersection with Exchange Street. "
           "The rain started when he crossed Miller, increased as he turned onto the "
           "professional building's drive."

           ]
text_dict = {}
a = 1
for num in range(1, 9):
    text_dict[f'story{a}']= stories[a - 1]
    a += 1

with open("Story_collection.json", "w") as story_file:
    json.dump(text_dict, story_file, indent=4)

class GetStory:
    def __init__(self):
        self.get_story()

    def get_story(self):
        with open("Story_collection.json", "r") as file:
            storys = json.load(file)

        random_num = random.choice(range(1,9))

        new_story_id = f"story{random_num}"

        self.story = storys[new_story_id]



