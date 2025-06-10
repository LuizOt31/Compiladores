import os
import sys
import subprocess
import difflib

def run_test(input_file, expected_output_file, actual_output_dir, execution_input_dir):
    base_name = os.path.basename(input_file)
    name_without_ext = os.path.splitext(base_name)[0]
    
    generated_c_file = os.path.join(actual_output_dir, f"{name_without_ext}.c")
    executable_file = os.path.join(actual_output_dir, f"{name_without_ext}")

    try:
        compiler_result = subprocess.run(
            ['python3', 'main.py', input_file, generated_c_file],
            capture_output=True, text=True
        )
        if compiler_result.returncode != 0:
            print(f"❌ FALHA NO COMPILADOR: {base_name}")
            print(compiler_result.stderr)
            return False

        with open(generated_c_file, 'r', encoding='utf-8') as f:
            compiler_output = f.read().strip()

        with open(expected_output_file, 'r', encoding='utf-8') as f:
            expected_output = f.read().strip()
        
        if "Fim da compilacao" in expected_output:
            if compiler_output == expected_output:
                print(f"✅ PASSOU (Erro esperado): {base_name}")
                return True
            else:
                print(f"❌ FALHOU (Erro esperado): {base_name}")
                print_diff(expected_output, compiler_output)
                return False

        compile_result = subprocess.run(
            ['gcc', generated_c_file, '-o', executable_file, '-w'],
            capture_output=True, text=True
        )
        if compile_result.returncode != 0:
            print(f"❌ FALHA DE COMPILAÇÃO C: {base_name}")
            print(f"   Erro do GCC: {compile_result.stderr}")
            return False

        execution_input_path = os.path.join(execution_input_dir, base_name)
        execution_input_data = None
        if os.path.exists(execution_input_path):
            with open(execution_input_path, 'r', encoding='utf-8') as f:
                execution_input_data = f.read()

        program_result = subprocess.run(
            [executable_file],
            input=execution_input_data,
            capture_output=True, text=True,
            encoding='utf-8'
        )

        actual_execution_output = program_result.stdout.strip()

        if actual_execution_output == expected_output:
            print(f"✅ PASSOU: {base_name}")
            return True
        else:
            print(f"❌ FALHOU (Execução): {base_name}")
            print_diff(expected_output, actual_execution_output)
            return False

    except Exception as e:
        print(f"❌ ERRO INESPERADO NO TESTE: {base_name} - {e}")
        return False

def print_diff(expected, actual):
    diff = difflib.unified_diff(
        expected.splitlines(keepends=True),
        actual.splitlines(keepends=True),
        fromfile='esperado',
        tofile='obtido',
    )
    print("   Diferenças:")
    for line in diff:
        print(f"   {line.strip()}")

def run_all_tests(input_dir, expected_output_dir, actual_output_dir, execution_input_dir):
    input_files = []
    
    for file in os.listdir(input_dir):
        if file.endswith('.alg'):
            input_path = os.path.join(input_dir, file)
            expected_output_path = os.path.join(expected_output_dir, file)
            
            if os.path.exists(expected_output_path):
                input_files.append((input_path, expected_output_path))
            else:
                print(f"⚠️ AVISO: Arquivo de saída esperada '{expected_output_path}' não encontrado para a entrada '{file}'")
    
    os.makedirs(actual_output_dir, exist_ok=True)
    
    if not input_files:
        print("\nNenhum par de arquivos de teste (entrada/saída esperada) foi encontrado.")
        return

    success_count = 0
    total_count = len(input_files)
    
    for input_path, expected_output_path in sorted(input_files):
        print(f"\n📋 Testando: {os.path.basename(input_path)}")
        if run_test(input_path, expected_output_path, actual_output_dir, execution_input_dir):
            success_count += 1
    
    print(f"\n📊 Resumo dos testes:")
    print(f"   Total de casos encontrados: {total_count}")
    print(f"   Aprovados: {success_count}")
    print(f"   Reprovados: {total_count - success_count}")
    if total_count > 0:
        print(f"   Taxa de sucesso: {(success_count/total_count)*100:.2f}%")

if __name__ == "__main__":
    base_dir = "casos-de-teste"
    default_input_dir = os.path.join(base_dir, "entrada")
    default_expected_output_dir = os.path.join(base_dir, "saida_esperada")
    default_execution_input_dir = os.path.join(base_dir, "entrada-execucao")
    default_actual_output_dir = "saida_gerada"
    
    for path in [default_input_dir, default_expected_output_dir, default_execution_input_dir]:
        if not os.path.isdir(path):
            print(f"❌ ERRO: Diretório necessário '{path}' não encontrado.")
            sys.exit(1)
            
    print(f"🔍 Testando compilador (com compilação e execução) para a linguagem LA")
    print(f"   Diretório de entrada: {default_input_dir}")
    print(f"   Diretório de entrada (execução): {default_execution_input_dir}")
    print(f"   Diretório de saída esperada: {default_expected_output_dir}")
    print(f"   Diretório de saída gerada: {default_actual_output_dir}")
    
    run_all_tests(default_input_dir, default_expected_output_dir, default_actual_output_dir, default_execution_input_dir)