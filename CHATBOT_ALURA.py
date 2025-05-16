import google.generativeai as genai
import os

# Carrega a API Key da variável de ambiente
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Configura a API Key
genai.configure(api_key=GOOGLE_API_KEY)

# Inicializa o modelo (vamos continuar com 'models/gemma-3-27b-it' por enquanto)
model = genai.GenerativeModel('models/gemma-3-27b-it')

def gerar_sugestoes_de_atividades(serie, disciplina, tema, metodologia):
    prompt = f"""Você é um assistente pedagógico especializado em ensino fundamental 1. Você usará, como base nas suas respostas, o documento chamado Base Nacional Comum Curricular.
    Gere uma lista de 3 sugestões de atividades criativas e relevantes para uma aula de {disciplina} do {serie} ano com o tema: {tema} Não esqueça de levar em consideração a metodologia {metodologia}.
    As sugestões devem ser concisas e fáceis de implementar em sala de aula.

    Formato da resposta:
    - Atividade 1: [Descrição da atividade]
    - Atividade 2: [Descrição da atividade]
    - Atividade 3: [Descrição da atividade]
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Ocorreu um erro ao gerar as sugestões: {e}"

# Interface de texto simples
print("\n")
print("Bem-vindo ao professor crIAtivo!")
print("\n")
serie_professor = input("Digite a série/ano da turma: ")
disciplina_professor = input("Digite a disciplina: ")
tema_professor = input("Digite o tema da aula: ")
metodologia_professor = input ("Digite a metodologia de ensino desejável:")
print("\n")

sugestoes = gerar_sugestoes_de_atividades(serie_professor, disciplina_professor, tema_professor, metodologia_professor)

print("\nSugestões de atividades:")
print(sugestoes)

# ... (depois de imprimir as sugestões) ...
print("\n")
salvar = input("DESEJA SALVAR ESSAS SUGESTÕES EM UM ARQUIVO DE TEXTO? (s/n): ")
if salvar.lower() == 's':
    try:
        with open(f"sugestoes_{disciplina_professor}_{tema_professor}.txt", "w", encoding="utf-8") as f:
            f.write(f"Sugestões para {disciplina_professor} - {serie_professor}º ano\n")
            f.write(f"Tema: {tema_professor}\n")
            f.write(f"Metodologia: {metodologia_professor}\n\n")
            f.write(sugestoes)
        print(f"Sugestões salvas em 'sugestoes_{disciplina_professor}_{tema_professor}.txt'")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

