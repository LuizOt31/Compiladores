# Testador Automático para ColorArt
# Projeto de Compiladores - Sistema de Desenho Geométrico

import os
import sys
import subprocess
import glob

def executar_teste(arquivo_entrada, arquivo_saida):
    """Executa o compilador ColorArt para um teste específico"""
    try:
        resultado = subprocess.run(
            ["python3", "colorart.py", arquivo_entrada, arquivo_saida],
            capture_output=True,
            text=True,
            timeout=30
        )
        return resultado.returncode == 0, resultado.stdout, resultado.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout na execução"
    except Exception as e:
        return False, "", str(e)

def comparar_arquivos(arquivo1, arquivo2):
    """Compara dois arquivos SVG"""
    try:
        with open(arquivo1, 'r', encoding='utf-8') as f1:
            conteudo1 = f1.read().strip()
        with open(arquivo2, 'r', encoding='utf-8') as f2:
            conteudo2 = f2.read().strip()
        return conteudo1 == conteudo2
    except Exception:
        return False

def main():
    print("=" * 60)
    print("TESTADOR AUTOMÁTICO - COLORART")
    print("=" * 60)
    
    # Verificar se as pastas existem
    if not os.path.exists("casos-de-teste/entradas"):
        print("ERRO: Pasta 'casos-de-teste/entradas' não encontrada!")
        return
    
    if not os.path.exists("casos-de-teste/saidas-esperadas"):
        print("ERRO: Pasta 'casos-de-teste/saidas-esperadas' não encontrada!")
        return
    
    # Criar pasta de saídas se não existir
    os.makedirs("casos-de-teste/saidas", exist_ok=True)
    
    # Buscar todos os arquivos de teste
    arquivos_entrada = glob.glob("casos-de-teste/entradas/teste*.ca")
    arquivos_entrada.sort()
    
    if not arquivos_entrada:
        print("AVISO: Nenhum arquivo de teste encontrado em 'casos-de-teste/entradas/'")
        return
    
    total_testes = len(arquivos_entrada)
    testes_passou = 0
    
    print(f"Encontrados {total_testes} teste(s)\n")
    
    for arquivo_entrada in arquivos_entrada:
        nome_base = os.path.basename(arquivo_entrada).replace("teste", "").replace(".ca", "")
        arquivo_saida = f"casos-de-teste/saidas/saida{nome_base}.svg"
        arquivo_esperado = f"casos-de-teste/saidas-esperadas/saida{nome_base}.svg"
        
        print(f"Teste {nome_base}:", end=" ")
        
        # Executar o compilador
        sucesso, stdout, stderr = executar_teste(arquivo_entrada, arquivo_saida)
        
        if not sucesso:
            print("FALHOU (Erro de compilação)")
            if stderr:
                print(f"  Erro: {stderr}")
            continue
        
        # Verificar se arquivo de saída foi criado
        if not os.path.exists(arquivo_saida):
            print("FALHOU (Arquivo de saída não criado)")
            continue
        
        # Verificar se existe arquivo esperado
        if not os.path.exists(arquivo_esperado):
            print("PASSOU (Sem arquivo de referência)")
            testes_passou += 1
            continue
        
        # Comparar com saída esperada
        if comparar_arquivos(arquivo_saida, arquivo_esperado):
            print("PASSOU")
            testes_passou += 1
        else:
            print("FALHOU (Saída diferente da esperada)")
            print(f"  Saída gerada: {arquivo_saida}")
            print(f"  Saída esperada: {arquivo_esperado}")
    
    print("\n" + "=" * 60)
    print(f"RESULTADO: {testes_passou}/{total_testes} testes passaram")
    
    if testes_passou == total_testes:
        print("✅ Todos os testes passaram!")
    else:
        print("❌ Alguns testes falharam.")
    
    print("=" * 60)

if __name__ == "__main__":
    main() 