import os
import sys
import subprocess
import difflib
from pathlib import Path

def run_test(input_file, expected_output_file, actual_output_file):
    """Executa o analisador sintático no arquivo de entrada e compara o resultado com a saída esperada."""
    # Executa o analisador
    try:
        subprocess.run(['python3', 'main.py', input_file, actual_output_file], check=True)
        
        # Lê o conteúdo do arquivo de saída
        with open(actual_output_file, 'r', encoding='utf-8') as f:
            actual_output = f.read().strip()
            
        # Lê o conteúdo do arquivo de saída esperada
        with open(expected_output_file, 'r', encoding='utf-8') as f:
            expected_output = f.read().strip()
            
        # Compara os resultados
        if actual_output == expected_output:
            print(f"✅ PASSOU: {os.path.basename(input_file)}")
            print(f"   Saída: {actual_output}")
            return True
        else:
            print(f"❌ FALHOU: {os.path.basename(input_file)}")
            print(f"   Esperado: {expected_output}")
            print(f"   Obtido: {actual_output}")
            
            # Mostra as diferenças
            diff = difflib.unified_diff(
                expected_output.splitlines(),
                actual_output.splitlines(),
                fromfile='esperado',
                tofile='obtido',
                n=0
            )
            diff_text = '\n'.join(diff)
            if diff_text:
                print(f"   Diferenças: \n{diff_text}")
                
            return False
    except subprocess.CalledProcessError:
        print(f"❌ ERRO AO EXECUTAR: {os.path.basename(input_file)}")
        return False

def run_all_tests(input_dir, expected_output_dir, actual_output_dir):
    """Executa todos os testes comparando a saída com os resultados esperados."""
    input_files = []
    
    # Encontra todos os arquivos .txt no diretório de entrada
    for file in os.listdir(input_dir):
        if file.endswith('.txt'):
            input_path = os.path.join(input_dir, file)
            expected_output_path = os.path.join(expected_output_dir, file)
            
            # Verifica se o arquivo de saída esperada existe
            if os.path.exists(expected_output_path):
                input_files.append((input_path, expected_output_path, file))
            else:
                print(f"⚠️ AVISO: Arquivo de saída esperada não encontrado para {file}")
    
    # Cria o diretório de saída se não existir
    os.makedirs(actual_output_dir, exist_ok=True)
    
    success_count = 0
    total_count = len(input_files)
    
    # Executa cada teste
    for input_path, expected_output_path, filename in sorted(input_files):
        actual_output_path = os.path.join(actual_output_dir, f"saida_{filename}")
        
        print(f"\n📋 Teste {os.path.basename(input_path)}:")
        if run_test(input_path, expected_output_path, actual_output_path):
            success_count += 1
    
    # Exibe estatísticas
    print(f"\n📊 Resumo dos testes:")
    print(f"   Total: {total_count}")
    print(f"   Aprovados: {success_count}")
    print(f"   Reprovados: {total_count - success_count}")
    print(f"   Taxa de sucesso: {(success_count/total_count)*100:.2f}%")

if __name__ == "__main__":
    # Valores padrão
    default_input_dir = os.path.join("casos-de-teste", "entrada")
    default_expected_output_dir = os.path.join("casos-de-teste", "saida_esperada") 
    default_actual_output_dir = "saida_gerada"
    
    if len(sys.argv) == 4:
        # Usa os diretórios fornecidos pelo usuário
        input_dir = sys.argv[1]
        expected_output_dir = sys.argv[2]
        actual_output_dir = sys.argv[3]
    elif len(sys.argv) == 1:
        # Usa os diretórios padrão
        input_dir = default_input_dir
        expected_output_dir = default_expected_output_dir
        actual_output_dir = default_actual_output_dir
        
        # Verifica se os diretórios existem
        if not os.path.isdir(input_dir):
            print(f"⚠️ ERRO: Diretório de entrada '{input_dir}' não encontrado.")
            sys.exit(1)
            
        if not os.path.isdir(expected_output_dir):
            print(f"⚠️ ERRO: Diretório de saída esperada '{expected_output_dir}' não encontrado.")
            sys.exit(1)
    else:
        print("Uso: python3 test.py [dir_entrada] [dir_saida_esperada] [dir_saida_gerada]")
        sys.exit(1)
    
    print(f"🔍 Testando analisador sintático para a linguagem LA")
    print(f"   Diretório de entrada: {input_dir}")
    print(f"   Diretório de saída esperada: {expected_output_dir}")
    print(f"   Diretório de saída gerada: {actual_output_dir}")
    
    run_all_tests(input_dir, expected_output_dir, actual_output_dir) 