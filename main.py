import requests
import json
import time
from consolemenu import *
from consolemenu.items import *

fill_test_cases = [[50, 90, 15], #Test case 1
                   [50, 60, 15], #Test case 2
                   [30, 15]]     #Test case 3
overheat_test_case = [300, 1500]
fill_delay = 120 # time in seconds before sending command

machine_id = 864622110032548

def send_throw_trash(percentage):

    range = -percentage + 155
    url = "https://ncs-srb-001.dynv6.net:1880/throwTrash.do?garbageIndex=1&type=3"

    payload = json.dumps({
    "dataList": [
        {
        "garbageIndex": 1,
        "type": 9,
        "weight": 100,
        "beforeWeight": 1434,
        "afterWeight": 1441,
        "range": range
        }
    ],
    "idCode": f"{machine_id}",
    "idContent": "1234567890",
    "idType": 7,
    "time": int(time.time() * 1000)
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)

def send_overheat():
    url = "https://ncs-srb-001.dynv6.net:1880/errorCode.do"

    payload = json.dumps({
    "dataList": [
        {
        "temperature": "82",
        "errorCode": 311,
        "errorStatus": 1
        }
    ],
    "idCode": f"{machine_id}",
    "time": 1671282752000
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.status_code)

def run_throw_trash_test(fill_cases, delay):
    for index, level in enumerate(fill_cases):

        print(f"Setting fill level of bin {machine_id} to {level} percent")
        send_throw_trash(level)
        if index != len(fill_cases) - 1:
            for i in range(delay,0,-1):
                print(f"Calling next fill level case in {i} seconds", end="\r", flush=True)
                time.sleep(1)
        else:
            input("Test case completed. Press Enter to continue...")

def overheat_test():
    for index, delay in enumerate(overheat_test_case):

        print(f"Sending out an overheat alert from {machine_id}")
        send_overheat()
        if index != len(overheat_test_case) - 1:
            for i in range(delay,0,-1):
                print(f"Waiting {i} seconds before sending next alert", end="\r", flush=True)
                time.sleep(1)
        else:
            input("Test case completed. Press Enter to continue...")

def p_list(l, i):
    return ','.join([str(x) for x in l[i]])

if __name__ == '__main__':

    menu = ConsoleMenu("EPD Test Scripts", "Select a test script")

    overheat_case = FunctionItem("Overheat Case", overheat_test, [])

    throw_trash_item1 = FunctionItem(f"Run fill case {p_list(fill_test_cases, 0)}", run_throw_trash_test, [fill_test_cases[0], fill_delay])
    throw_trash_item2 = FunctionItem(f"Run fill case {p_list(fill_test_cases, 1)}", run_throw_trash_test, [fill_test_cases[1], fill_delay])
    throw_trash_item3 = FunctionItem(f"Run fill case {p_list(fill_test_cases, 2)}", run_throw_trash_test, [fill_test_cases[2], fill_delay])
    fill_case_menu = ConsoleMenu("EPD Test Scripts", "Select a test script")
    fill_case_submenu_item = SubmenuItem("Fill Cases", fill_case_menu, menu)

    fill_case_menu.append_item(throw_trash_item1)
    fill_case_menu.append_item(throw_trash_item2)
    fill_case_menu.append_item(throw_trash_item3)
    menu.append_item(fill_case_submenu_item)
    menu.append_item(overheat_case)
    menu.show()

