from pods import Pod
from time import sleep


def main():
    data = Pod()
    pods_list = data.filtering_data(data.list_pods())
    data.catching_errors(pods_list)


while True:
    if __name__ == "__main__":
        print('----------Refresh----------')
        main()
        sleep(5)




