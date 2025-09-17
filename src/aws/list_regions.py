import boto3
from rich import print

def listar_regioes():
    ec2 = boto3.client("ec2")
    response = ec2.describe_regions(AllRegions=True)
    regioes = [regiao["RegionName"] for regiao in response["Regions"]]
    return regioes

if __name__ == "__main__":
    print("[bold green]🌍 Regiões disponíveis na AWS:[/bold green]")
    for r in listar_regioes():
        print(f"- {r}")
