#!/usr/bin/python
# -*- coding: ascii -*-

"""
A - Task Scheduling Problem
Time Limit: 2 sec / Memory Limit: 1024 MB

Score :100 points

Problem Statement
You have three tasks, all of which need to be completed.

First, you can complete any one task at cost 0.
Then, just after completing the i-th task, you can complete the.
Find the minimum total cost required to complete all the task.
sample input: 1 6 3
sample output: 5
"""

def task_schedule(tasks):
    out = 0
    tasks = sorted(tasks)
    idx = tasks[0]
    for i in tasks[1:]:
        out += abs(i - idx)
        idx = i
    return out

tasks = list((int(x) for x in raw_input().split()))
print task_schedule(tasks)
