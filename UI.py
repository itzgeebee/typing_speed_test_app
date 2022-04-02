from tkinter import *
from tkinter import messagebox
import pandas as pd
import datetime as dt
from data import GetStory

time_loop = None
get_story = GetStory()


class TypeEngine:
    def __init__(self):
        self.window = Tk()
        self.window.config(pady=10, padx=10, bg="#f7f5dd")
        self.window.title("Typing speed test ⚡⚡⚡")
        self.story = get_story.story
        self.entry_list = []
        self.text_list = []
        # self.reg = self.window.register(self.callback)

        self.welcome = Label(text="are you ready to test your typing speed?\n"
                                  "hit Enter to begin", bg="#f7f5dd", font=("Courier", 20))
        self.welcome.grid(row=5, column=0)

        self.enter_button = Button(text="Enter", bg="#9bdeac", font=("Courier", 20, "bold"), command=self.typing_screen)
        self.enter_button.grid(row=6, column=0)

        self.window.mainloop()

    def typing_screen(self):
        # self.welcome.config(text="", state="disabled")
        # self.enter_button.config(state="disabled")
        self.welcome.grid_forget()
        self.enter_button.grid_forget()
        self.canvas = Canvas(width=850, height=340, bg="#f7f5dd", highlightthickness=False)
        self.canvas.grid(row=1, column=0)
        # self.canvas2 = Canvas(width=200, height=200, bg="#e2979c")
        #
        # self.canvas2.grid(row=1, column=2)
        # self.timer_text = self.canvas2.create_text(1100, 70, text="00:00", fill="white", font=("Courier", 20, "bold"),
        #                                            anchor="sw", width=400)
        self.timer_txt = Label(text="00:00", font=("Courier", 20, "bold"), foreground="red", background="white")
        self.timer_txt.grid(row=0, column=0, pady=5)

        self.text_window = self.canvas.create_rectangle(32, 10, 814, 310, fill="white")
        self.test_text = self.canvas.create_text(36, 30, fill="black", anchor="nw", font=("Muli", "15"), width=760,
                                                 text=self.story)

        entry_label = Label(text="Hit start when ready and START typing in the space below ⤵", bg="#f7f5dd",
                            font=("Courier", "15", "bold"))
        entry_label.grid(row=3, column=0)
        self.entry1 = Entry(self.window, font=("Calibri", "18", "bold"), width=65, state="disabled", )
        # ys = Scrollbar(orient='vertical', command=self.entry1.yview)
        # self.entry1['yscrollcommand'] = ys.set
        # ys.grid(row=2, column=2)
        self.entry1.grid(row=4, column=0, pady=5)
        # entry1.grid(row=2,column=1)
        wm = Label(text="Made by Geebee", bg="#f7f5dd")
        wm.grid(row=6, column=0, columnspan=2, pady=5)

        start_button = Button(text="START", font=("Courier", "20", "bold"), bg="#9bdeac", foreground="black",
                              command=self.start_timer)
        start_button.grid(row=2, column=0, pady=5)

        stop_button = Button(text="STOP", font=("Courier", "20", "bold"), bg="#e2979c", foreground="black",
                             command=self.stop_timer)
        stop_button.grid(row=5, column=0, pady=5)

        # self.user_input = self.canvas2.create_window(20, 380, window=entry1, anchor="sw")

    def start_timer(self):
        self.entry1.config(state="normal")
        count = 59
        self.counter(count)

    def stop_timer(self):
        self.entry1.config(state="disabled")
        self.window.after_cancel(self.time_loop)
        self.timer_txt.config(text=self.counter_timer)
        self.display_result()
        # self.record_statistics()
        self.update_statistics()
        statistics_Button = Button(text="View Statistics", font=("Courier", "20", "bold"),
                                   bg="#9bdeac", foreground="black",
                                   command="")
        today = dt.datetime.now()
        self.day = today.date()
        self.score = self.wpm

    def display_result(self):
        print(self.count)
        self.used_time = round(((59 - self.count) / 59), 3)
        self.inaccurate = self.check_accuracy()
        print(self.used_time)
        self.wpm = round(len(self.entry_list)/self.used_time,0)
        messagebox.showinfo(title="Results", message=f"You had {self.wpm} words per minute \n"
                                                     f" and {self.inaccurate} inaccurate word(s)")
        self.entry1.delete(0, END)


        # count = 59
        # self.counter(count)

    def counter(self, count):

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

    # def callback(self):
    #     if self.entry1 == self.test_text:
    #         print(self.entry1)
    #         return True
    #
    #     else:
    #         print(self.entry1)
    #         return False

    def check_accuracy(self):
        a = 0
        word = ""
        for letter in self.entry1.get():
            if a % 5 == 0:
                self.entry_list.append(word)
                word = ""
            word += letter
            a += 1
        # print(self.entry_list)


        count_incorrect = 0

        entry_word_list = self.entry1.get().split(" ")
        total_words = len(entry_word_list)
        self.text_list = self.story.split(" ")[: total_words + 4]
        # print(self.text_list, entry_word_list)

        for i in range(total_words):

            if  entry_word_list[i] != self.text_list[i]:
                count_incorrect += 1
                # print(count_incorrect)
                # print(entry_word_list[i], self.text_list[i])

        accuracy = count_incorrect
        # print("accuracy:", accuracy)
        # print(total_words)

        return accuracy

    def record_statistics(self):
        statistics_list = [[self.day], [self.score]]
        self.df = pd.DataFrame(statistics_list).transpose()
        self.df.columns = ["date", "score"]
        self.df.to_csv("statistics.csv", index=False)

    def update_statistics(self):
        self.df.loc[len(self.df.index)] = [self.day, self.score]
