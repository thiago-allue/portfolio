"""
https://molotov.readthedocs.io/en/stable/tutorial/
https://molotov.readthedocs.io/en/stable/cli/

w: worker
d: execution duration (seconds)
p: processes

molotov -w 1 -d 1 -p 1 -x molotoving.py
molotov -w 1 -d 1 -p 1 -x molotoving.py --statsd
"""

import time
import json

import molotov

_T = {}
concurs = []  # [(timestamp, worker count)]


def _now():
    return time.time() * 1000


@molotov.scenario(weight=100)
async def localhost(session):
    async with session.get('http://localhost:8080') as resp:
        assert resp.status == 200, resp.status


@molotov.events()
async def record_time(event, **info):
    if event == "current_workers":
        concurs.append((_now(), info["workers"]))
    req = info.get("request")
    if event == "sending_request":
        _T[req] = _now()
    elif event == "response_received":
        _T[req] = _now() - _T[req]

    if event == "scenario_start":
        scenario = info["scenario"]
        index = (info["wid"], scenario["name"])
        _T[index] = _now()
    if event == "scenario_success":
        scenario = info["scenario"]
        index = (info["wid"], scenario["name"])
        start_time = _T.pop(index, None)
        duration = int(_now() - start_time)
        if start_time is not None:
            print(
                json.dumps(
                    {
                        "ts": time.time(),
                        "type": "scenario_success",
                        "name": scenario["name"],
                        "duration": duration,
                    }
                )
            )
    elif event == "scenario_failure":
        scenario = info["scenario"]
        exception = info["exception"]
        index = (info["wid"], scenario["name"])
        start_time = _T.pop(index, None)
        duration = int(_now() - start_time)
        if start_time is not None:
            print(
                json.dumps(
                    {
                        "ts": time.time(),
                        "type": "scenario_failure",
                        "name": scenario["name"],
                        "exception": exception.__class__.__name__,
                        "errorMessage": str(exception),
                        "duration": duration,
                    }
                )
            )


@molotov.global_teardown()
def display_average():
    print(f"\nConcurrencies: {concurs}")
    delta = max(ts for ts, _ in concurs) - min(ts for ts, _ in concurs)
    average = sum(value for _, value in concurs) * 1000 / delta
    print(f"\nAverage concurrency: {average:.2f} VU/s")
