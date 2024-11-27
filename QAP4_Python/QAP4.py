'''
Author: Ashton Dennis
Dates: November 18, 2024 - November 21, 2024
Desc: Calculate insurance policy information for the One Stop Insurance Company
'''
import FormatValues as FV
import datetime as dt
from time import sleep
import os
import sys

# Program Constants
POLICY_NUM = "1944"
PREMIUM_RATE = 869.00
DISCOUNTED_PREMIUM_RATE = PREMIUM_RATE - (PREMIUM_RATE * 0.25)
LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_COVERAGE_COST = 58.00
HST = 0.15
PROCESSING_FEE = 39.99
PROV_TERR_LST = ["NL", "PE", "NS", "NB", "QC", "ON", \
                 "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
PAY_TYPE_LST = ["Full", "Monthly", "Down Payment"]
INVOICE_DATE = dt.date.today()
FIRST_PAYMENT_DATE = (INVOICE_DATE.replace(day=1) + dt.timedelta(days=32)).replace(day=1)
NOT = False
NOTNOT = True

# Program Functions
def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

def HandleClaims():
    # I'm so sorry in advance for this section, but it's funny!
    claims = []
    twprint("\nClaims:")
    while True:
        while not False:
            claimNum = twinput("Enter Claim Number (#####): ")
            if len(claimNum) == 5 and claimNum.isdigit():
                break
            else:
                twprint("\nInvalid Input. Claim Number must be 5 digits\n")

        while not not True:
            try:
                claimDate = dt.datetime.strptime(twinput("Enter Claim Date (YYYY-MM-DD): "), "%Y-%m-%d")
            except:
                twprint("\nInvalid Input. Claim Date must be in the format \"YYYY-MM-DD\"\n")
            else:
                break
        
        while not not not NOT:
            try:
                claimAmt = float(twinput("Enter Claim Amount: "))
            except:
                print("\nInvalid Input. Claim Amount must be a number\n")
            else:
                break
        
        claims.append([claimNum, FV.FormatDateShort(claimDate), FV.FormatDollar2(claimAmt)])
        while not not not not NOTNOT:
            # Validating
            match twinput("Would you like to process another claim? (Y/N): ").upper():
                case "Y":
                    print()
                    break
                case "N":
                    return claims
                case _:
                    twprint("\nInvalid Input. Input must be \"Y\" or \"N\"\n")

# I made these 2 functions myself with the help of the internet.
# I did not copy-paste this from anywhere.
def twprint(*values: object, delay: float | None = 0.03, sep: str | None = " ", end: str | None = "\n"):
    """
    Prints the values to sys.stdout with a typewriter effect.\n
    Optional keyword arguments:\n
    delay: speed in which text appears. default 0.03s\n
    sep: string inserted between values, default a space.\n
    end: string appended after the last value, default a newline.\n
    """
    for value in values:
        value = str(value)
        for c in value:
            sleep(delay)
            sys.stdout.write(c)
            sys.stdout.flush()
        sys.stdout.write(sep)
        sleep(delay)
    sys.stdout.write(end)
    return None

def twinput(prompt: object = ""):
    """
    Read a string from standard input. The trailing newline is stripped.\n
    The prompt string, if given, is printed with a typewriter effect to standard output without a trailing newline before reading input.
    """
    twprint(prompt, end="", sep="")
    val = sys.stdin.readline().replace("\n", "")
    return val

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear()

    # Inputs
    fName = twinput("Enter First Name: ").title()
    lName = twinput("Enter Last Name: ").title()
    streetAddr = twinput("Enter Street Address: ").title()
    city = twinput("Enter City Name: ").title()

    # Validate Province/Territory
    while True:
        provTerr = twinput("Enter Province/Territory (XX): ").upper()
        if provTerr in PROV_TERR_LST:
            break
        else:
            twprint(f"\nInvalid Input. There is no province/territory \"{provTerr}\"\n")

    # Validate Postal Code
    while True:
        PostalCode = twinput("Enter Postal Code (X#X#X#): ").upper()
        if len(PostalCode) != 6:
            twprint("\nInvalid Input. Postal Code must be 6 characters long...\n")
        else:
            valid = True
            for i in range(len(PostalCode)):
                if (i % 2 == 0 and not PostalCode[i].isalpha()) or (i % 2 == 1 and not PostalCode[i].isdigit()):
                    twprint("Invalid Input. Postal Code must be in the format \"X#X#X#\"")
                    valid = False
                    break
            if valid:
                break

    phoneNum = FV.FormatPhone(twinput("Enter Phone Number (10 digits): ")) 

    while True:
        try:
            numCarsInsured = int(twinput("Enter Amount Of Cars Being Insured: "))
        except:
            twprint("\nInvalid Input. Number of cars insured must be a number\n")
        else:
            if numCarsInsured > 0:
                break
            else:
                twprint("\nInvalid Input. Number of cars insured must be at least 1\n")


    xtraLiability = twinput("Would you like to add extra liability? (Y/N): ").upper()
    glassCoverage = twinput("Would you like to add glass coverage? (Y/N): ").upper()
    loanerCar = twinput("Would you like a loaner car? (Y/N): ").upper()

    while True:
        payType = twinput("How would you like to pay? (Full/Monthly/Down Payment): ").title()
        if payType in PAY_TYPE_LST:
            break
        else:
            twprint("\nInvalid Input. Payment type must be \"Full\", \"Monthly\", or \"Down Payment\"\n")

    # Accepts user input if payment type is "Down Payment", otherwise defaults to 0
    downPayAmt = float(twinput("Enter Down Payment Amount: ")) if payType == "Down Payment" else 0

    # Calculations
    basicPremium = PREMIUM_RATE
    additionalCars = DISCOUNTED_PREMIUM_RATE * (numCarsInsured - 1)
    totalPremiums = basicPremium + additionalCars


    totalExtraCosts = 0
    if xtraLiability == "Y":
        totalExtraCosts += LIABILITY_COST * numCarsInsured
    if glassCoverage == "Y":
        totalExtraCosts += GLASS_COVERAGE_COST * numCarsInsured
    if loanerCar == "Y":
        totalExtraCosts += LOANER_COVERAGE_COST * numCarsInsured

    subtotal = totalPremiums + totalExtraCosts - downPayAmt

    hst = subtotal * HST

    total = subtotal + hst

    monthly = (total + PROCESSING_FEE) / 8

    claims = HandleClaims()

    sleep(0.5)
    clear()

    for i in range(31):
        sleep(0.1)
        ProgressBar(i, 30, "Generating Receipt", "Done", 50)
    print()
    sleep(0.7)
    clear()

    # Display Variables
    fullName = f"{fName[0]}. {lName}"

    fullAddr = [streetAddr, f"{city}, {provTerr} {PostalCode}"]

    extrasDsp = []
    for element in [xtraLiability, glassCoverage, loanerCar]:
        if element == "Y":
            extrasDsp.append("Yes")
        else:
            extrasDsp.append("No")

    downPayDsp = FV.FormatDollar2(downPayAmt) if downPayAmt != 0 else "N/A"

    calcsDsp = []
    for element in [basicPremium, additionalCars, totalPremiums, totalExtraCosts, subtotal, hst, total, monthly, PROCESSING_FEE]:
        calcsDsp.append(FV.FormatDollar2(element))
    
    datesDsp = []
    for element in [INVOICE_DATE, FIRST_PAYMENT_DATE]:
        datesDsp.append(FV.FormatDateShort(element))

    # Outputs
    print()
    print( "         1         2         3         4        ")
    print( "123456789012345678901234567890123456789012345678")
    print()
    print( "---------------One Stop Insurance---------------")
    print(f"Name:             {fullName:>30s}")
    print()
    print(f"Address:     {fullAddr[0]:>35s}")
    print(f"        {fullAddr[1]:>40s}")
    print()
    print(f"Phone:                            {phoneNum:>14s}")
    print( "------------------------------------------------")
    print(f"Cars Insured:                                 {numCarsInsured:>02d}")
    print(f"Extra Liability:                             {extrasDsp[0]:>3s}")
    print(f"Glass Coverage:                              {extrasDsp[1]:>3s}")
    print(f"Loaner Car:                                  {extrasDsp[2]:>3s}")
    print( "------------------------------------------------")
    print(f"Payment Option:                     {payType:>12s}")
    print(f"Down Payment:                         {downPayDsp:>10s}")
    print( "------------------------------------------------")
    print(f"Basic Premium:                        {calcsDsp[0]:>10s}")
    print(f"Additional Cars:                      {calcsDsp[1]:>10s}")
    print( "                                      ----------")
    print(f"Total Insurance Premiums:             {calcsDsp[2]:>10s}")
    print(f"Extra Costs:                          {calcsDsp[3]:>10s}")
    print( "                                      ----------")
    print(f"Subtotal:                             {calcsDsp[4]:>10s}")
    print(f"Tax (HST):                            {calcsDsp[5]:>10s}")
    print( "                                      ----------")
    print(f"Total:                                {calcsDsp[6]:>10s}")
    if payType != "Full":
        print( "------------------------------------------------")
        print(f"Processing Fee:                       {calcsDsp[8]:>10s}")
        print(f"Monthly Payment:                      {calcsDsp[7]:>10s}")
        print(f"First Payment Date:                   {datesDsp[1]:>10s}")
    print( "================================================")
    print(f"Issued:                               {datesDsp[0]:>10s}")
    print(f"Policy Number:                              {POLICY_NUM:>4s}")
    print( "================================================")
    print()

    # Claims Output
    print( "                 Claim History:")
    print( "       ==================================")
    print( "       Claim #   Claim Date        Amount")
    print( "       ----------------------------------")
    for lst in claims:
        print(f"        {lst[0]:<5s}    {lst[1]}    {lst[2]:>10s}")
    print( "       ==================================\n")

    while True:
        match twinput("Would you like to process another customer? (Y/N): ").upper():
            case "Y":
                break
            case "N":
                exit(0)
            case _:
                twprint("\nInvalid Input. Selection must be \"Y\" or \"N\"\n")