from addressValidator import address_validator,address_validator_dian,address_validator_file,address_validator_file_dian

def test_address_validator() -> str:

    address = "Calle 3BC #10-2 Barrio San Juan Apartamento 201"
    if address_validator(address):
       return address+" direccion valida"
    else:
       return address+" direccion invalida"

def test_address_validator_dian() -> str:

    address = "AV 33 B2C BIS 10 21 BR SOCORRO AP 2"
    if address_validator_dian(address):
       return address+" direccion valida"
    else:
       return address+" direccion invalida"

def test_address_validator_file() -> None:

    with open("address.txt") as file_object:
         address_validator_file(file_object)

def test_address_validator_file_dian() -> None:

    with open("addressDian.txt") as file_object:
         address_validator_file_dian(file_object)

if __name__ == "__main__":
    print(test_address_validator())
    print(test_address_validator_dian())
    test_address_validator_file()
    test_address_validator_file_dian()
