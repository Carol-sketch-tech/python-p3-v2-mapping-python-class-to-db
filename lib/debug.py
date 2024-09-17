#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb
Department.drop_table()
Department.create_table()

payroll = Department.create('payroll','Building A, 5th Floor')
print(payroll)

hr = Department.create("Human resource", "Building C, East Wing")
print(hr)

food = Department.create('Cafeteria', 'Building C, West wing, 1st Floor')
print(food)

hr.name = 'HR'
hr.location = 'Building F, 10th Floor'
hr.update()
print(hr)

print('Delete Payroll')
payroll.delete()
print(payroll)

ipdb.set_trace()
