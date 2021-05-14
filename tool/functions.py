import pandas as pd
# import xlwt
import os


def taking_Attendance(Upload_folder, todays_attendace, attendance_register, date=None):
    todays_attendace = pd.read_excel(todays_attendace, engine="openpyxl")
    attendance_register = pd.read_excel(attendance_register, engine="openpyxl")
    columns = list(attendance_register.columns.values)
    total_students = list(attendance_register['Roll No.'])
    students = list(todays_attendace['Roll No.'])
    date = list(todays_attendace['Timestamp'])
    todays_attendace['Date'] = [str(i).split(' ')[0] for i in date]
    date = list(todays_attendace['Timestamp'])
    date = list(set(date))
    date.sort()
    for i in date:
        presented_total_students = todays_attendace['Timestamp'] == i
        presented_total_students = todays_attendace.loc[presented_total_students]
        presented_total_students = presented_total_students['Roll No.'].to_list(
        )
        attendance_register[i] = 'A'

        for student in presented_total_students:
            if student in total_students:
                attendance_register[i][total_students.index(
                    student)] = 'P'
    filename = os.path.join(Upload_folder, 'output.xlsx')
    attendance_register.to_excel(filename, index=0)

    return 'output.xlsx'
