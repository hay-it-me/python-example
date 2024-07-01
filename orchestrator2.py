from data import data
from steps import step1
from steps import step3

def orchestrator(data):
    step1.step1(data)
    step3.step3(data)
    return data