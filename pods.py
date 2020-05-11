import subprocess
from operator import itemgetter


class Pod:
    def list_pods(self):
        data = subprocess.check_output('kubectl get pods --all-namespaces', shell=True)
        data_decode = data.decode('ASCII')
        convert_data = data_decode.split()
        return convert_data

    def filtering_data(self, obj):
        new = []
        for i in range(0, len (obj), 6):
            new.append(obj[i: i + 6])
        return new

    def catching_errors(self, list_of_pods):
        err_msg_list = [
            "ErrImagePull",
            "Error",
            "CrashLoopBackOff",
            "ImagePullBackOff",
        ]
        for e in err_msg_list:
            for i in list_of_pods:
                if e in i:
                    data = itemgetter(0, 1, 3)(i)  # select specific items from list of the pods
                    data_str = '    '.join(data)  # concatenate and convert items to strings
                    print(data_str)
