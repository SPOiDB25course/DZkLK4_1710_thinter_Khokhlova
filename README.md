Десктопное приложение для отображения резюме, разработанное с использованием Tkinter и Pillow для работы с изображениями.

### Требования
- Python 3.6 или выше
- Pillow - для обработки изображений
- Tkinter - встроенная библиотека для графического интерфейса (обычно включается в стандартную поставку Python)

### Установка зависимостей
```bash
# Установка Pillow для работы с изображениями
pip install Pillow
```

### Структура проекта
```bash
├── images/
│   ├── skyblue.png          # Фоновое изображение
│   ├── profile_image.png          # Изображение для примера
│   └── Kotik.png    # Аватар профиля
├── code_tkinter.py   # Основной файл приложения
└── README.md                # Документация
```
Запуск приложения
```bash
python code_tkinter.py
```

## Используемые библиотеки
### GUI Framework - Tkinter
Основной фреймворк для создания графического интерфейса

Tk() - Главное окно приложения - root = tk.Tk()
Canvas - Холст для рисования и размещения элементов -	self.canvas = tk.Canvas()
Frame -	Контейнер для группировки виджетов - main_frame = tk.Frame()
Label -	Отображение текста и изображений	- user_label = tk.Label()

### PIL (Pillow) - Обработка изображений

Image.open() -	Загрузка изображений	- Image.open(profile_path)
Image.resize()	- Изменение размера изображения	- resize((100, 100), Image.LANCZOS)
ImageTk.PhotoImage	- Конвертация для Tkinter -	ImageTk.PhotoImage(profile_img)

### Системные библиотеки

os	- Работа с файловой системой -	os.path.join(), os.path.dirname()

## Архитектура приложения
Класс ResumeApp
__init__(self, root)

- Инициализация главного окна
- Настройка параметров приложения
```bash
def __init__(self, root):
    self.root = root
    self.root.title("Резюме")
    self.root.geometry("300x400")
```
load_images(self)

- Загрузка и подготовка изображений
- Обработка ошибок файловой системы
```bash
def load_images(self):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, "images")
```
create_widgets(self)

- Создание и компоновка всех элементов интерфейса
- Использование Canvas для гибкого позиционирования
```bash
def create_widgets(self):
    self.canvas = tk.Canvas(self.root, width=300, height=400)
    self.canvas.pack(fill="both", expand=True)
```

### Структура интерфейса
## Основные компоненты:

1. Canvas - основной фон приложения
2. Фоновое изображение - растянуто на верхней части
3. Фрейм аватара - контейнер для фотографий профиля
4. Основной фрейм - содержит всю текстовую информацию

## Разделы информации:

Личная информация - имя и биография
Навыки - что-то кошачье
Опыт работы - то, что котик уже успел сделать

### Особенности реализации
1. Работа с изображениями
```bash
# Автоматическое определение путей
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, "images")

# Масштабирование с высоким качеством
profile_img = profile_img.resize((100, 100), Image.LANCZOS)
```
2. Гибкое позиционирование
```bash
# Использование Canvas для точного позиционирования
self.canvas.create_window(150, 70, window=ikon_frame, width=100, height=100)
```
3. Стилизация элементов
```bash
# Настройка шрифтов и цветов
user_label = tk.Label(main_frame, text="Dungeon Master", 
                     bg="white", fg='black', font=("Times New Roman", 20))
```
