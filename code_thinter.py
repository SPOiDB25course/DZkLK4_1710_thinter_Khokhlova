import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Резюме")
        self.root.geometry("300x400")

        self.load_images()
        self.create_widgets()

    def load_images(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            images_dir = os.path.join(script_dir, "images")

            profile_path = os.path.join(images_dir, "Kotik.png")
            profile_img = Image.open(profile_path)
            profile_img = profile_img.resize((100, 100), Image.LANCZOS)
            self.profile_photo = ImageTk.PhotoImage(profile_img)

            background_path = os.path.join(images_dir, "skyblue.png")
            background_img = Image.open(background_path)
            background_img = background_img.resize((300, 140), Image.LANCZOS)
            self.background_photo = ImageTk.PhotoImage(background_img)
        
        except FileNotFoundError as error:
            print(f"Ошибка загрузки фото:\n{error}")

    def create_widgets(self):
        """Создание виджетов"""

        self.canvas = tk.Canvas(self.root, width = 300, height = 400)
        self.canvas.pack(fill="both", expand=True)

        if self.background_photo:
            self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        ikon_frame = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window(150, 70, window=ikon_frame, width=100, height=100)

        if self.profile_photo:
            profile_label = tk.Label(ikon_frame, image=self.profile_photo, bg="white")
            profile_label.pack()

        main_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window(150, 270, window=main_frame, width=300, height=260)

        user_label = tk.Label(main_frame, text="Мишель (Вермишель)", bg="white", fg='black', font=("Times New Roman", 20))
        user_label.place(x=25, y=0)  

        bio_label = tk.Label(main_frame, text="Биография", bg="white", fg='black',font=("Times New Roman", 17))
        bio_label.place(x=15, y=30)

        about_label = tk.Label(main_frame, 
                            text="Я маленький пушистый котёнок.", 
                            bg="white",fg='black', justify=tk.LEFT)
        about_label.place(x=15, y=60)

        skills_label = tk.Label(main_frame, text="Умения", bg="white", fg='black',font=("Times New Roman", 17))
        skills_label.place(x=15, y=85)

        languages_label = tk.Label(main_frame, text="Умиляю всех вокруг.", fg='black',bg="white")
        languages_label.place(x=15, y=110)

        languages_label = tk.Label(main_frame, text="Могу кричать Мяу всю ночь", fg='black',bg="white")
        languages_label.place(x=15, y=130)

        experience_label = tk.Label(main_frame, text="Опыт", bg="white", fg='black',font=("Times New Roman", 17))
        experience_label.place(x=15, y=155)

        developer_label = tk.Label(main_frame, text="Потрошитель диванов", fg='black',bg="white")
        developer_label.place(x=15, y=180)

        dev_dates_label = tk.Label(main_frame, text="Гроза ваз", fg='black',bg="white", font=("Times New Roman", 10))
        dev_dates_label.place(x=15, y=200)

        driver_label = tk.Label(main_frame, text="Поедатель цветов", fg='black',bg="white")
        driver_label.place(x=15, y=220)

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()
