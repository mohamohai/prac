import pandas as pd
# import configparser
# import ast
from conf import config


# config.ini를 이용하는건데 쉽지않네;;
# config = configparser.ConfigParser()
# config.read('config.ini', encoding='utf-8')

# df_train = pd.read_csv(config.get('input_dat','train.csv'))
# df_test = pd.read_csv(config.get('input_dat','test.csv'))

# print('flag=',config.get('columns','drop_trn_flag'))
# print('cols= ',config.get('columns','drop_trn_cols'))

print('pyclos', config['input']['train'])
df_train = pd.read_csv(config['input']['train'])
print(config['columns']['drop_trn_flag'])


if config['columns']['drop_trn_flag'] == True:
    print('ok')
    df_train.drop(columns=config['columns']['drop_trn_cols'], axis=1, inplace=True)
print('result',df_train.columns)
    