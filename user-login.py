
def login (event, context):
    print(event)
    user = {"name":"Carlos", "pwd":"1234"}
    if user == event:
        return True
    else:
        return False


if __name__ == '__main__':
    event ={"name":"Carlos", "pwd":"1234"}
    print(login(event, context= ""))