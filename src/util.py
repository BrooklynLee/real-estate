import os
import requests
import pandas as pd

def read_csv(filepath, header=None):
    return pd.read_csv(filepath, sep=",")

def read_tsv(filepath):
    return pd.read_csv(filepath, sep="\t")

def send_msg_to_slack(text):
    url = open("../config/slack.cfg", "r").readlines()[0][:-1]
    payload = "{\n\t\"text\": \""+text+"\"}"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "f0c31595-8d8f-3de1-fc1d-01ec4f93aecc"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

# READ RCODES
def get_rcode_df(filepath):
    f_in = open(filepath, "r")
    lines = [line[:-1].split(",") for line in f_in.readlines()]

    from collections import defaultdict
    r_dict = defaultdict() 
    for line in lines: 
        r_dict[line[0]] = [line[4], line[5], line[2]]

    import pandas as pd
    r_df = pd.DataFrame.from_dict(r_dict)
    r_df = r_df.transpose()
    # r_df.head(10) # metadata
    return r_df

DATA_PATH = '/home/irteam/blog/real-estate/data'
def load_data(rcode, trade_type):
    import glob
    filelist = glob.glob(os.path.join(DATA_PATH, "apt-{}/{}/*.csv".format(trade_type, rcode)))
    list_ = []
    for filepath in filelist[:-7]:
        print ('load %s ...' % filepath)
        df = read_tsv(filepath)
        list_.append(df)
    item_df = pd.concat(list_)
    return item_df

def get_data_by_trade_type(rcodes, trade_type):
    item_df_list = []
    for rcode in rcodes:
        item_df = load_data(rcode, trade_type) 
        # print '{}: {}'.format(r_df.loc[rcode], len(item_df))
        item_df_list.append(item_df)
    df = pd.concat(item_df_list)
    return df
