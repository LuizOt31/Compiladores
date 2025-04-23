import os
import subprocess
import sys
import re

def normalizar_formato(texto):
    """Normaliza o formato do texto para facilitar a comparação."""
    # Remove espaços em branco e caracteres de formatação
    texto = texto.strip()
    
    # Normaliza o formato dos tokens
    # De: "<'token', TYPE>" para "<token, TYPE>"
    # Ou de: "'<token', TYPE>" para "<token, TYPE>"
    texto = re.sub(r"['\s]*<['\s]*([^,>]+)['\s]*,\s*([^>]+)['\s]*>", r"<\1,\2>", texto)
    
    # Remove linhas vazias
    linhas = [linha.strip() for linha in texto.split('\n') if linha.strip()]
    
    return '\n'.join(linhas)

def run_test(entrada_file, saida_esperada_file):
    # Caminho para o arquivo de saída temporário
    saida_temp = "saida.txt"
    
    # Executar o programa main.py com o arquivo de entrada
    cmd = ['python3', 'main.py', entrada_file, saida_temp]
    subprocess.run(cmd)
    
    # Verificar se o arquivo de saída foi gerado
    if not os.path.exists(saida_temp):
        print(f"Falha: Arquivo de saída não foi gerado para {entrada_file}")
        return False
    
    # Ler o conteúdo dos arquivos
    with open(saida_temp, 'r', encoding='utf-8') as f:
        saida_conteudo = f.read().strip()
    
    with open(saida_esperada_file, 'r', encoding='utf-8') as f:
        esperado_conteudo = f.read().strip()
    
    # Normalizar os formatos para comparação
    saida_normalizada = normalizar_formato(saida_conteudo)
    esperado_normalizado = normalizar_formato(esperado_conteudo)
    
    # Comparar os conteúdos normalizados
    if saida_normalizada == esperado_normalizado:
        print(f"✅ Passou: {os.path.basename(entrada_file)}")
        return True
    else:
        print(f"❌ Falhou: {os.path.basename(entrada_file)}")
        return False

def main():
    # Diretórios dos arquivos de teste
    entrada_dir = "./testes/entrada"
    saida_esperada_dir = "./testes/saida_esperada"
    
    # Verificar se os diretórios existem
    if not os.path.exists(entrada_dir):
        print(f"Diretório de entrada não encontrado: {entrada_dir}")
        return
    
    if not os.path.exists(saida_esperada_dir):
        print(f"Diretório de saída esperada não encontrado: {saida_esperada_dir}")
        return
    
    # Listar todos os arquivos de entrada
    entrada_files = sorted(os.listdir(entrada_dir))
    
    total_testes = 0
    testes_passaram = 0
    
    # Mudar para o diretório T1 para executar os testes
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    for entrada_file in entrada_files:
        entrada_path = os.path.join(entrada_dir, entrada_file)
        saida_esperada_path = os.path.join(saida_esperada_dir, entrada_file)
        
        # Verificar se existe um arquivo de saída esperada correspondente
        if os.path.exists(saida_esperada_path):
            total_testes += 1
            if run_test(entrada_path, saida_esperada_path):
                testes_passaram += 1
        else:
            print(f"⚠️ Aviso: Não há arquivo de saída esperada para {entrada_file}")
    
    # Exibir resultado final
    if total_testes > 0:
        print(f"\nResultado: {testes_passaram}/{total_testes} testes passaram ({testes_passaram/total_testes*100:.2f}% de sucesso)")
    else:
        print("\nNenhum teste foi executado.")

if __name__ == "__main__":
    main() 