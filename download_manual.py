#!/usr/bin/env python3
"""
Script para download do Manual NTSL da Profit Pro
"""

import urllib.request
import ssl
import sys

def download_manual():
    url = "https://downloadserver-cdn.nelogica.com.br/content/profit/manual_ntsl/ManualNTSL.pdf"
    output_file = "docs/ManualNTSL.pdf"

    print(f"Baixando manual NTSL de: {url}")
    print(f"Salvando em: {output_file}")

    # Criar contexto SSL que não verifica certificados (para contornar problemas de SSL)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Headers para simular um navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0'
    }

    try:
        # Criar requisição com headers customizados
        req = urllib.request.Request(url, headers=headers)

        # Fazer download
        with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
            # Verificar se a resposta é válida
            if response.status != 200:
                print(f"Erro: Status HTTP {response.status}")
                return False

            # Ler o conteúdo
            content = response.read()

            # Verificar se tem conteúdo
            if len(content) == 0:
                print("Erro: Arquivo vazio baixado")
                return False

            # Salvar arquivo
            with open(output_file, 'wb') as f:
                f.write(content)

            file_size = len(content) / 1024  # KB
            print(f"✓ Download concluído com sucesso!")
            print(f"✓ Tamanho do arquivo: {file_size:.2f} KB")
            return True

    except urllib.error.HTTPError as e:
        print(f"✗ Erro HTTP {e.code}: {e.reason}")
        return False
    except urllib.error.URLError as e:
        print(f"✗ Erro de URL: {e.reason}")
        return False
    except Exception as e:
        print(f"✗ Erro inesperado: {str(e)}")
        return False

if __name__ == "__main__":
    success = download_manual()
    sys.exit(0 if success else 1)
