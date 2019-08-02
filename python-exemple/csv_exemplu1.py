from csv import reader, writer


def delete_users(first, last):
    with open("users.csv") as csv_file:
        csv_reader = reader(csv_file)
        rows = list(csv_reader)

    count = 0

    with open("users.csv", "w") as csv_file:
        csv_writer = writer(csv_file)
        for row in rows:
            if row[0] == first and row[1] == last:
                count += 1
            else:
                csv_writer.writerow(row)
    return "Users deleted: {}.".format(count)


delete_users("Colt", "Steel")
