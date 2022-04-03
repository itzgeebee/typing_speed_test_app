# import the required liraries and packages
import csv
from tkinter import *
from tkinter import messagebox
import datetime as dt
from data import GetStory
from do_statistics import PlotGraph

plotter = PlotGraph()
# create a time loop variable for the time
time_loop = None

# initialize the story object
get_story = GetStory()


class TypeEngine:
    def __init__(self):

        """initializes the opening window"""
        # new Tk window
        self.window = Tk()
        self.window.config(pady=10, padx=10, bg="#f7f5dd")
        self.window.title("Typing speed test ⚡⚡⚡")

        # get the story from the get story object
        self.story = get_story.story
        self.entry_list = []
        self.text_list = []

        # opening message
        self.welcome = Label(text="are you ready to test your typing speed?\n"
                                  "hit Enter to begin", bg="#f7f5dd", font=("Courier", 20))
        self.welcome.grid(row=5, column=0)

        self.enter_button = Button(text="Enter", bg="#9bdeac", font=("Courier", 20, "bold"), command=self.typing_screen)
        self.enter_button.grid(row=6, column=0)

        self.window.mainloop()

    def typing_screen(self):

        # make the welcome text and button disappear
        self.welcome.grid_forget()
        self.enter_button.grid_forget()

        # canvas to display story text
        self.canvas = Canvas(width=850, height=340, bg="#f7f5dd", highlightthickness=False)
        self.canvas.grid(row=1, column=0)

        # timer text
        self.timer_txt = Label(text="00:00", font=("Courier", 20, "bold"), foreground="red", background="white")
        self.timer_txt.grid(row=0, column=0, pady=5)

        # text window in form of a canvas rectangle
        self.text_window = self.canvas.create_rectangle(32, 10, 814, 310, fill="white")
        self.test_text = self.canvas.create_text(36, 30, fill="black", anchor="nw", font=("Muli", "15"), width=760,
                                                 text=self.story)

        entry_label = Label(text="Hit start when ready and START typing in the space below ⤵", bg="#f7f5dd",
                            font=("Courier", "15", "bold"))
        entry_label.grid(row=3, column=0)

        self.entry1 = Entry(self.window, font=("Calibri", "18", "bold"), width=65, state="disabled", )
        self.entry1.grid(row=4, column=0, pady=5)

        wm = Label(text="Made by Geebee", bg="#f7f5dd")
        wm.grid(row=6, column=0, columnspan=2, pady=5)

        self.start_button = Button(text="START", font=("Courier", "20", "bold"), bg="#9bdeac", foreground="black",
                              command=self.start_timer)
        self.start_button.grid(row=2, column=0, pady=5)

        self.stop_button = Button(text="STOP", font=("Courier", "20", "bold"), bg="#e2979c", foreground="black",
                                  command=self.stop_timer)
        self.stop_button.grid(row=5, column=0, pady=5)

    def start_timer(self):
        """This function starts the countdown timer"""

        self.entry1.config(state="normal")
        self.entry1.delete(0, END)
        count = 59
        self.counter(count)

    def stop_timer(self):
        """stops the timer countdown and calls the functions that follow"""
        self.entry1.config(state="disabled")
        self.window.after_cancel(self.time_loop)
        self.timer_txt.config(text=self.counter_timer)
        self.display_result()
        today = dt.datetime.now()
        self.day = today.date()
        self.score = self.wpm
        self.record_statistics()
        # self.window.after(12000, self.window.quit)

        # pending feature
        statistics_Button = Button(text="View Statistics", font=("Courier", "20", "bold"),
                                   bg="#9bdeac", foreground="black",
                                   command="")

    def display_result(self):
        """ displays the speed and accuracy of the concluded session"""
        self.start_button.config(state="disabled")
        self.stop_button.config(state="disabled")
        self.used_time = round(((59 - self.count) / 59), 3)
        self.inaccurate = self.check_accuracy()
        self.wpm = round(len(self.entry_list) / self.used_time, 0)
        messagebox.showinfo(title="Results", message=f"You had {self.wpm} words per minute \n"
                                                     f" and {self.inaccurate} inaccurate word(s)")
        self.window.after(5000, plotter.plot_data, self.window, 1, 0)

    def counter(self, count):
        """timer countdown function"""
        count_sec = str(count)
        if count < 10:
            count_sec = "0" + str(count_sec)
        self.counter_timer = f"00:{count_sec}"

        self.timer_txt.config(text=self.counter_timer)
        if count > 0:
            self.time_loop = self.window.after(1000, self.counter, count - 1)
        else:
            self.stop_timer()
        self.count = count

    def check_accuracy(self):
        """reurns the accuracy of the user entry """
        a = 0
        word = ""
        # 5 characters = one word, append the entry into a list after every 5 chars
        for letter in self.entry1.get():
            if a % 5 == 0:
                self.entry_list.append(word)
                word = ""
            word += letter
            a += 1

        count_incorrect = 0

        # create word list to check for accuracy
        entry_word_list = self.entry1.get().split(" ")
        total_words = len(entry_word_list)
        self.text_list = self.story.split(" ")[: total_words + 4]

        for i in range(total_words):
            if entry_word_list[i] != self.text_list[i]:
                count_incorrect += 1

        accuracy = count_incorrect
        return accuracy

    def record_statistics(self):
        """records the wpm of the session into a csv file"""
        try:

            with open("statistics.csv", mode="r") as stat_file:
                data = csv.reader(stat_file)
        except FileNotFoundError:
            with open("statistics.csv", mode="w") as stat_file:
                fieldnames = ['Date', "score"]
                stat_writer = csv.writer(stat_file)
                stat_writer.writerow(fieldnames)
                stat_writer.writerow([self.day, self.score])

        else:
            with open("statistics.csv", mode="a") as stat_file:
                stat_writer = csv.writer(stat_file)
                stat_writer.writerow([self.day, self.score])
