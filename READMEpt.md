<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>README - Simulador Bancário</title>
</head>
<body>

    <h1>🏦 Sistema de Simulador de Empréstimo Bancário</h1>

    <p>Uma aplicação profissional de terminal desenvolvida em Python para simular análises de crédito bancário e parcelamentos. Este projeto demonstra a implementação de regras de negócio financeiras e validação robusta de dados.</p>

    <h2>🚀 Funcionalidades</h2>
    <ul>
        <li><strong>Validação de Nome:</strong> Garante que os nomes dos clientes contenham apenas letras através de métodos específicos de manipulação de texto.</li>
        <li><strong>Entrada de Dados Segura:</strong> Gerencia entradas inválidas, como letras em campos numéricos, utilizando tratamento de erros (try/except) para evitar que o programa feche.</li>
        <li><strong>Análise de Crédito Automática:</strong> Avalia a elegibilidade com base na renda e na relação entre dívida e rendimentos.</li>
        <li><strong>Simulação Financeira:</strong> Calcula parcelas e o valor total de pagamento com uma taxa de juros de 2% ao mês.</li>
        <li><strong>Menu Interativo:</strong> Interface profissional com limpeza de tela e um laço operacional para processar vários clientes em uma única sessão.</li>
    </ul>

    

    <h2>📋 Regras de Negócio</h2>
    <ul>
        <li><strong>Renda Mínima:</strong> Deve ser superior a R$ 2.000,00.</li>
        <li><strong>Limite de Parcela:</strong> O pagamento mensal não pode ultrapassar 30% da renda bruta do cliente.</li>
        <li><strong>Taxa de Juros:</strong> Juros simples de 2% ao mês aplicados à duração total do contrato.</li>
    </ul>

    <h2>🛠️ Desafios Técnicos e Soluções</h2>

    <h3>1. Escopo de Funções e Passagem de Dados</h3>
    <p>Inicialmente, as variáveis se perdiam entre as funções. Resolvi isso implementando comandos de retorno (<strong>return</strong>), permitindo que as funções passassem os dados validados de volta para o controlador principal.</p>
    
    

    <h3>2. Prevenção de Vazamento de Memória</h3>
    <p>Substituí chamadas de funções recursivas (uma função chamando ela mesma) por um laço <strong>while</strong> e condições de parada (<strong>break</strong>). Isso mantém o uso da memória estável, mesmo processando muitos clientes.</p>
    
    

    <h3>3. Suporte Multiplataforma</h3>
    <p>Adicionei uma verificação condicional para detectar o sistema operacional, garantindo que o comando de limpar o terminal funcione corretamente no Windows (cls) ou Unix/Mac (clear).</p>

    <h2>💻 Como Executar</h2>
    <ol>
        <li>Clone o repositório para sua máquina local.</li>
        <li>Abra seu terminal ou prompt de comando.</li>
        <li>Navegue até a pasta do projeto.</li>
        <li>Execute o comando: <code>python main.py</code></li>
    </ol>

    <hr>

</body>
</html>