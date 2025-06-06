import json

def lambda_handler(event, context):
    try:
        body = event.get("body")
        if body is None:
            return {
                "statusCode": 400,
                "body": json.dumps({ "erro": "Corpo da requisição ausente." })
            }

        data = json.loads(body)

        operacao = data.get("operacao")
        a = float(data.get("a", 0))
        b = float(data.get("b", 0))

        if operacao not in ["soma", "subtracao", "multiplicacao", "divisao"]:
            return {
                "statusCode": 400,
                "body": json.dumps({ "erro": "Operação inválida." })
            }

        if operacao == "soma":
            resultado = a + b
        elif operacao == "subtracao":
            resultado = a - b
        elif operacao == "multiplicacao":
            resultado = a * b
        elif operacao == "divisao":
            if b == 0:
                return {
                    "statusCode": 400,
                    "body": json.dumps({ "erro": "Divisão por zero não permitida." })
                }
            resultado = a / b

        return {
            "statusCode": 200,
            "body": json.dumps({ "resultado": resultado })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({ "erro": f"Erro ao processar: {str(e)}" })
        }