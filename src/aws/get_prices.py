import boto3
import json
from rich import print
from region_mapper import get_region_name  # <<--- importar mapeador

def get_instance_price(instance_type="t2.micro", region_code="us-east-1"):
    pricing = boto3.client("pricing", region_name="us-east-1")

    region_name = get_region_name(region_code)  # converte código -> nome Pricing API

    response = pricing.get_products(
        ServiceCode="AmazonEC2",
        Filters=[
            {"Type": "TERM_MATCH", "Field": "instanceType", "Value": instance_type},
            {"Type": "TERM_MATCH", "Field": "location", "Value": region_name},
            {"Type": "TERM_MATCH", "Field": "operatingSystem", "Value": "Linux"},
            {"Type": "TERM_MATCH", "Field": "tenancy", "Value": "Shared"},
            {"Type": "TERM_MATCH", "Field": "preInstalledSw", "Value": "NA"},
            {"Type": "TERM_MATCH", "Field": "capacitystatus", "Value": "Used"},
        ],
        MaxResults=1,
    )

    if not response["PriceList"]:
        return None

    price_item = json.loads(response["PriceList"][0])
    on_demand = list(price_item["terms"]["OnDemand"].values())[0]
    price_dimensions = list(on_demand["priceDimensions"].values())[0]
    price_per_hour = float(price_dimensions["pricePerUnit"]["USD"])

    return price_per_hour


if __name__ == "__main__":
    instancias_teste = ["t2.micro", "t3.medium", "m5.large"]
    regiao_teste = "us-east-1"  # agora usamos código
    regiao_nome = get_region_name(regiao_teste)

    print(f"[bold green]💰 Preços On-Demand na região {regiao_nome} ({regiao_teste}):[/bold green]\n")
    for inst in instancias_teste:
        preco = get_instance_price(inst, regiao_teste)
        if preco:
            print(f"- {inst}: [yellow]${preco:.4f}[/yellow] por hora")
        else:
            print(f"- {inst}: [red]Preço não encontrado[/red]")
