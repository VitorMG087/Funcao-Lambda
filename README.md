# 🧮 Lambda Calculadora - Operações Aritméticas Básicas

## 📌 Descrição

Esta função Lambda na AWS executa operações matemáticas básicas com dois números reais: soma, subtração, multiplicação e divisão.

---

## Dependências
Nenhuma dependência foi utilizada

## Validações
A operação deve ser uma das seguintes:<br><br>

"soma"<br>
"subtracao"<br>
"multiplicacao"<br>
"divisao"<br><br>

b não pode ser 0 em caso de divisão.<br>
Se a operação for inválida, será retornado erro 400.<br>


## 🧪 Exemplo de Requisição, Como testar

Use a URL:<br>
https://adw3cue6gok55olmzgut4lf7tu0yiehf.lambda-url.us-east-2.on.aws/
<br>

**Método:** `POST`  
Aba Body:<br>
Selecione a opção raw<br>
Escolha o tipo JSON (ícone à direita)<br>
Cole e edite o seguinte JSON conforme necessário:<br>

**Corpo da Requisição (JSON):**
```json
{
  "operacao": "multiplicacao",
  "a": 5,
  "b": 3
}

