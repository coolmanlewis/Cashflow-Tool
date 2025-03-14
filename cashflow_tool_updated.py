import pandas as pd
import ace_tools_open as tools  # Ensure ace_tools is installed and available

class PropertyAnalysis:
    def __init__(self):
        self.properties = []

    def add_property(self, address, down_payment, interest_rate, loan_term):
        property_data = self.fetch_property_data(address)
        if not property_data:
            print(f"Failed to fetch data for address: {address}")
            return
        property_data.update({
            'Address': address,
            'Down Payment': down_payment,
            'Interest Rate': interest_rate,
            'Loan Term': loan_term
        })
        self.calculate_cash_flow(property_data)
        self.properties.append(property_data)

    def fetch_property_data(self, address):
        # Placeholder for API call to fetch property details
        example_data = {
            'Purchase Price': 250000,
            'Expected Rent': 1800,
            'Monthly Expenses': 300,
            'Vacancy Rate': 0.05,
            'Maintenance Rate': 0.1,
            'Management Fee Rate': 0.1
        }
        return example_data

    def calculate_cash_flow(self, property_data):
        loan_amount = property_data['Purchase Price'] - property_data['Down Payment']
        
        monthly_interest_rate = property_data['Interest Rate'] / 12 / 100
        total_payments = property_data['Loan Term'] * 12

        # Handle case where interest rate is 0 to prevent division by zero
        if monthly_interest_rate > 0:
            monthly_mortgage_payment = (
                loan_amount * monthly_interest_rate
            ) / (1 - pow((1 + monthly_interest_rate), -total_payments))
        else:
            monthly_mortgage_payment = loan_amount / total_payments  # Simple division for zero interest

        gross_income = property_data['Expected Rent']
        vacancy_loss = gross_income * property_data['Vacancy Rate']
        maintenance_cost = gross_income * property_data['Maintenance Rate']
        management_fee = gross_income * property_data['Management Fee Rate']

        net_income = gross_income - vacancy_loss - maintenance_cost - management_fee
        cash_flow = net_income - property_data['Monthly Expenses'] - monthly_mortgage_payment

        property_data.update({
            'Monthly Mortgage Payment': round(monthly_mortgage_payment, 2),
            'Net Income': round(net_income, 2),
            'Cash Flow': round(cash_flow, 2)
        })

    def generate_report(self):
        if not self.properties:
            print("No properties to generate a report.")
            return
        df = pd.DataFrame(self.properties)
        tools.display_dataframe_to_user(name="Property Analysis Report", dataframe=df)

# Usage Example
property_analysis = PropertyAnalysis()
property_analysis.add_property("123 Main St", down_payment=50000, interest_rate=5.5, loan_term=30)
property_analysis.generate_report()
