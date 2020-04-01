import subprocess
from operator import itemgetter
from time import sleep


def list_pods():
    data = subprocess.check_output('kubectl get pods --all-namespaces', shell=True)
    data_decode = data.decode('ASCII')
    convert_data = data_decode.split()
    return convert_data


def filtering_data(data):
    new = []
    for i in range(0, len(data), 6):
        new.append(data[i: i + 6])
    return new


def catching_errors(list_of_pods):
    err_msg_list = [
        "ErrImagePull",
        "Error",
        "CrashLoopBackOff",
        "ImagePullBackOff",
    ]
    for e in err_msg_list:
        for i in list_of_pods:
            if e in i:
                data = itemgetter(0, 1, 3)(i)   # select specific items from list of the pods
                data_str = '    '.join(data)    # concatenate and convert items to strings
                print(data_str)


def main():
    data = list_pods()
    filtered_data = filtering_data(data)
    catching_errors(filtered_data)


while True:
    if __name__ == "__main__":
        print('Refresh')
        main()
        sleep(5)




