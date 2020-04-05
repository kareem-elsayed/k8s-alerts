from kubernetes import client, config
import ast


def get_container_statuses():
    v1 = client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        if i.status.phase == 'Pending':
            str_data = str(i.status.container_statuses)
            str_data = ast.literal_eval(str_data)  # convert what is looks likes a list data type
            dict_data = str_data[0]  # get just the dict inside the list
            return dict_data


def catch_container_error(data):
    for k, v in data.items():
        if k == "state":
            print(v)


def main():
    config.load_kube_config()
    data = get_container_statuses()
    catch_container_error(data)


main()


'''
print(f'{i.metadata.namespace}  ' f'{i.metadata.name}   ' + f'{i.status.phase}  ' + '   Warning')
'''
