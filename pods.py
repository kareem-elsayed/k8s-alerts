import subprocess
from operator import itemgetter


class Pod:
    def __init__(self):
        data = subprocess.check_output('kubectl get pods --all-namespaces', shell=True)
        data_decode = data.decode('ASCII')
        self.obj = data_decode.split()
        self.err_msg_list = [
                                "ErrImagePull",
                                "Error",
                                "CrashLoopBackOff",
                                "ImagePullBackOff",
                            ]

    def filtering_data(self):
        new = []
        for i in range(0, len(self.obj), 6):
            new.append(self.obj[i: i + 6])
        return new

    def catching_errors(self, list_of_pods):
        for e in self.err_msg_list:
            for i in list_of_pods:
                if e in i:
                    data = itemgetter(0, 1, 3)(i)  # select specific items from list of the pods
                    data_str = '    '.join(data)  # concatenate and convert items to strings
                    print(data_str)
