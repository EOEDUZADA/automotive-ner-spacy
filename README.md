

Descrição
Projeto prático aplicando Processamento de Linguagem Natural (PLN) e Machine Learning. Utilizei o framework **spaCy v3** para ler textos de ordens de serviço de oficinas mecânicas e extrair automaticamente três coisas: Peças, Serviços e Valores.

Eu queria que o computador conseguisse ler uma frase ou parágrafo de texto livre (como o texto de um orçamento de oficina) e separasse essas três categorias de negócio:
*   `PECA`: Amortecedor, pastilha de freio, marcas como Bosch, Monroe, etc.
*   `SERVICO`: Troca de óleo, alinhamento, balanceamento, cambagem.
*   `VALOR`: Preços como 150, 480,00, 1.200,00.

Tecnologias e Bibliotecas Utilizadas
*   Python 3
*   Label Studio (Para a interface e exportação das anotações das entidades)
*   spaCy v3 (Pipeline de PLN e treinamento do modelo de NER)
*   Scikit-Learn (Para o split de treino e teste)
*   Google Colab (Ambiente de desenvolvimento na nuvem)

*   obs: O projeto foi criado para aprendizado sobre o framework e overfitting
