import requests

def fetch_and_save(blob_url: str, filename: str):
    resp = requests.get(blob_url)
    resp.raise_for_status()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(resp.text.strip())
    print(resp.text.strip())

if __name__ == "__main__":
    blob_url = "https://kcscctfblob.blob.core.windows.net/secret/invoicecompany.txt"
    fetch_and_save(blob_url, "mycompany.txt")
