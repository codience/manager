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