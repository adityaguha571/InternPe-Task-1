import tkinter as tk
O_unicode = "\u2B55" 
X_unicode = "\u274C" 
class TicTacToe(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.board = [""] * 9
        self.player = X_unicode

    def create_widgets(self):
        self.buttons = []
        font_size=10; 
        font = ("Arial", font_size, "bold")
        for i in range(9):
            button = tk.Button(self, text="", width=20, height=10,font=font, command=lambda i=i: self.button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].configure(text=self.player, state=tk.DISABLED)
            if self.check_winner(self.player):
                winner_label = tk.Label(self, text=f"Winner {self.player} !!", fg="red", font=("Arial", 20, "bold"))
                winner_label.grid(row=3, column=0, columnspan=3)
                self.disable_buttons()
            else:
                self.player = O_unicode if self.player == X_unicode else X_unicode

    def check_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]              
        ]
        for combination in winning_combinations:
            if all(self.board[i] == player for i in combination):
                return True
        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.configure(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    app = TicTacToe(master=root)
    app.pack()
    root.geometry("700x700")
    root.configure(bg="silver")
    app.configure(bg="white")


    # button colors
    button_color = "#E0E0E0"
    active_button_color = "#BDBDBD"
    for button in app.buttons:
        button.configure(bg=button_color, activebackground=active_button_color)

    root.mainloop()
