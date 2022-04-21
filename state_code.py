import pandas as pd 
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-s", "--state", help="OFFICAL STATE NAME", nargs='+')
args = parser.parse_args()


df = pd.read_csv("state_code.csv")
states_data = df.to_dict(orient='records')


def state_code(state_provided):
    for states in states_data:
        if state_provided == states['State']:
            print("STATE AND STATE CODE: {} , {}".format(states['State'], states['Abbreviation']))
            return states['Abbreviation'] 

state_code(' '.join(args.state))
