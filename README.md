# Padrões de Projeto

Este repositório contém exemplos de três padrões de projeto: Iterator, Facade e Singleton, utilizando a linguagem Python.

## Iterator

**Propósito**: Fornece uma maneira de acessar os elementos de um agregado sequencialmente sem expor sua representação subjacente.

**Problema**: Quando você precisa percorrer diferentes coleções de dados (listas, árvores, grafos, etc.) sem expor sua estrutura interna.

**Solução**: Cria uma interface para percorrer os elementos de uma coleção e mantém o controle do estado atual da iteração.

![Iterator UML](https://refactoring.guru/images/patterns/diagrams/iterator/structure-2x.png)

**Classe  `Iterator`**
- Construtor (`__init__`): Inicializa o iterador com a coleção (`aggregate`) e define o índice inicial (`_index`) como 0.
- Método  `has_next`: Verifica se há elementos na coleção para iterar, retornando  `True`  se houver e  `False`  caso contrário.
- Método  `next`: Retorna o próximo item da coleção se houver mais elementos. Caso contrário, passa em  `StopIteration`.  

**Classe  `Aggregate`**:
- Construtor (`__init__`): Inicializa a lista de itens (`_items`) como uma lista vazia.
- Método  `add_item`: Adiciona um item a lista de itens.
- Método  `create_iterator`: Cria e retorna um iterador para a lista de itens.

1.  **Criação do Agregado**:
    
- Um objeto  `Aggregate`  é criado e três itens ("Item 1", "Item 2", "Item 3") são adicionados a lista de itens.
  
2.  **Criação do Iterador**:

- Um iterador é criado para a lista de itens do agregado usando o método  `create_iterator`.
3.  **Iteração sobre os Itens**:
    
- Um loop  `while`  é usado para iterar sobre os itens da coleção. O método  `has_next`  verifica se ainda há itens para iterar, e o método  `next`  retorna o próximo item.

**Código**: [iterator.py](./iterator.py)

## Facade

**Propósito**: Fornece uma interface simplificada para um subsistema complexo.

**Problema**: Quando você precisa interagir com um subsistema complexo e deseja fornecer uma interface mais simples e amigável para os usuários.

**Solução**: Facilita a interação com o subsistema fornecendo uma interface unificada e simplificada.

![Facade UML](https://refactoring.guru/images/patterns/diagrams/facade/structure-2x.png)

**Classes SubsystemA e SubsystemB**:
    
- Estas são classes de subsistemas que possuem métodos específicos (`operation_a`  e  `operation_b`).
- `SubsystemA`  tem um método  `operation_a`  que retorna a string  `"Operação A do Subsistema A"`.
- `SubsystemB`  tem um método  `operation_b`  que retorna a string  `"Operação B do Subsistema B!"`.

**Classe Facade**:
   
- Esta classe serve como uma interface simplificada para interagir com os subsistemas.
- No método  `__init__`, ela instancia objetos de  `SubsystemA`  e  `SubsystemB`.
- O método  `operation`  chama os métodos dos subsistemas (`operation_a`  e  `operation_b`), armazena os resultados em uma lista e retorna uma string com os resultados concatenados, separados por uma nova linha.
    
**Bloco Principal**:
    
- Se o script for executado diretamente (não importado como módulo), ele cria uma instância da classe  `Facade`  e chama o método  `operation`, imprimindo o resultado no console.  

**Código**: [facade.py](./facade.py)

## Singleton

**Propósito**: Garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a ela.

**Problema**: Quando você precisa garantir que apenas uma instância de uma classe seja criada e fornecer um ponto global de acesso a essa instância.

**Solução**: A classe Singleton controla sua própria instância e fornece um método para acessá-la.

![Singleton UML](https://refactoring.guru/images/patterns/diagrams/singleton/structure-en.png)

**Classe `Singleton`**:

- Definida com um atributo de classe `_instance` inicializado como `None`. Este atributo armazenará a única instância da classe

**Método  `__new__`**:

- O método  `__new__`  é sobrescrito para controlar a criação de novas instâncias.
- Se  `_instance`  ainda não foi definida (`None`), uma nova instância é criada usando  `super(Singleton, cls).__new__(cls, *args, **kwargs)`  e atribuída a  `_instance`.
- Se  `_instance`  já foi definida, a mesma instância é retornada, garantindo que apenas uma instância da classe exista.

**Método  `some_business_logic`**:

- Um método de exemplo que retorna uma string. Este método representa a lógica de negócios que a instância Singleton pode executar.

**Main**:

- Duas variáveis,  `singleton1`  e  `singleton2`, são criadas como instâncias da classe  `Singleton`.
- A expressão  `print(singleton1 is singleton2)`  imprime  `True`, indicando que ambas as variáveis referenciam a mesma instância.
- A expressão  `print(singleton1.some_business_logic())`  imprime  `"Lógica de Negócio do Singleton"`, demonstrando o uso do método da instância Singleton.

**Código**: [singleton.py](./singleton.py)