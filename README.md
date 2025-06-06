# 🧮 Lambda Calculadora - Operações Aritméticas Básicas

## 📌 Descrição

Esta função Lambda na AWS executa operações matemáticas básicas com dois números reais: soma, subtração, multiplicação e divisão.

---

## 🧪 Exemplo de Requisição

**Método:** `POST`  
**URL:** `[URL do API Gateway]`  
**Cabeçalhos:**  
`Content-Type: application/json`

**Corpo da Requisição (JSON):**
```json
{
  "operacao": "multiplicacao",
  "a": 5,
  "b": 3
}
