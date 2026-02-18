<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>README - Bank Loan Simulator</title>
</head>
<body>

    <nav>
        <p>Language / Idioma: <strong>English</strong> | <a href="READMEpt.md">Versão em Português</a></p>
    </nav>

    <header>
        <h1>🏦 Bank Loan Simulator System</h1>
    </header>

    <section>
        <p>A professional terminal-based application developed in Python to simulate bank credit analysis and loan installments. This project demonstrates the implementation of financial business rules and robust data validation.</p>
    </section>

    <section>
        <h2>🚀 Features</h2>
        <ul>
            <li><strong>Name Validation:</strong> Ensures customer names contain only letters through specific string manipulation methods.</li>
            <li><strong>Safe Data Input:</strong> Manages invalid entries, such as letters in numeric fields, using error handling (try/except) to prevent application crashes.</li>
            <li><strong>Automated Credit Analysis:</strong> Evaluates eligibility based on income and debt-to-income ratios.</li>
            <li><strong>Financial Simulation:</strong> Calculates installments and the total repayment amount with a 2% monthly interest rate.</li>
            <li><strong>Interactive Menu:</strong> Professional interface with screen clearing and an operational loop to process multiple clients in a single session.</li>
        </ul>
    </section>

    <section>
        <h2>📋 Business Rules</h2>
        <ul>
            <li><strong>Minimum Income:</strong> Must be greater than R$ 2,000.00.</li>
            <li><strong>Installment Limit:</strong> Monthly payment cannot exceed 30% of the customer's gross income.</li>
            <li><strong>Interest Rate:</strong> 2% simple interest per month applied to the total duration.</li>
        </ul>
    </section>

    <section>
        <h2>🛠️ Technical Challenges & Solutions</h2>

        <h3>1. Function Scope and Data Hand-off</h3>
        <p>Initially, variables were being lost between functions. I solved this by implementing <strong>return</strong> statements, allowing functions to pass validated data back to the main controller.</p>

        <h3>2. Preventing Memory Leaks</h3>
        <p>I replaced recursive function calls (a function calling itself) with a <strong>while</strong> loop and <strong>break</strong> conditions. This keeps memory usage stable, even when processing many clients.</p>

        <h3>3. Cross-Platform Support</h3>
        <p>I added a conditional check to detect the operating system, ensuring the terminal clearing command works correctly on Windows (cls) or Unix/Mac (clear).</p>
    </section>

    <section>
        <h2>💻 How to Run</h2>
        <ol>
            <li>Clone the repository to your local machine.</li>
            <li>Open your terminal or command prompt.</li>
            <li>Navigate to the project folder.</li>
            <li>Run the command: <code>python main.py</code></li>
        </ol>
    </section>

    <hr id="portuguese">

    <section>
        <h2>🇧🇷 Versão em Português</h2>
        <p>O conteúdo em português pode ser acessado logo abaixo (ou em um arquivo separado). Clique no link abaixo para retornar ao topo.</p>
        <p><a href="#">Back to Top / Voltar ao Topo</a></p>
    </section>

    <footer>
        <hr>
        <h2>✍️ Author</h2>
        <p><strong>Renan</strong></p>
        <p>Connect with me on <a href="https://linkedin.com/in/renanbarbosaa">LinkedIn</a> or check my other projects on <a href="https://github.com/renanbarbosaaa">GitHub</a>.</p>
    </footer>

</body>
</html>