#!/usr/bin/env python3
"""
Script alternativo para download do Manual NTSL usando requests
"""

import sys
import os

def download_with_requests():
    """Tenta download usando biblioteca requests"""
    try:
        import requests
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
    except ImportError:
        print("✗ Biblioteca 'requests' não está instalada")
        print("  Instale com: pip install requests")
        return False

    url = "https://downloadserver-cdn.nelogica.com.br/content/profit/manual_ntsl/ManualNTSL.pdf"
    output_file = "docs/ManualNTSL.pdf"

    print(f"Tentando download de: {url}")

    # Configurar sessão com retry
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # Headers completos
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/pdf,application/octet-stream,*/*',
        'Accept-Language': 'pt-BR,pt;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.nelogica.com.br/',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
    }

    try:
        # Tentar com verify=False para ignorar SSL
        response = session.get(
            url,
            headers=headers,
            timeout=30,
            verify=False,
            allow_redirects=True,
            stream=True
        )

        if response.status_code == 200:
            # Salvar arquivo
            with open(output_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            file_size = os.path.getsize(output_file) / 1024
            print(f"✓ Download concluído!")
            print(f"✓ Arquivo: {output_file}")
            print(f"✓ Tamanho: {file_size:.2f} KB")
            return True
        else:
            print(f"✗ Erro HTTP: {response.status_code}")
            return False

    except Exception as e:
        print(f"✗ Erro: {str(e)}")
        return False

def download_with_urllib():
    """Fallback usando urllib"""
    import urllib.request
    import ssl

    url = "https://downloadserver-cdn.nelogica.com.br/content/profit/manual_ntsl/ManualNTSL.pdf"
    output_file = "docs/ManualNTSL.pdf"

    print(f"\nTentando com urllib...")

    ctx = ssl._create_unverified_context()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
            content = response.read()
            with open(output_file, 'wb') as f:
                f.write(content)

            file_size = len(content) / 1024
            print(f"✓ Download concluído: {file_size:.2f} KB")
            return True
    except Exception as e:
        print(f"✗ Erro: {str(e)}")
        return False

if __name__ == "__main__":
    print("=== Download Manual NTSL ===\n")

    # Tentar primeiro com requests
    success = download_with_requests()

    # Se falhar, tentar com urllib
    if not success:
        success = download_with_urllib()

    if not success:
        print("\n" + "="*50)
        print("❌ Não foi possível fazer o download automaticamente")
        print("="*50)
        print("\nPor favor, baixe manualmente de:")
        print("https://downloadserver-cdn.nelogica.com.br/content/profit/manual_ntsl/ManualNTSL.pdf")
        print("\nE salve em: docs/ManualNTSL.pdf")

    sys.exit(0 if success else 1)
