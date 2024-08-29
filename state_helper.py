import pandas as pd
import constants
import json

# USELESS

def get_state():
    try:
        with open('state.json', 'r') as file:
            state = json.load(file)
    except:
        state = None
    return state

def get_refit_date():
    state = get_state()
    try:
        date = pd.to_datetime(state["REFIT DATE"], format=constants.DATE_FORMAT)
    except:
        date = None
    return date

def update_state(adjust_state: dict):
    state = get_state()
    if state is None:
        state = {}
    state.update(adjust_state)
    with open('state.json', 'w') as file:
        json.dump(state, file, indent=4)

def set_refit_date(date: pd.Timestamp):
    update_state({"REFIT DATE": date.strftime(constants.DATE_FORMAT)})

if __name__ == "__main__":
    set_refit_date(pd.to_datetime("2010-12-21", format=constants.DATE_FORMAT))
    # print(get_state())
    pass