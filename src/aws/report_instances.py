import boto3
import json
from region_mapper import get_region_name


def list_instances(region_code="us-east-1"):
    """
    Lista os tipos de instância EC2 em uma região.
    """
    ec2 = boto3.client("ec2", region_name=region_code)
    response = ec2.describe_instance_types()
    
    instances = []
    for itype in response["InstanceTypes"]:
        instances.append({
            "InstanceType": itype["InstanceType"],
            "vCPU": itype["VCpuInfo"]["DefaultVCpus"],
            "Memory (GiB)": itype["MemoryInfo"]["SizeInMiB"] / 1024
        })
    return instances


def get_prices(instance_type, region_code="us-east-1"):
    """
    Busca preço sob demanda para um tipo de instância.
    """
    pricing = boto3.client("pricing", region_name="us-east-1")
    region_name = get_region_name(region_code)

    response = pricing.get_products(
        ServiceCode="AmazonEC2",
        Filters=[
            {"Type": "TERM_MATCH", "Field": "instanceType", "Value": instance_type},
            {"Type": "TERM_MATCH", "Field": "location", "Value": region_name},
            {"Type": "TERM_MATCH", "Field": "operatingSystem", "Value": "Linux"},
            {"Type": "TERM_MATCH", "Field": "tenancy", "Value": "Shared"},
            {"Type": "TERM_MATCH", "Field": "preInstalledSw", "Value": "NA"},
        ],
        MaxResults=1,
    )

    if not response["PriceList"]:
        return None

    price_item = json.loads(response["PriceList"][0])
    terms = price_item["terms"]["OnDemand"]
    for _, term in terms.items():
        for _, price_dim in term["priceDimensions"].items():
            return float(price_dim["pricePerUnit"]["USD"])
    return None


def generate_report(region_code="us-east-1", limit=5):
    """
    Gera relatório unindo instâncias + specs + preço.
    """
    instances = list_instances(region_code)[:limit]
    report = []

    for inst in instances:
        price = get_prices(inst["InstanceType"], region_code)
        report.append({
            "InstanceType": inst["InstanceType"],
            "vCPU": inst["vCPU"],
            "Memory (GiB)": inst["Memory (GiB)"],
            "PricePerHourUSD": price
        })
    
    return report


if __name__ == "__main__":
    report = generate_report("us-east-1", limit=5)
    print("📊 Relatório de instâncias EC2 (us-east-1):\n")
    for r in report:
        print(r)
