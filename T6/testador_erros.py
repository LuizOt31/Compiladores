# Testador de Erros para ColorArt
# Projeto de Compiladores - Validação de Detecção de Erros

import os
import sys
import subprocess
import glob

def executar_teste_erro(arquivo_entrada, arquivo_saida):
    """Executa o compilador ColorArt esperando que haja erro"""
    try:
        resultado = subprocess.run(
            ["python3", "colorart.py", arquivo_entrada, arquivo_saida],
            capture_output=True,
            text=True,
            timeout=30
        )
        # Para testes de erro, esperamos que NÃO seja bem-sucedido
        return resultado.returncode != 0 or "erro" in resultado.stdout.lower(), resultado.stdout, resultado.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout na execução"
    except Exception as e:
        return False, "", str(e)

def verificar_tipo_erro(arquivo_saida, tipo_esperado):
    """Verifica se o tipo de erro esperado foi detectado"""
    try:
        with open(arquivo_saida, 'r', encoding='utf-8') as f:
            conteudo = f.read().lower()
        
        if tipo_esperado == "lexico" and ("léxico" in conteudo or "token recognition error" in conteudo):
            return True
        elif tipo_esperado == "sintatico" and ("sintático" in conteudo or "mismatched input" in conteudo):
            return True
        elif tipo_esperado == "semantico" and "semântico" in conteudo:
            return True
        
        return False
    except Exception:
        return False

def main():
    print("=" * 60)
    print("TESTADOR DE ERROS - COLORART")
    print("=" * 60)
    
    # Lista de testes de erro esperados
    testes_erro = [
        ("teste_erro_lexico.ca", "lexico", "Erro léxico - caractere inválido"),
        ("teste_erro_sintatico.ca", "sintatico", "Erro sintático - sintaxe incorreta"),
        ("teste_erro_semantico.ca", "semantico", "Erro semântico - cores não declaradas"),
        ("teste_erro_variavel.ca", "semantico", "Erro semântico - variável duplicada"),
        ("teste_erro_complexo.ca", "semantico", "Erro semântico - múltiplos erros")
    ]
    
    os.makedirs("casos-de-teste/saidas-geradas", exist_ok=True)
    
    total_testes = len(testes_erro)
    testes_passou = 0
    
    print(f"Executando {total_testes} teste(s) de erro\n")
    
    for arquivo_teste, tipo_erro, descricao in testes_erro:
        arquivo_entrada = f"casos-de-teste/entradas/{arquivo_teste}"
        arquivo_saida = f"casos-de-teste/saidas-geradas/erro_{tipo_erro}.svg"
        
        print(f"Teste {arquivo_teste}: {descricao}")
        print(f"  Esperado: {tipo_erro.upper()}", end=" -> ")
        
        # Verificar se arquivo de entrada existe
        if not os.path.exists(arquivo_entrada):
            print("FALHOU (Arquivo de entrada não existe)")
            continue
        
        # Executar o compilador
        erro_detectado, stdout, stderr = executar_teste_erro(arquivo_entrada, arquivo_saida)
        
        if not erro_detectado:
            print("FALHOU (Nenhum erro detectado)")
            continue
        
        # Verificar se o tipo de erro correto foi detectado
        if verificar_tipo_erro(arquivo_saida, tipo_erro):
            print("PASSOU ✅")
            testes_passou += 1
        else:
            print("FALHOU (Tipo de erro incorreto)")
            if os.path.exists(arquivo_saida):
                with open(arquivo_saida, 'r', encoding='utf-8') as f:
                    print(f"    Erro encontrado: {f.read().strip()[:100]}...")
    
    print("\n" + "=" * 60)
    print(f"RESULTADO: {testes_passou}/{total_testes} testes de erro passaram")
    
    if testes_passou == total_testes:
        print("✅ Todos os testes de erro passaram!")
        print("   O compilador está detectando corretamente os erros!")
    else:
        print("❌ Alguns testes de erro falharam.")
        print("   Verificar a detecção de erros no compilador.")
    
    print("=" * 60)

if __name__ == "__main__":
    main() 