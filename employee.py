import logging

from rapidfuzz import process, fuzz

employee_names = [
"ELISABETE",
"AARON MALVERN DANN",
"ALECSANDRA TEIXEIRA CUNHA",
"ANA ALICE BONIFACIO LEITE",
"ANA GABRIELA DE MELLO LAUER",
"ANA MARIA CASTELO BRANCO F. GUIMARÃES",
"ANA PAULA REZENDE GONCALVES",
"ARTHUR BARRAGAN VASCONCELOS",
"AILTON TORRES DE SOUZA",
"ANGELA MARGARIDA MONTEIRO DIAS BRANCO",
"BRUNO ESTEVES VIGNE",
"CARSTEN WEGENER",
"DENISE MARIA AFONSO GOMES DA SILVA",
"DIOGO GUIMARAES MULDER",
"ELAINE FERRARI ANTUNES",
"ELIANE PIMENTEL RIBEIRO",
"ELVIRA REALEIRO",
"FERNANDO CANAZIO AMORIM",
"GIOVANA BRANCO CARNEIRO",
"GRACIETE OLIVEIRA DE MOURA",
"GUILHERME DE MELLO GONÇALVES",
"IDA FATIMA GARRITANO M GUIMARÃES",
"JORGELINA ELECTRA FLORES",
"JULIANA MANCZENKO CHAGAS",
"JUDITH PATRICIA BRANDT",
"KELVIN DANIEL",
"LUCIANE ALVES FERNANDEZ",
"LUIZA ANTONIA DE CAMPOS FIGUEIREDO",
"MARCIA P DOS SANTOS",
"MARCIO DE BRITTO PEREIRA TENIUS",
"MERCEDES ISABEL PAGOLA",
"MONICA ESTHER BACA COAQUIRA",
"NADJA DIAS GONÇALVES DE FRANÇA",
"NATALI ORNELLA CAMPILONGO",
"RAFAEL GOMEZ",
"RITA MARIA CARDOSO BAIAO MARAO",
"ROBERT DOUGLAS DE SÁ QUEEN",
"ROSIANE TAVARES GONCALVES",
"TATIANA ALVES RANGEL",
"TATIANA CORREIA DOS SANTOS",
"VERA REGINA DE OLIVEIRA SERRA",
"WAGNER RIBEIRO ANGELO"
]



logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S")


    # Função para identificar se um nome da planilha está presente no texto extraído
def identify_employee_name(text, employee_list):
    """
    Identifica o nome de um funcionário no texto extraído.
    """
    logging.info("Texto recebido para identificação: '%s'", text)
    text_lower = text.lower()
    for name in employee_list:
        if name.lower() in text_lower:
            logging.debug("Nome encontrado: '%s'", name)
            return name
    return "Desconhecido"

