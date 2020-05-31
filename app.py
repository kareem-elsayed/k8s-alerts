import argparse
from pods import Pod
from time import sleep


parser = argparse.ArgumentParser(description = 'k8s alert helper!')
parser.add_argument("--d", default = 5, help = "set duration time in min (Default is 5)")
args = parser.parse_args()
d = args.d
d_time = int(d)


def main():
    data = Pod()
    pods_list = data.filtering_data()
    data.catching_errors(pods_list)


if __name__ == "__main__":
    while True:
        print('----------Refresh----------')
        main()
        sleep(d_time)




