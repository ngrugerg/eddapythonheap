class Paciente:
    def __init__(self, nome, tipoSanguineo, dataNasc):
        self.nome = nome
        self.tipoSanguineo = tipoSanguineo
        self.dataNasc = dataNasc
    
    def __repr__(self):
        return self.nome + ', tipo sanguíneo: ' + self.tipoSanguineo + ', nascido em: ' + self.dataNasc

class MaxHeap:

    def __init__(self):
        self.heap = [0]

    def put(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if len(self.heap) != 1:
            return self.heap[1]
        else:
            return str("Não há próximo paciente")
            
    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1: # nao faz nada se for raiz
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)


def escolha(opcao):
    match opcao:
        case 1:
            nome = input("Digite o nome do paciente: ")
            tipoSanguineo = input("Digite o tipo sanguineo do paciente: ")
            dataNasc = input("Digite a data de nascimento do paciente: ")
            paciente = Paciente(nome, tipoSanguineo, dataNasc)
            prioridade = 0
            while(prioridade < 1 or prioridade > 10):
                prioridade = int(input("Digite a prioridade do paciente(1-10): "))
            global ordem
            global cont
            item = (prioridade, ordem, paciente)
            h.put(item)
            ordem += 1
            cont -= 1
            print("Contador atual: ", cont)
        case 2:
            if(h.peek()):
                chamados.append(h.peek())
            print(h.get())
        case 3:
            print(h.peek())
        case 4:
            if(len(chamados)<=4):
                for i in range(len(chamados)):
                    print(chamados[i])
            else:
                for i in range(1,6):
                    print(chamados[len(chamados) - i])
        case _:
            print("Opção inválida")
        
## Sistema ##
cont = 999
ordem = 0
h = MaxHeap()
chamados = list()
while(True):
    print("(1) Adicionar novo paciente")
    print("(2) Chamar próximo paciente")
    print("(3) Mostrar próximo paciente")
    print("(4) Listar últimos 5 chamados")
    i = 0
    while(i<1 or i>4):
        i = int(input("Digite o que deseja fazer: "))
        escolha(i)