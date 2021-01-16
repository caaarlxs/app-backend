def create(event, context):
    print(event)

    return True


if __name__ == '__main__':
    create(event={"name": "Antonio", "pwd": "9876", "company-name": "X"}, context="")
