from pydantic import BaseModel, Field, validator

class FinancialData(BaseModel):
    yearly_income: float = Field(..., gt = 0)
    assets: float = Field(..., ge= 0)
    debt_ratio: float = 5.0
    max_morgage: float = 0.85

def calc_max_price(financials: FinancialData):
    """
    Räknar ut maximalt bolån beroende av inkomst och tillgångar.
    """
    try:
        max_loan_debt_ratio = financials.yearly_income * financials.debt_ratio #Räknar ut max bolån baserat på skuldkvot
        max_price_morgage = financials.assets / (1 - financials.max_morgage)
        max_house_price = min(max_price_morgage, max_loan_debt_ratio + financials.assets)

        return max_house_price
    
    except Exception as e:
        print(f"Ett fel uppstod vid beräkningen: {e}")
        return None

def run_calculation_prompt():
    """
    Funktion för att interagera med användaren och göra beräkningen
    """
    print("\n===BERÄKNA MAXIMALT BOSTADSPRIS===")

    while True:
        try: 
            yearly_income_input = input("Ange din totala årsinkomst, före skatteavdrag: ")
            assets_input = input("Ange ditt totala egna kapital/kontantinsats: ")

            yearly_income = float(yearly_income_input)
            assets = float(assets_input)

            financial_data = FinancialData(yearly_income= yearly_income, assets=assets)

            max_price = calc_max_price(financial_data)

            if max_price is not None:
                print(f"Baserat på dina uppgifter kan du köpa en bostad som kostar maximalt {max_price:,.2f} kronor.")
                break
        
        except ValueError:
            print("Ogiltig inmatning. Du behöver ange siffror.")
        
        except Exception as e:
            print(f"Ett fel uppstod {e}.")






# ======= MENY =======

while True:
    print("=============    VÄLKOMMEN TILL BOSTADSPRISBERÄKNAREN    =============")
    print("")
    print("=== Gör ett av följande val. Klicka på tangenten Q för att avsluta programmet: ===")
    print("")
    print("1. Vill du se hur mycket du kan köpa lägenhet för, baserat på din inkomst och dina tillgångar?")
    print("2. Har du hittat en bostad och vill se om du kan få ett lån?")
    print("____________________________________________________________")
    print("")
    choice = input("Skriv ditt val (1, 2 eller Q): ")

    if choice.lower() == "q":
        print("Programmet avslutas. ")
        break

    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            print("Du har valt 1")      #1. funktion som beräknar skuldkvot
            print("-------------------")
            run_calculation_prompt()
            break

        elif choice == 2:
            print("Du har valt 2")      #2. fuktion som beräknar levnadsomkostnader och hur mycket av lön som återstår efter
            break 

        else:
            print("Felaktig inmatning. Ange ditt val på nytt: ")
    
    else:
        print("Felaktig inmatning. Välj 1, 2 eller Q.")
        # Loopen fortsätter till nästa iteration

    
        