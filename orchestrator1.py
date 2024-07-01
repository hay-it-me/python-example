from data import data
from steps import step1
from steps import step2

def orchestrator(data):
    step1.step1(data)
    step2.step2(data)
    return data