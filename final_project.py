from tkinter import *
from tkinter import ttk
import re
from datetime import datetime

from methods_sort.bubble_sort import bubble_sort
from methods_sort.counting_sort import counting_sort
from methods_sort.heap_sort import heap_sort
from methods_sort.merge_sort import merge_sort
from methods_sort.quick_sort import quick_sort
from methods_sort.radix_sort import radix_sort

labels_list = []
scroll_list = []
labels_time_list = []

# Очистка/Добавление в буфер обмена
def copy_to_clipboard(str_int):
    window.clipboard_clear()  # Очистить буфер обмена
    window.clipboard_append(str_int)  # Добавить текст в буфер обмена

# Кнопка 'Copy' для копировани в буфер обмена
def button_copy(str_int):
    b3 = Button(window, text='Copy', command=copy_to_clipboard(str_int), font=20, bg='yellow')
    b3.place(x=420, y=220)

# Текстовое поле вывода
def output_text(str_int):

    global scroll_list
    if scroll_list:   # удалить последний scroll
        scroll_list.pop().destroy()

    # Создаем Frame (в нем будем хранить наш текстовый вывод и прокрутку)
    frame = ttk.Frame(borderwidth=1, relief=SOLID, width=400, height=500)
    frame.place(x=30, y=220)

    # Создаем текстовое поле
    txt = Text(frame, width=40, font=('Arial', 12, 'bold'), bg='lightblue', height=5)
    txt.pack(side=LEFT, fill='y')
    txt.insert(1.0, str(str_int))

    # Создаем вертикальную полосу прокрутки
    scroll = Scrollbar(frame, orient = VERTICAL, command = txt.yview)
    scroll.pack(side=RIGHT, fill='y')
    # Добавляем в список scroll, чтобы потом удалить (для обновления в window) 
    scroll_list.append(scroll)

    # Конфигурируем поле с полосой прокрутки
    txt.configure(yscrollcommand = scroll.set)

# Основная функция выполнения разных методов сортировки
def start_sort():

    list_int = [] # список для чисел
    if labels_list:   # удаляем последний label в списке
        labels_list.pop().destroy()

    # получаем значения с каждого label (name, surname и age)
    name = str_name.get()

    if name != '':
        list_name = re.split(',',name)
        for l in list_name:
            try:
                l = int(l)
                list_int.append(l)
            finally: # если не int значение, продолжаем, не добавляем в list
                continue

        if not list_int:
            # выводим label, в случае, если ввели неверные данные
            label4 = Label(window, text=('Не является числовой последовательностью!')
                , font=('Arial', 12, 'bold'), bg='red')
            label4.place(x=370, y=70)
            # добавляем в список label4, чтобы потом удалить (для обновления в window)
            labels_list.append(label4)

    else:
        # выводим label, в случае, если ввели пустые значения (такое не будем вводить в нашу БД, чтобы не копились пустые строки)
        label4 = Label(window, text='Вы ввели пустые данные!', font=('Arial', 12, 'bold'), bg='red')
        label4.place(x=370, y=70)
        # добавляем в список label4, чтобы потом удалить (для обновления в window) 
        labels_list.append(label4)

    if list_int:

        # время начала выполнения
        start_time = datetime.now()

        if combobox.get() == 'Сортировка пузырьком (Bubble Sort)':
            list_int = bubble_sort(list_int)

        elif combobox.get() == 'Сортировка подсчетом (Counting Sort)':
            list_int = counting_sort(list_int)

        elif combobox.get() == 'Пирамидальная сортировка (Heap Sort)':
            heap_sort(list_int)

        elif combobox.get() == 'Сортировка слиянием (Merge Sort)':
            list_int = merge_sort(list_int)

        elif combobox.get() == 'Быстрая сортировка (Quick Sort)':
            list_int = quick_sort(list_int)

        elif combobox.get() == 'Поразрядная сортировка (Radix Sort)':
            list_int = radix_sort(list_int)
            
        else:
            # выводим label
            label4 = Label(window, text='Необходимо выбрать метод сортировки!', font=('Arial', 12, 'bold'), bg='red')
            label4.place(x=370, y=150)
            # добавляем в список label4, чтобы потом удалить (для обновления в window) 
            labels_list.append(label4)

        if combobox.get() != 'Какой метод сортировки выбрать?':

            # вычисляем затраченное время на сортировку
            execution_time = end_time(start_time)
            # выводим на наше окно (window)
            get_label_time(execution_time)

            # Текстовое поле вывода
            str_int = ','.join(str(elem) for elem in list_int)
            output_text(str_int)

            # Создаем кнопку для копирования полученной последовательности в буфер обмена
            button_copy(str_int)

# функция для вычисления затрченного времени на сортировку
def end_time(start_time):
    end_time = datetime.now()  # время окончания выполнения
    execution_time = (end_time - start_time).total_seconds()*10**6 # вычисляем время выполнения (в мирокосекундах)

    return execution_time

# функция для добавления label (execution_time)
def get_label_time(execution_time):
    global labels_time_list
    if labels_time_list:   # удалить последний label3
        labels_time_list.pop().destroy()
    
    # Создаем текстовое поле, чтобы вывподить затраченное время на выполнение сортировки
    label3 = Label(window, text=f"Время затраченное на выполнение сортировки: {execution_time} микросекунд", font=('Hack 20', 10, 'bold'))
    label3.place(x=30, y=320)
    labels_time_list.append(label3)


if __name__== "__main__":

    # Создаем графическое окно
    window = Tk()
    window.title('Сортировка последовательности чисел') # заголовок окна
    window.geometry('770x400') # размер окна

    # ~~~~~~~ Ввод текста ~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Добавляем label для ввода
    label1 = Label(window, text='Последовательность чисел (через запятую)', font=('Hack 20', 20, 'bold'))
    label1.place(x=30, y=25)
    # добавляем Entry для str_name
    str_name = Entry(font=('Hack 20', 18, 'bold'), width=25)
    str_name.place(x=30, y=70)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~~~ Варианты сортировок ~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Добавляем label для ввода
    label2 = Label(window, text='Список методов сортировки', font=('Hack 20', 20, 'bold'))
    label2.place(x=30, y=110)
    # Список методов
    list_sort= [
        'Сортировка пузырьком (Bubble Sort)',
        'Сортировка подсчетом (Counting Sort)',
        'Пирамидальная сортировка (Heap Sort)',
        'Сортировка слиянием (Merge Sort)',
        'Быстрая сортировка (Quick Sort)',
        'Поразрядная сортировка (Radix Sort)']
    # Создаем виджет со списком
    combobox = ttk.Combobox(window, textvariable = StringVar(), width=50)
    combobox.set('Какой метод сортировки выбрать?')
    combobox['values'] = list_sort
    combobox['state'] = 'readonly'
    combobox.place(x=30, y=150)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~~~ Сортировка последовательности (Start) ~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Добавляем button(кнопку) для ввода последовательности чисел и выполнения сортировки
    btn_switch1 = Button(window, text='Start', bg='orange', fg='red',
                width=20, font=("Hack 20", 14, 'bold'), command=start_sort)
    btn_switch1.place(x=30, y=180) 
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # цикл обработки событий окна
    window.mainloop()