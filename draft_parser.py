import os
import time
import re

log_folder = 'logs'
os.chdir(log_folder)

# This draft is intended for refactoring; please do not use it as a reference for your solution.


def handle_eventnum(etc_events, raw_event):
    pattern = r'eventnum=\d+'
    matches = re.findall(pattern, raw_event)
    etc_events[matches[0]] = raw_event


def deal_with_event_pattern(event_pattern, raw_event, events_output):
    if event_pattern in raw_event:
        handle_eventnum(events_output, raw_event)
    return events_output


def deal_with_etc(raw_event, etc_events):
    deal_with_event_pattern('/etc/', raw_event, etc_events)
    return etc_events


def deal_with_system(raw_event, system_events):
    deal_with_event_pattern('/system/', raw_event, system_events)
    return system_events


def deal_with_network(raw_event, network_events):
    deal_with_event_pattern('/network/', raw_event, network_events)
    return network_events


def deal_with_auth(raw_event, auth_events):
    deal_with_event_pattern('auth|', raw_event, auth_events)
    return auth_events


events = {
    "etc": deal_with_etc,
    "system": deal_with_system,
    "network": deal_with_network,
    "auth": deal_with_auth
}


def main():
    print("Starting...")
    start = time.time()
    files = [f for f in os.listdir() if os.path.isfile(f) and not f.startswith('.')]
    print(files)
    etc_events = dict()
    system_events = dict()
    network_events = dict()
    auth_events = dict()

    # ----------------------------------------
    cnt = 0
    for file in files:
        with open(file) as fp:
            line = fp.readline()
            while line:  # line is our raw event!
                line = fp.readline()
                try:
                    events['etc'](line.strip(), etc_events)
                    events['system'](line.strip(), system_events)
                    events['network'](line.strip(), network_events)
                    events['auth'](line.strip(), auth_events)
                except EventException:
                    print("Broken event", line)
                finally:
                    cnt += 1

    print(cnt)
    print("etc events: ", len(etc_events))
    print("system events: ", len(system_events))
    print("network events: ", len(network_events))
    print("auth events: ", len(auth_events))
    # ----------------------------------------
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()