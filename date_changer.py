temp_created_date = input("Введите дату создания заметки в формате дд.мм.гггг:")
temp_issue_date = input("Введите дату завершения заметки в формате дд.мм.гггг:")

created_date = temp_created_date.replace(temp_created_date[2], ".")
issue_date = temp_issue_date.replace(temp_issue_date[2], ".")
print(
    "Дата создания заметки:",
    created_date[0:5],
    "\nДата завершения заметки: ",
    issue_date[0:5],
)
