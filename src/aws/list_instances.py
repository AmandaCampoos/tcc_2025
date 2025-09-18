import boto3
from rich import print

def listar_instancias(region="us-east-1"):
    ec2 = boto3.client("ec2", region_name=region)
    response = ec2.describe_instance_types()
    
    instancias = []
    for tipo in response["InstanceTypes"]:
        info = {
            "Tipo": tipo["InstanceType"],
            "vCPUs": tipo["VCpuInfo"]["DefaultVCpus"],
            "Memória (GiB)": tipo["MemoryInfo"]["SizeInMiB"] // 1024,
            "Armazenamento": tipo.get("InstanceStorageInfo", {}).get("TotalSizeInGB", "EBS only"),
            "Rede": tipo["NetworkInfo"]["NetworkPerformance"],
        }
        instancias.append(info)
    return instancias


if __name__ == "__main__":
    print("[bold cyan]💻 Tipos de instância disponíveis na região us-east-1:[/bold cyan]")
    for inst in listar_instancias("us-east-1"):
        print(f"- {inst['Tipo']} | {inst['vCPUs']} vCPUs | {inst['Memória (GiB)']} GiB RAM | "
              f"Armazenamento: {inst['Armazenamento']} | Rede: {inst['Rede']}")
