Claro, aqui está o conteúdo para o seu README de forma simplificada, apenas com textos e sem tabelas ou colunas:

Bank Loan Simulator System
A professional Python terminal application designed to simulate bank credit analysis and loan installments. This project showcases the implementation of financial business rules and robust data validation.

Features
Robust Name Validation: Ensures customer names contain only letters using specific string methods.

Safe Data Input: Handles invalid entries like letters in numeric fields using error treatment to prevent crashes.

Automated Credit Analysis: Evaluates eligibility based on income and debt-to-income ratios.

Financial Simulation: Calculates installments and total repayment with a 2% monthly interest rate.

Interactive Menu: Professional interface with screen clearing and an operational loop to process multiple clients.

Business Rules
Minimum Income: Must be greater than R$ 2,000.00.

Installment Limit: Monthly payment cannot exceed 30% of the customer's gross income.

Interest Rate: Simple interest of 2% per month applied to the total duration.

Technical Challenges and Solutions
Function Scope and Data Hand-off:
Initially, variables were getting lost between functions. I solved this by implementing return statements, allowing functions to pass validated data back to the main controller.

Preventing Memory Leaks:
I replaced recursive function calls with a while loop and break conditions. This keeps memory usage stable even when processing many clients in a single session.

Cross-Platform Support:
I added a conditional check to detect the operating system, ensuring the terminal clears correctly on Windows, Linux, or Mac.

How to Run
Clone the repository to your local machine.

Open your terminal or command prompt.

Navigate to the project folder.

Run the command: python main.py