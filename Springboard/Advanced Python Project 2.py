# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 06:11:35 2020

@author: James
"""

import datetime
account = [["Date", "Credit", "Debit", "Balance"]]

def transaction():
    now = datetime.datetime.now()
    dayMonthYear = str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    validInput = False
    while validInput == False:
        creditQ = input('Do you want to credit your account in this transaction? Y/N').lower()
        if (creditQ == 'y'):
            validInput = True
            credit = float(input('How much do you want to credit your account? '))
            if len(account) > 1:
                lastRow = account[len(account) - 1]
                newRow = [dayMonthYear, credit, 0, credit + lastRow[3]]
                account.append(newRow)
                print('Added', credit, 'to your account.')
                print('Your new balace is: ', account[len(account) - 1][3])