def home():
    return 'うめうめ梅宮のテキト〜さーばー。　なにかあったら euthanasia045@gmail.com まで'


def read_yaml(path):
    import yaml
    try:
        with open(path, mode='r') as config:
            data = yaml.load(config)
    except Exception as e:
        print(e)
        return
    else:
        return data


def read_api_path(path):
    try:
        with open(path, mode='r') as api:
            apis = api.read().split('\n')
            api_dict = {api.split(' ')[1]:api.split(' ')[0] for api in apis}
    except Exception as e:
        print(e)
        return
    else:
        return api_dict