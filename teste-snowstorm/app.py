import requests

# URL para a requisição GET
url = "https://browser.ihtsdotools.org/fhir/ValueSet/$expand?url=http://snomed.info/sct?fhir_vs&count=10&filter=myocardial"

# Realiza a requisição GET
response = requests.post(url)
print(response)
# Verifica se a requisição foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Imprime o conteúdo da resposta
    print(response.text)
else:
    print(f"A requisição falhou com código de status {response.status_code}")
