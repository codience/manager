def add_csv(value_list, state="一般"):
    for form in [f.split() for f in value_list][:2]:
        if not len(form) >= 2:
            print('The input may be strange.')
            return None
    import csv
    with open('./src/import_students_test.csv', mode='r') as f:
        try:
            reader = csv.reader(f)
            l = [row for row in reader]
            csv_header = l[0]
            latest_user_row = l[-1]
            id = int(latest_user_row[0]) + 1
            name = value_list[0]
            kana = value_list[1]
            state = state
            sex = "男性" if value_list[2] == "man" else "女性"
        except Exception as e:
            print(e)
            exit(0)
    new_row = [id, name, kana, state, sex, '', '一般']
    with open('./src/import_students_test.csv', 'a') as af:
        writer = csv.writer(af, lineterminator='\n')
        writer.writerow(new_row)
