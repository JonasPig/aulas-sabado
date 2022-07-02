class Casa():
    def __init__(self, rua, bairro, cep):
        self.rua = rua
        self.bairro = bairro
        self.cep = cep

    def enderecoCompleto (self) :
        return "Endereco Completo:"+self.rua+","+self.bairro+" "+self.cep

casa1 = Casa(rua = "rua baia ", bairro="alguma coisa", cep="78467")
casa2 = Casa(rua = "rua olavio", bairro="teste", cep="62546")

print(casa1.enderecoCompleto())
print(casa2.enderecoCompleto())

<p>oi</p>
