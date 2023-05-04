from ttkbootstrap import Style
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import time

style = Style(theme="superhero")
main_window = style.master
main_window.title("Cash Book")
main_window.geometry("1280x720")

# do function when click "calculat" button (save the list entered by the user and calculate the total price).


def calculate_click():
    try:
        pay_list = en1.get()
        price = float(en2.get())
        text_list1 = lebel_list1.cget("text")
        text_list2 = lebel_list2.cget("text")
        text_list3 = lebel_list3.cget("text")
        text_list4 = lebel_list4.cget("text")
        text_list5 = lebel_list5.cget("text")
        text_list6 = lebel_list6.cget("text")
        text_list7 = lebel_list7.cget("text")
        text_list8 = lebel_list8.cget("text")
        text_list9 = lebel_list9.cget("text")
        text_total1 = lebel_total1.cget("text")
        text_total2 = lebel_total2.cget("text")
        text_total3 = lebel_total3.cget("text")
        text_total4 = lebel_total4.cget("text")
        text_total5 = lebel_total5.cget("text")
        text_total6 = lebel_total6.cget("text")
        text_total7 = lebel_total7.cget("text")
        text_total8 = lebel_total8.cget("text")
        text_total9 = lebel_total9.cget("text")

        try:
            int_total2 = float(text_total1) + price
            int_total3 = float(text_total2) + price
            int_total4 = float(text_total3) + price
            int_total5 = float(text_total4) + price
            int_total6 = float(text_total5) + price
            int_total7 = float(text_total6) + price
            int_total8 = float(text_total7) + price
            int_total9 = float(text_total8) + price
        except:
            pass

        if (text_list1 == ""):
            lebel_list1.configure(text="1. " + pay_list)
            lebel_price1.configure(text=price)
        elif (text_list2 == ""):
            lebel_list2.configure(text="2. " + pay_list)
            lebel_price2.configure(text=price)
        elif (text_list3 == ""):
            lebel_list3.configure(text="3. " + pay_list)
            lebel_price3.configure(text=price)
        elif (text_list4 == ""):
            lebel_list4.configure(text="4. " + pay_list)
            lebel_price4.configure(text=price)
        elif (text_list5 == ""):
            lebel_list5.configure(text="5. " + pay_list)
            lebel_price5.configure(text=price)
        elif (text_list6 == ""):
            lebel_list6.configure(text="6. " + pay_list)
            lebel_price6.configure(text=price)
        elif (text_list7 == ""):
            lebel_list7.configure(text="7. " + pay_list)
            lebel_price7.configure(text=price)
        elif (text_list8 == ""):
            lebel_list8.configure(text="8. " + pay_list)
            lebel_price8.configure(text=price)
        elif (text_list9 == ""):
            lebel_list9.configure(text="9. " + pay_list)
            lebel_price9.configure(text=price)

        if (text_total1 == ""):
            lebel_total1.configure(text=price)
        elif (text_total2 == ""):
            lebel_total2.configure(text=int_total2)
        elif (text_total3 == ""):
            lebel_total3.configure(text=int_total3)
        elif (text_total4 == ""):
            lebel_total4.configure(text=int_total4)
        elif (text_total5 == ""):
            lebel_total5.configure(text=int_total5)
        elif (text_total6 == ""):
            lebel_total6.configure(text=int_total6)
        elif (text_total7 == ""):
            lebel_total7.configure(text=int_total7)
        elif (text_total8 == ""):
            lebel_total8.configure(text=int_total8)
        elif (text_total9 == ""):
            lebel_total9.configure(text=int_total9)
        lebel_error.configure(text="")

    except:
        lebel_error.configure(text="Price should be only number")

# do function when click "Clear All" button (clears all lists entered by the user).


def clear_all_click():
    lebel_list1.configure(text="")
    lebel_price1.configure(text="")
    lebel_total1.configure(text="")
    lebel_list2.configure(text="")
    lebel_price2.configure(text="")
    lebel_total2.configure(text="")
    lebel_list3.configure(text="")
    lebel_price3.configure(text="")
    lebel_total3.configure(text="")
    lebel_list4.configure(text="")
    lebel_price4.configure(text="")
    lebel_total4.configure(text="")
    lebel_list5.configure(text="")
    lebel_price5.configure(text="")
    lebel_total5.configure(text="")
    lebel_list6.configure(text="")
    lebel_price6.configure(text="")
    lebel_total6.configure(text="")
    lebel_list7.configure(text="")
    lebel_price7.configure(text="")
    lebel_total7.configure(text="")
    lebel_list8.configure(text="")
    lebel_price8.configure(text="")
    lebel_total8.configure(text="")
    lebel_list9.configure(text="")
    lebel_price9.configure(text="")
    lebel_total9.configure(text="")
    lebel_error.configure(text="")

# do function when click "Delete 1 item" button (deletes 1 entry that the user entered last).


def clear_click():
    text_list1 = lebel_list1.cget("text")
    text_list2 = lebel_list2.cget("text")
    text_list3 = lebel_list3.cget("text")
    text_list4 = lebel_list4.cget("text")
    text_list5 = lebel_list5.cget("text")
    text_list6 = lebel_list6.cget("text")
    text_list7 = lebel_list7.cget("text")
    text_list8 = lebel_list8.cget("text")
    text_list9 = lebel_list9.cget("text")
    if (text_list9 != ""):
        lebel_list9.configure(text="")
        lebel_price9.configure(text="")
        lebel_total9.configure(text="")
    elif (text_list8 != ""):
        lebel_list8.configure(text="")
        lebel_price8.configure(text="")
        lebel_total8.configure(text="")
    elif (text_list7 != ""):
        lebel_list7.configure(text="")
        lebel_price7.configure(text="")
        lebel_total7.configure(text="")
    elif (text_list6 != ""):
        lebel_list6.configure(text="")
        lebel_price6.configure(text="")
        lebel_total6.configure(text="")
    elif (text_list5 != ""):
        lebel_list5.configure(text="")
        lebel_price5.configure(text="")
        lebel_total5.configure(text="")
    elif (text_list4 != ""):
        lebel_list4.configure(text="")
        lebel_price4.configure(text="")
        lebel_total4.configure(text="")
    elif (text_list3 != ""):
        lebel_list3.configure(text="")
        lebel_price3.configure(text="")
        lebel_total3.configure(text="")
    elif (text_list2 != ""):
        lebel_list2.configure(text="")
        lebel_price2.configure(text="")
        lebel_total2.configure(text="")
    elif (text_list1 != ""):
        lebel_list1.configure(text="")
        lebel_price1.configure(text="")
        lebel_total1.configure(text="")
    lebel_error.configure(text="")

# do function when click "Download" button (list the information in a text file named with the user-entered date information and download it).


def download_click():
    try:
        input_day = int(enter_day.get())
        input_month = int(enter_month.get())
        input_year = enter_year.get()
        if ((input_day <= 31) & (input_day >= 1) & (input_month <= 12) & (input_month >= 1)):
            if (input_month == 1):
                str_month = "Jan"
            elif (input_month == 2):
                str_month = "Fab"
            elif (input_month == 3):
                str_month = "Mar"
            elif (input_month == 4):
                str_month = "Apr"
            elif (input_month == 5):
                str_month = "May"
            elif (input_month == 6):
                str_month = "Jun"
            elif (input_month == 7):
                str_month = "Jul"
            elif (input_month == 8):
                str_month = "Aug"
            elif (input_month == 9):
                str_month = "Sep"
            elif (input_month == 10):
                str_month = "Oct"
            elif (input_month == 11):
                str_month = "Nov"
            elif (input_month == 12):
                str_month = "Dec"
            str_day = str(input_day)
            str_year = "20" + input_year
            this_day = str_day + "-" + str_month + "-" + str_year
            print(this_day)
            print(type(this_day))
            text_list1 = lebel_list1.cget("text")
            text_list2 = lebel_list2.cget("text")
            text_list3 = lebel_list3.cget("text")
            text_list4 = lebel_list4.cget("text")
            text_list5 = lebel_list5.cget("text")
            text_list6 = lebel_list6.cget("text")
            text_list7 = lebel_list7.cget("text")
            text_list8 = lebel_list8.cget("text")
            text_list9 = lebel_list9.cget("text")
            text_price1 = lebel_price1.cget("text")
            text_price2 = lebel_price2.cget("text")
            text_price3 = lebel_price3.cget("text")
            text_price4 = lebel_price4.cget("text")
            text_price5 = lebel_price5.cget("text")
            text_price6 = lebel_price6.cget("text")
            text_price7 = lebel_price7.cget("text")
            text_price8 = lebel_price8.cget("text")
            text_price9 = lebel_price9.cget("text")
            text_total1 = lebel_total1.cget("text")
            text_total2 = lebel_total2.cget("text")
            text_total3 = lebel_total3.cget("text")
            text_total4 = lebel_total4.cget("text")
            text_total5 = lebel_total5.cget("text")
            text_total6 = lebel_total6.cget("text")
            text_total7 = lebel_total7.cget("text")
            text_total8 = lebel_total8.cget("text")
            text_total9 = lebel_total9.cget("text")
            my_file = open("%s.txt" % this_day, 'w')
            print(my_file)
            my_file.write("Revenue Accounts".center(140, " ") + "\n")
            my_file.write("".center(140, "-") + "\n")
            my_file.write("{:100s} {:20s} {:20s}\n".format(
                "List", "Price", "Total"))
            my_file.write("".center(140, "-") + "\n")
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list1, str(text_price1), str(text_total1)))
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list2, str(text_price2), str(text_total2)))
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list3, str(text_price3), str(text_total3)))
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list4, str(text_price4), str(text_total4)))
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list5, str(text_price5), str(text_total5)))
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list6, str(text_price6), str(text_total6)))
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list7, str(text_price7), str(text_total7)))
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list8, str(text_price8), str(text_total8)))
            my_file.write("{:100s} {:21s} {:10s}\n".format(
                text_list9, str(text_price9), str(text_total9)))
            lebel_error.configure(text="")
        else:
            lebel_error.configure(
                text="day should be 1-31, month should be 1-12")

    except:
        lebel_error.configure(text="Date should be only number")

# do function when click "Today" button (list the information in a text file named with the current date and download it).


def date_click():
    this_time = time.localtime()
    st_time = time.asctime(this_time)
    time_list = list(st_time.split(" "))
    this_day = time_list[2] + "-" + time_list[1] + "-" + time_list[4]
    text_list1 = lebel_list1.cget("text")
    text_list2 = lebel_list2.cget("text")
    text_list3 = lebel_list3.cget("text")
    text_list4 = lebel_list4.cget("text")
    text_list5 = lebel_list5.cget("text")
    text_list6 = lebel_list6.cget("text")
    text_list7 = lebel_list7.cget("text")
    text_list8 = lebel_list8.cget("text")
    text_list9 = lebel_list9.cget("text")
    text_price1 = lebel_price1.cget("text")
    text_price2 = lebel_price2.cget("text")
    text_price3 = lebel_price3.cget("text")
    text_price4 = lebel_price4.cget("text")
    text_price5 = lebel_price5.cget("text")
    text_price6 = lebel_price6.cget("text")
    text_price7 = lebel_price7.cget("text")
    text_price8 = lebel_price8.cget("text")
    text_price9 = lebel_price9.cget("text")
    text_total1 = lebel_total1.cget("text")
    text_total2 = lebel_total2.cget("text")
    text_total3 = lebel_total3.cget("text")
    text_total4 = lebel_total4.cget("text")
    text_total5 = lebel_total5.cget("text")
    text_total6 = lebel_total6.cget("text")
    text_total7 = lebel_total7.cget("text")
    text_total8 = lebel_total8.cget("text")
    text_total9 = lebel_total9.cget("text")
    my_file = open("%s.txt" % this_day, 'w')
    print(my_file)
    my_file.write("Revenue Accounts".center(140, " ") + "\n")
    my_file.write("".center(140, "-") + "\n")
    my_file.write("{:100s} {:20s} {:20s}\n".format("List", "Price", "Total"))
    my_file.write("".center(140, "-") + "\n")
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list1, str(text_price1), str(text_total1)))
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list2, str(text_price2), str(text_total2)))
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list3, str(text_price3), str(text_total3)))
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list4, str(text_price4), str(text_total4)))
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list5, str(text_price5), str(text_total5)))
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list6, str(text_price6), str(text_total6)))
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list7, str(text_price7), str(text_total7)))
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list8, str(text_price8), str(text_total8)))
    my_file.write("{:100s} {:21s} {:10s}\n".format(
        text_list9, str(text_price9), str(text_total9)))
    lebel_error.configure(text="")


def enterClick(event):
    calculate_click()


def remove1(event):
    clear_click()


def exit(event):
    main_window.destroy()


main_window.bind("<Return>", enterClick)
main_window.bind("<Delete>", remove1)
main_window.bind("<Escape>", exit)

# GUI part
money_img = ImageTk.PhotoImage(Image.open("money.png").resize((100, 100)))
img1 = ttk.Label(main_window, image=money_img)
img1.place(x=705, y=5)

head_lebel = ttk.Label(main_window, text="Cash Book", font=(
    "Helvetica 30 bold"), anchor=tk.CENTER)
head_lebel.place(x=465, y=30, width=220)

ize_lebel = ttk.Label(main_window, text='"by Ize"', font=(
    "Helvetica 12 bold"), anchor=tk.CENTER)
ize_lebel.place(x=1100, y=30, width=220)


lebel_list = ttk.Label(main_window, text="List", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list.place(x=200, y=100)

lebel_price = ttk.Label(main_window, text="Price", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price.place(x=850, y=100, width=120)

lebel_total = ttk.Label(main_window, text="Total", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total.place(x=1020, y=100, width=120)

en1 = ttk.Entry(main_window, font=("Helvetica 20 bold"), foreground='white')
en1.place(x=200, y=140, width=600, height=50)

en2 = ttk.Entry(main_window, font=("Helvetica 20 bold"), foreground='white')
en2.place(x=850, y=140, width=120, height=50)

calculate_button = ttk.Button(main_window, text="Calculate", cursor="hand2", style=(
    "success.Outline.TButton"), command=calculate_click)
calculate_button.place(x=1030, y=145, width=100, height=40)

calculate_button = ttk.Button(main_window, text="Delete 1 item", cursor="hand2", style=(
    "danger.TButton"), command=clear_click)
calculate_button.place(x=945, y=665, width=150, height=40)

calculate_button = ttk.Button(main_window, text="Clear All", cursor="hand2", style=(
    "danger.TButton"), command=clear_all_click)
calculate_button.place(x=1110, y=665, width=150, height=40)

lebel_list1 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list1.place(x=200, y=210, width=600, height=50)

lebel_price1 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price1.place(x=850, y=210, width=120, height=50)

lebel_total1 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total1.place(x=1020, y=210, width=120, height=50)

lebel_list2 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list2.place(x=200, y=260, width=600, height=50)

lebel_price2 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price2.place(x=850, y=260, width=120, height=50)

lebel_total2 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total2.place(x=1020, y=260, width=120, height=50)

lebel_list3 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list3.place(x=200, y=310, width=600, height=50)

lebel_price3 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price3.place(x=850, y=310, width=120, height=50)

lebel_total3 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total3.place(x=1020, y=310, width=120, height=50)

lebel_list4 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list4.place(x=200, y=360, width=600, height=50)

lebel_price4 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price4.place(x=850, y=360, width=120, height=50)

lebel_total4 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total4.place(x=1020, y=360, width=120, height=50)

lebel_list5 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list5.place(x=200, y=410, width=600, height=50)

lebel_price5 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price5.place(x=850, y=410, width=120, height=50)

lebel_total5 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total5.place(x=1020, y=410, width=120, height=50)

lebel_list6 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list6.place(x=200, y=460, width=600, height=50)

lebel_price6 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price6.place(x=850, y=460, width=120, height=50)

lebel_total6 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total6.place(x=1020, y=460, width=120, height=50)

lebel_list7 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list7.place(x=200, y=510, width=600, height=50)

lebel_price7 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price7.place(x=850, y=510, width=120, height=50)

lebel_total7 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total7.place(x=1020, y=510, width=120, height=50)

lebel_list8 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list8.place(x=200, y=560, width=600, height=50)

lebel_price8 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price8.place(x=850, y=560, width=120, height=50)

lebel_total8 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total8.place(x=1020, y=560, width=120, height=50)

lebel_list9 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.W)
lebel_list9.place(x=200, y=610, width=600, height=50)

lebel_price9 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_price9.place(x=850, y=610, width=120, height=50)

lebel_total9 = ttk.Label(main_window, text="", font=(
    "Helvetica 20 bold"), anchor=tk.CENTER)
lebel_total9.place(x=1020, y=610, width=120, height=50)

lebel_date = ttk.Label(main_window, text="Write Date",
                       font=("Helvetica 15 bold"), anchor=tk.CENTER)
lebel_date.place(x=20, y=630, width=180, height=40)

lebel_date_sign = ttk.Label(main_window, text="/",
                            font=("Helvetica 28 bold"), anchor=tk.CENTER)
lebel_date_sign.place(x=70, y=662, width=15, height=40)

lebel_date_sign2 = ttk.Label(
    main_window, text="/", font=("Helvetica 28 bold"), anchor=tk.CENTER)
lebel_date_sign2.place(x=134, y=662, width=15, height=40)

enter_day = ttk.Entry(main_window, font=(
    "Helvetica 20 bold"), foreground='white')
enter_day.place(x=20, y=665, width=48, height=40)

enter_month = ttk.Entry(main_window, font=(
    "Helvetica 20 bold"), foreground='white')
enter_month.place(x=86, y=665, width=47, height=40)

enter_year = ttk.Entry(main_window, font=(
    "Helvetica 20 bold"), foreground='white')
enter_year.place(x=150, y=665, width=48, height=40)

date_button = ttk.Button(main_window, text="Download", cursor="hand2", style=(
    "success.TButton"), command=download_click)
date_button.place(x=220, y=665, width=160, height=40)

download_button = ttk.Button(main_window, text="Today", cursor="hand2", style=(
    "success.TButton"), command=date_click)
download_button.place(x=395, y=665, width=160, height=40)

lebel_error = ttk.Label(main_window, text="", font=(
    "Helvetica 13 bold"), anchor=tk.CENTER,foreground='red')
lebel_error.place(x=575, y=665, width=350, height=40)

# style configuration part
style.configure('success.Outline.TButton', font=("Helvetica", 13, "bold"))
style.configure('danger.TButton', font=("Helvetica", 15, "bold"))
style.configure('success.TButton', font=("Helvetica", 12, "bold"))

# open window loop
main_window.mainloop()