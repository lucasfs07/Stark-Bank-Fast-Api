import starkbank
from starkbank import Invoice, Project
import random
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv()

project_id = os.getenv("PROJECT_ID")
private_key_path = os.getenv("PRIVATE_KEY_PATH")

private_key_path = os.path.abspath(private_key_path)

with open(private_key_path, "r") as f:
    private_key = f.read()

user = Project(
    id=project_id,
    private_key=private_key,
    environment="sandbox"
)
starkbank.user = user


faker = Faker('pt_BR')

def gerar_cpf_valido():
    def digito(digs):
        s = sum([v * (len(digs) + 1 - i) for i, v in enumerate(digs)])
        r = (s * 10) % 11
        return r if r < 10 else 0

    base = [random.randint(0, 9) for _ in range(9)]
    d1 = digito(base)
    d2 = digito(base + [d1])
    return ''.join(map(str, base + [d1, d2]))
#emissao invoice randomica
def emitir_invoices():
    invoices = []
    quantidade = random.randint(8, 12)
    for _ in range(quantidade):
        nome = faker.name()
        cpf = gerar_cpf_valido()
        valor = random.randint(10000, 100000)
        invoice = Invoice(amount=valor, name=nome, tax_id=cpf)
        invoices.append(invoice)

    criadas = starkbank.invoice.create(invoices, user=user)
    for i in criadas:
        print(f"- {i.name} | {i.tax_id} | R${i.amount/100:.2f}")
    return criadas