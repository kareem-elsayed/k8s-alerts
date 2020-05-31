import subprocess
from operator import itemgetter


class Pod:
    def __init__(self):
        data = subprocess.check_output('kubectl get pods --all-namespaces', shell = True)
        data_decode = data.decode('ASCII')
        self.obj = data_decode.split()
        self.err_msg_list = [
            "ErrImagePull",
            "Error",
            "CrashLoopBackOff",
            "ImagePullBackOff"
        ]

    # def filtering_data(self):
    #     new = []
    #     for i in range(0, len(self.obj), 6):
    #         new.append(self.obj[i: i + 6])
    #     return new

    def filtering_data(self):
        for i in range(0, len(self.obj), 6):
            yield (self.obj[i: i + 6])

    def catching_errors(self, list_of_pods):
        for items in list_of_pods:
            for err in self.err_msg_list:
                if err in items:
                    data = itemgetter(0, 1, 3)(items)  # select specific items from list of the pods
                    data_str = '    '.join(data)  # concatenate and convert items to strings
                    print(data_str)
