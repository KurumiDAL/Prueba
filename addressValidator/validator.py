from typing import TextIO

from addressValidator.mealy import Path, State

q0 = State("q0")
q1 = State("q1")
q2 = State("q2")
q3 = State("q3")
q4 = State("q4")
q5 = State("q5")
q6 = State("q6")
q7 = State("q7")
q8 = State("q8")
q9 = State("q9")
q10 = State("q10")
q11 = State("q11")
q12 = State("q12")
q13 = State("q13")
q14 = State("q14")
q15 = State("q15")
q16 = State("q16")
q17 = State("q17")
q18 = State("q18")
q19 = State("q19")
q20 = State("q20")
q21 = State("q21")
q22 = State("q22")
q23 = State("q23")
q24 = State("q24")
q25 = State("q25")
q26 = State("q26")
q27 = State("q27")
q28 = State("q28")
q29 = State("q29")
q30 = State("q30")
q31 = State("q31")
q32 = State("q32")
q33 = State("q33")
q34 = State("q34")
q35 = State("q35")



def address_validator(word: str) -> bool:

    q0.set_paths([Path("tv", q1, "0",r'\b(Autopista|Avenida|Avenida Calle|Avenida Carrera|Bulevar|Calle|Carrera|Carretera|Circular|Circunvalar|Diagonal|Cuentas Corridas|Pasaje|Paseo|Peatonal|Transversal|Variante|Via|Troncal)\b'), Path("br2", q19, "0",r'\b(Barrio|Ciudadela|Supermanzana)\b'),Path("vda", q27, "0",r'\bVereda\b'),Path("km", q31, "0",r'\bKilometro\b')])
    #Urbana
    q1.set_paths([Path("nv", q2, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q2.set_paths([Path("bis", q3, "0",r'^(BIS|Bis)$'),Path("c", q5, "0",r'^(NORTE|Norte|SUR|Sur|ESTE|Este|OESTE|Oeste)$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q3.set_paths([Path("lp", q4, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$'),Path("c", q5, "0",r'^(NORTE|Norte|SUR|Sur|ESTE|Este|OESTE|Oeste)$')])
    q4.set_paths([Path("c", q5, "0",r'^(NORTE|Norte|SUR|Sur|ESTE|Este|OESTE|Oeste)$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q5.set_paths([Path("nv", q6, "0",r'^[1-9][0-9]{0,2}(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$')])
    q6.set_paths([Path("bis", q7, "0",r'^(BIS|Bis)$'),Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q7.set_paths([Path("lp", q8, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1})|)$'),Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q8.set_paths([Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q9.set_paths([Path("c", q10, "1",r'^(NORTE|Norte|SUR|Sur|ESTE|Este|OESTE|Oeste)$'),Path("br", q11, "0",r'^(Barrio|Ciudadela|Supermanzana)$'),Path("u", q13, "0",r'^(Bloque|Celula|Etapa|Urbanizacion|Sector|Torre|Zona)$'),Path("ma", q15, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q10.set_paths([Path("br", q11, "0",r'^(Barrio|Ciudadela|Supermanzana)$'),Path("u", q13, "0",r'^(Bloque|Celula|Etapa|Urbanizacion|Sector|Torre|Zona)$'),Path("ma", q15, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q11.set_paths([Path("nb", q12, "1",r'^\w+$')])
    q12.set_paths([Path("u", q13, "0",r'^(Bloque|Celula|Etapa|Urbanizacion|Sector|Torre|Zona)$'),Path("ma", q15, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$'),Path("nb", q12, "1",r'^\w+$')])
    q13.set_paths([Path("nu", q14, "1",r'^\w+$')])
    q14.set_paths([Path("ma", q15, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$'),Path("nu", q14, "1",r'^\w+$')])
    q15.set_paths([Path("nma", q16, "1",r'^\w+$')])
    q16.set_paths([Path("tp", q17, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q17.set_paths([Path("ip", q18, "1",r'^\w+$')])
    #Barrio // urbana
    q19.set_paths([Path("nb", q20, "0",r'^\w+$')])
    q20.set_paths([Path("u", q21, "0",r'^(Bloque|Celula|Etapa|Urbanizacion|Sector|Torre|Zona)$'),Path("ma", q23, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("nb", q20, "0",r'^\w+$')])
    q21.set_paths([Path("nu", q22, "0",r'^\w+$')])
    q22.set_paths([Path("ma", q23, "0",r'^(Manzana|Interior|Sector|Etapa|Edificio|Modulo|Torre)$'),Path("nu", q22, "0",r'^\w+$')])
    q23.set_paths([Path("nma", q24, "1",r'^\w+$')])
    q24.set_paths([Path("tp", q25, "0",r'^(Altillo|Apartamento|Bodega|Casa|Consultorio|Deposito|Garaje|Local|Lote|Mezzanine|Oficina|Parqueadero|Pent-House|Planta|Predio|Semisotano|Sotano|Suite|Terraza|Unidad)$')])
    q25.set_paths([Path("ip", q26, "1",r'^\w+$')])
    #Vereda // rural
    q27.set_paths([Path("nvda", q28, "1",r'^\w+$')])
    q28.set_paths([Path("sc", q29, "0",r'^Sector$'),Path("nvda", q28, "1",r'^\w+$')])
    q29.set_paths([Path("nsc", q30, "1",r'^\w+$')])
    q30.set_paths([Path("nsc", q30, "1",r'^\w+$')])
    #Km y via //rural
    q31.set_paths([Path("nmk", q32, "0",r'^[1-9][0-9]{0,2}$')])
    q32.set_paths([Path("v", q33, "0",r'^Via$')])
    q33.set_paths([Path("n1", q34, "1",r'^\w+$')])
    q34.set_paths([Path("n2", q35, "1",r'^\w+$')])
    return q0.walk(word)

def address_validator_dian(word: str) -> bool:
   
    q0.set_paths([Path("tv", q1, "0",r'\b(AU|AV|AC|AK|BL|CL|KR|CT|CQ|CV|DG|CC|PJ|PS|PT|TV|VT|VI|TC)\b'), Path("br2", q19, "0",r'\b(BR|CD|SM)\b'),Path("vda", q27, "0",r'\bVDA\b'),Path("km", q31, "0",r'\bKM\b')])
    #Urbana
    q1.set_paths([Path("nv", q2, "0",r'^[1-9][0-9]{0,2}$')])
    q2.set_paths([Path("lv", q2, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1}))$'),Path("bis", q3, "0",r'^(BIS)$'),Path("c", q5, "0",r'^(NORTE|SUR|ESTE|OESTE)$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}$')])
    q3.set_paths([Path("lp", q4, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1}))$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}$'),Path("c", q5, "0",r'^(NORTE|SUR|ESTE|OESTE)$')])
    q4.set_paths([Path("c", q5, "0",r'^(NORTE|SUR|ESTE|OESTE)$'),Path("nv", q6, "0",r'^[1-9][0-9]{0,2}$')])
    q5.set_paths([Path("nv", q6, "0",r'^[1-9][0-9]{0,2}$')])
    q6.set_paths([Path("lv", q6, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1}))$'),Path("bis", q7, "0",r'^(BIS)$'),Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q7.set_paths([Path("lp", q8, "0",r'^(([A-Z][1-9][A-Z])|([A-Z]{2})|([A-Z]{0,1}))$'),Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q8.set_paths([Path("np", q9, "1",r'\b[1-9][0-9]{0,2}\b')])
    q9.set_paths([Path("c", q10, "1",r'^(NORTE|SUR|ESTE|OESTE)$'),Path("br", q11, "0",r'\b(BR|CD|SM)\b'),Path("u", q13, "0",r'^(BQ|CU|ET|UR|SC|TO|ZN)$'),Path("ma", q15, "0",r'^(MZ|IN|SC|ET|ED|MD|TO)$'),Path("tp", q17, "0",r'^(AL|AP|BG|CS|CN|DP|GA|LC|LT|MN|OF|PA|PN|PL|PD|SS|SO|ST|TZ|UN|UL|LM|GS|DS)$')])
    q10.set_paths([Path("br", q11, "0",r'\b(BR|CD|SM)\b'),Path("u", q13, "0",r'^(BQ|CU|ET|UR|SC|TO|ZN)$'),Path("ma", q15, "0",r'^(MZ|IN|SC|ET|ED|MD|TO)$'),Path("tp", q17, "0",r'^(AL|AP|BG|CS|CN|DP|GA|LC|LT|MN|OF|PA|PN|PL|PD|SS|SO|ST|TZ|UN|UL|LM|GS|DS)$')])
    q11.set_paths([Path("nb", q12, "1",r'^\w+$')])
    q12.set_paths([Path("u", q13, "0",r'^(BQ|CU|ET|UR|SC|TO|ZN)$'),Path("ma", q15, "0",r'^(MZ|IN|SC|ET|ED|MD|TO)$'),Path("tp", q17, "0",r'^(AL|AP|BG|CS|CN|DP|GA|LC|LT|MN|OF|PA|PN|PL|PD|SS|SO|ST|TZ|UN|UL|LM|GS|DS)$'),Path("nb", q12, "1",r'^\w+$')])
    q13.set_paths([Path("nu", q14, "1",r'^\w+$')])
    q14.set_paths([Path("ma", q15, "0",r'^(MZ|IN|SC|ET|ED|MD|TO)$'),Path("tp", q17, "0",r'^(AL|AP|BG|CS|CN|DP|GA|LC|LT|MN|OF|PA|PN|PL|PD|SS|SO|ST|TZ|UN|UL|LM|GS|DS)$'),Path("nu", q14, "1",r'^\w+$')])
    q15.set_paths([Path("nma", q16, "1",r'^\w+$')])
    q16.set_paths([Path("tp", q17, "0",r'^(AL|AP|BG|CS|CN|DP|GA|LC|LT|MN|OF|PA|PN|PL|PD|SS|SO|ST|TZ|UN|UL|LM|GS|DS)$')])
    q17.set_paths([Path("ip", q18, "1",r'^\w+$')])
    #Barrio // urbana
    q19.set_paths([Path("nb", q20, "0",r'^\w+$')])
    q20.set_paths([Path("u", q21, "0",r'^(BQ|CU|ET|UR|SC|TO|ZN)$'),Path("ma", q23, "0",r'^(MZ|IN|SC|ET|ED|MD|TO)$'),Path("nb", q20, "0",r'^\w+$')])
    q21.set_paths([Path("nu", q22, "0",r'^\w+$')])
    q22.set_paths([Path("ma", q23, "0",r'^(MZ|IN|SC|ET|ED|MD|TO)$'),Path("nu", q22, "0",r'^\w+$')])
    q23.set_paths([Path("nma", q24, "1",r'^\w+$')])
    q24.set_paths([Path("tp", q25, "0",r'^(AL|AP|BG|CS|CN|DP|GA|LC|LT|MN|OF|PA|PN|PL|PD|SS|SO|ST|TZ|UN|UL|LM|GS|DS)$')])
    q25.set_paths([Path("ip", q26, "1",r'^\w+$')])
    #Vereda // rural
    q27.set_paths([Path("nvda", q28, "1",r'^\w+$')])
    q28.set_paths([Path("sc", q29, "0",r'^SC$'),Path("nvda", q28, "1",r'^\w+$')])
    q29.set_paths([Path("nsc", q30, "1",r'^\w+$')])
    q30.set_paths([Path("nsc", q30, "1",r'^\w+$')])
    #Km y via //rural
    q31.set_paths([Path("nmk", q32, "0",r'^[1-9][0-9]{0,2}$')])
    q32.set_paths([Path("v", q33, "0",r'^VI$')])
    q33.set_paths([Path("n1", q34, "1",r'^\w+$')])
    q34.set_paths([Path("n2", q35, "1",r'^\w+$')])
    return q0.walk(word)

def address_validator_file(file: TextIO) -> None:
    files_address: str = file.readlines()
    with open("output.txt","w") as file_object:
        for file in files_address:
            file = file.rstrip('\n')
            if address_validator(file):
                file_object.write(file+" aceptada\n")
            elif not address_validator(file):
                file_object.write(file+" rechazada\n")
                
def address_validator_file_dian(file: TextIO)-> None:
    files_address: str = file.readlines()
    with open("output.txt","w") as file_object:
        for file in files_address:
            file = file.rstrip('\n')
            if address_validator_dian(file):
                file_object.write(file+" aceptada\n")
            elif not address_validator_dian(file):
                file_object.write(file+" rechazada\n")
