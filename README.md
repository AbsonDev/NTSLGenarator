# Documentação NTSL - Nelogica Trading System Language

## 📋 Índice

- [Introdução](#introdução)
- [O que é NTSL?](#o-que-é-ntsl)
- [Estrutura de uma Estratégia](#estrutura-de-uma-estratégia)
- [Sintaxe Básica](#sintaxe-básica)
- [Tipos de Dados e Variáveis](#tipos-de-dados-e-variáveis)
- [Estruturas de Controle](#estruturas-de-controle)
- [Indicadores Técnicos](#indicadores-técnicos)
- [Funções de Automação](#funções-de-automação)
- [Exemplos Práticos](#exemplos-práticos)
- [Recursos e Documentação](#recursos-e-documentação)

---

## Introdução

Esta documentação foi criada para auxiliar traders e desenvolvedores a entender e utilizar a linguagem NTSL (Nelogica Trading System Language) para criar estratégias automatizadas de trading na plataforma Profit da NeoLogica.

---

## O que é NTSL?

**NTSL** significa **Nelogica Trading System Language** - uma linguagem de programação proprietária criada exclusivamente pela NeoLogica para uso na **Plataforma Profit**.

### Características Principais

- **Sintaxe**: Baseada em Pascal e EasyLanguage (TradeStation)
- **Propósito**: Desenvolvimento de estratégias automatizadas de trading
- **Plataforma**: Editor de Estratégias do Profit
- **Uso**: Codificar, testar e simular operações no mercado financeiro

### Para que serve?

A NTSL permite criar:

- ✅ **Robôs traders (bots)** para automação de operações
- ✅ **Indicadores personalizados** para análise técnica
- ✅ **Backtesting** de estratégias com dados históricos
- ✅ **Coloração de gráficos** customizada
- ✅ **Filtros de ativos** (screening/rastreamento)
- ✅ **Sistemas de gerenciamento de risco**

---

## Estrutura de uma Estratégia

Uma estratégia em NTSL é dividida em **três áreas principais**:

```pascal
// 1. ÁREA DE PARÂMETROS (INPUT)
input
    Parametro1(10),  // Parâmetros configuráveis
    Parametro2(20);

// 2. ÁREA DE VARIÁVEIS E FUNÇÕES (VAR)
var
    MinhaVariavel: integer;
    MediaMovel: float;

// 3. ÁREA DE CÓDIGO (BEGIN...END)
begin
    // Seu código aqui
    MediaMovel := MediaExp(20, Close);

    if MediaMovel > Close then
        Buy;
end;
```

### Detalhamento das Áreas

1. **Área INPUT**: Entre `input` e `var`
   - Declara parâmetros configuráveis pelo usuário
   - Permite ajustar a estratégia sem modificar o código

2. **Área VAR**: Entre `var` e `begin`
   - Declara variáveis e funções
   - Define tipos de dados necessários

3. **Área BEGIN...END**: Código executável
   - Contém a lógica da estratégia
   - Calcula sinais e executa ordens

---

## Sintaxe Básica

### Declaração de Variáveis

```pascal
var
    NomeVariavel: Tipo;
```

**Sintaxe obrigatória**: `Nome : Tipo`

### Comentários

```pascal
// Comentário de linha única

{ Comentário
  de múltiplas
  linhas }
```

### Atribuição

```pascal
MinhaVariavel := Valor;
```

**Importante**: Use `:=` para atribuição (não `=`)

### Operadores

#### Operadores Aritméticos
- `+` Adição
- `-` Subtração
- `*` Multiplicação
- `/` Divisão

#### Operadores Relacionais
- `=` Igual
- `<>` Diferente
- `>` Maior que
- `<` Menor que
- `>=` Maior ou igual
- `<=` Menor ou igual

#### Operadores Lógicos
- `and` E lógico
- `or` OU lógico
- `not` NÃO lógico

---

## Tipos de Dados e Variáveis

### Tipos Primitivos

```pascal
var
    Inteiro: integer;        // Números inteiros
    Decimal: float;          // Números decimais (ponto flutuante)
    Booleano: boolean;       // true ou false
    Texto: string;           // Texto/string
```

### Séries de Dados

**Todas as variáveis em NTSL são séries de dados**, permitindo acessar valores históricos através de indexação:

```pascal
var
    Preco: float;

begin
    Preco := Close;        // Valor atual
    Preco[1];              // Valor de 1 candle atrás
    Preco[5];              // Valor de 5 candles atrás
end;
```

### Preços OHLC

Variáveis built-in para acessar preços:

- `Open` - Preço de abertura
- `High` - Preço máximo
- `Low` - Preço mínimo
- `Close` - Preço de fechamento
- `Volume` - Volume negociado

```pascal
begin
    if Close > Open then
        // Candle de alta
        Plot(Close, 'Verde');
end;
```

---

## Estruturas de Controle

### IF / THEN / ELSE

```pascal
if Condicao then
    Comando
else
    OutroComando;

// Múltiplos comandos
if Condicao then
begin
    Comando1;
    Comando2;
end
else
begin
    Comando3;
    Comando4;
end;
```

### FOR (Loop com Contador)

```pascal
var
    i: integer;

begin
    for i := 1 to 10 do
    begin
        // Executa 10 vezes
    end;
end;
```

### WHILE (Loop Condicional)

```pascal
var
    contador: integer;

begin
    contador := 0;
    while contador < 10 do
    begin
        contador := contador + 1;
        // Executa enquanto contador < 10
    end;
end;
```

---

## Indicadores Técnicos

### Médias Móveis

#### Média Móvel Simples (SMA)

```pascal
var
    MediaSimples: float;

begin
    MediaSimples := Media(20, Close);  // Média de 20 períodos
end;
```

#### Média Móvel Exponencial (EMA)

```pascal
var
    MediaExp: float;

begin
    MediaExp := MediaExp(80, Close);  // EMA de 80 períodos
end;
```

### MACD (Moving Average Convergence Divergence)

```pascal
var
    MacdLinha: float;
    MacdSinal: float;

begin
    // MACD(MediaLonga, MediaCurta, Sinal)|Tipo|
    MacdLinha := MACD(26, 12, 9)|0|;  // Linha MACD
    MacdSinal := MACD(26, 12, 9)|1|;  // Linha de sinal

    // Calculando média do MACD
    MediaDoMacd := MediaExp(9, MACD(26, 12, 9)|0|);
end;
```

### RSI (Índice de Força Relativa)

```pascal
var
    RSI14: float;

begin
    RSI14 := RSI(14);  // RSI de 14 períodos

    if RSI14 < 30 then
        // Sobrevenda
        Buy
    else if RSI14 > 70 then
        // Sobrecompra
        Sell;
end;
```

### Bandas de Bollinger

```pascal
var
    BandaSuperior: float;
    BandaInferior: float;
    BandaMedia: float;

begin
    BandaSuperior := BollingerBands(20, 2)|0|;  // Banda superior
    BandaMedia := BollingerBands(20, 2)|1|;     // Banda média
    BandaInferior := BollingerBands(20, 2)|2|;  // Banda inferior
end;
```

---

## Funções de Automação

### Ordens de Compra (Long)

#### Compra a Mercado

```pascal
BuyAtMarket;
```

#### Compra com Limite

```pascal
BuyLimit(Preco);
```

#### Compra com Stop

```pascal
BuyStop(Preco);
```

### Ordens de Venda (Short)

#### Venda a Descoberto a Mercado

```pascal
SellShortAtMarket;
```

#### Venda a Descoberto com Limite

```pascal
SellShortLimit(Preco);
```

#### Venda a Descoberto com Stop

```pascal
SellShortStop(Preco);
```

### Ordens de Saída

#### Fechar Posição Comprada

```pascal
Sell;  // Venda a mercado
SellLimit(Preco);  // Venda com limite
SellStop(Preco);   // Venda com stop
```

#### Fechar Posição Vendida

```pascal
BuyToCover;  // Compra para cobrir a mercado
BuyToCoverLimit(Preco);  // Compra para cobrir com limite
BuyToCoverStop(Preco);   // Compra para cobrir com stop
```

### Gerenciamento de Posição

```pascal
var
    PosicaoAtual: integer;

begin
    PosicaoAtual := Position;  // Retorna a posição atual

    if PosicaoAtual = 0 then
        // Sem posição
    else if PosicaoAtual > 0 then
        // Posição comprada
    else if PosicaoAtual < 0 then
        // Posição vendida
end;
```

---

## Exemplos Práticos

### Exemplo 1: Cruzamento de Médias Móveis

```pascal
input
    PeriodoRapida(9),
    PeriodoLenta(21);

var
    MediaRapida: float;
    MediaLenta: float;

begin
    // Calcula as médias
    MediaRapida := MediaExp(PeriodoRapida, Close);
    MediaLenta := MediaExp(PeriodoLenta, Close);

    // Sinal de compra: média rápida cruza acima da lenta
    if (MediaRapida > MediaLenta) and
       (MediaRapida[1] <= MediaLenta[1]) then
    begin
        if Position <= 0 then  // Se não está comprado
        begin
            BuyAtMarket;
        end;
    end;

    // Sinal de venda: média rápida cruza abaixo da lenta
    if (MediaRapida < MediaLenta) and
       (MediaRapida[1] >= MediaLenta[1]) then
    begin
        if Position >= 0 then  // Se não está vendido
        begin
            SellShortAtMarket;
        end;
    end;
end;
```

### Exemplo 2: Estratégia com RSI

```pascal
input
    PeriodoRSI(14),
    NivelSobrecompra(70),
    NivelSobrevenda(30);

var
    RSIAtual: float;

begin
    RSIAtual := RSI(PeriodoRSI);

    // Compra em sobrevenda
    if RSIAtual < NivelSobrevenda then
    begin
        if Position <= 0 then
            BuyAtMarket;
    end;

    // Vende em sobrecompra
    if RSIAtual > NivelSobrecompra then
    begin
        if Position >= 0 then
            SellShortAtMarket;
    end;
end;
```

### Exemplo 3: Estratégia com Stop Loss e Gain

```pascal
input
    PercentualStop(2),      // 2% de stop loss
    PercentualGain(4);      // 4% de stop gain

var
    PrecoEntrada: float;
    StopLoss: float;
    StopGain: float;

begin
    // Lógica de entrada (exemplo simples)
    if Close > MediaExp(20, Close) then
    begin
        if Position = 0 then
        begin
            BuyAtMarket;
            PrecoEntrada := Close;

            // Calcula stop loss e gain
            StopLoss := PrecoEntrada * (1 - PercentualStop/100);
            StopGain := PrecoEntrada * (1 + PercentualGain/100);
        end;
    end;

    // Gerenciamento de risco
    if Position > 0 then
    begin
        // Stop Loss
        if Close <= StopLoss then
            Sell;

        // Stop Gain
        if Close >= StopGain then
            Sell;
    end;
end;
```

### Exemplo 4: Estratégia MACD + RSI (Confirmação Dupla)

```pascal
input
    PeriodoRSI(14);

var
    MacdLinha: float;
    MacdSinal: float;
    RSIAtual: float;

begin
    MacdLinha := MACD(26, 12, 9)|0|;
    MacdSinal := MACD(26, 12, 9)|1|;
    RSIAtual := RSI(PeriodoRSI);

    // Compra: MACD cruza para cima E RSI não está sobrecomprado
    if (MacdLinha > MacdSinal) and
       (MacdLinha[1] <= MacdSinal[1]) and
       (RSIAtual < 70) then
    begin
        if Position <= 0 then
            BuyAtMarket;
    end;

    // Venda: MACD cruza para baixo E RSI não está sobrevendido
    if (MacdLinha < MacdSinal) and
       (MacdLinha[1] >= MacdSinal[1]) and
       (RSIAtual > 30) then
    begin
        if Position >= 0 then
            SellShortAtMarket;
    end;
end;
```

---

## Recursos e Documentação

### Documentação Oficial

- **Manual NTSL (PDF)**: [https://www.nelogica.com.br/manualntsl](https://www.nelogica.com.br/manualntsl)
- **Download Direto**: [Manual NTSL PDF](https://downloadserver-cdn.nelogica.com.br/content/profit/manual_ntsl/ManualNTSL.pdf)
- **Central de Ajuda**: [Documentação NTSL - Compilado de Funções](https://ajuda.nelogica.com.br/hc/pt-br/articles/360046443212)

### Tutoriais e Guias

- [Como montar uma estratégia](https://ajuda.nelogica.com.br/hc/pt-br/articles/9794527588123)
- [Editor de Estratégias](https://ajuda.nelogica.com.br/hc/pt-br/articles/9165042993691)
- [Módulo de Automação](https://ajuda.nelogica.com.br/hc/pt-br/articles/18501196212251)

### Comunidade e Exemplos

- [NeoTraderBot - Documentação NTSL](https://neotraderbot.com/docs/material-iniciantes/plataformas/documentacao-ntsl-nelogica/)
- [NeoTraderBot - Editor de Estratégias](https://neotraderbot.com/docs/material-iniciantes/plataformas/editor-estrategias-profit/)
- [Melhores Práticas NTSL](https://neotraderbot.com/2022/11/06/melhores-praticas-para-escrever-sua-estrategia/)

### Recursos Adicionais

- [Notas de Atualização NTSL](https://ajuda.nelogica.com.br/hc/pt-br/community/posts/13442294857499)
- [Manual de Boas Práticas - Loja de Estratégias](https://ajuda.nelogica.com.br/hc/pt-br/articles/18041626226715)

---

## Boas Práticas

### 1. Organização do Código

- Use indentação adequada
- Nomeie variáveis de forma descritiva
- Comente seções importantes do código
- Separe logicamente diferentes partes da estratégia

### 2. Testes e Validação

- Sempre faça backtesting antes de automatizar
- Teste em diferentes períodos e ativos
- Valide os resultados antes de operar com dinheiro real
- Use período de paper trading para validação

### 3. Gerenciamento de Risco

- Sempre implemente stop loss
- Defina tamanho de posição adequado
- Não arrisque mais de 1-2% do capital por operação
- Considere múltiplas confirmações antes de entrar em posição

### 4. Otimização

- Evite over-fitting (ajuste excessivo aos dados históricos)
- Use parâmetros simples e robustos
- Teste em dados fora da amostra (out-of-sample)
- Mantenha a estratégia simples

---

## Limitações Conhecidas

### Módulo de Automação

⚠️ **Importante**: Algumas funções podem não funcionar corretamente no módulo de automação:

- Funções de cobertura como `BuyToCoverLimit`, `BuyToCoverStop`, `SellShortToCoverLimit` e `SellShortToCoverStop` podem necessitar refatoração
- Nem todas as funções disponíveis no backtesting funcionam na automação
- Sempre teste sua estratégia no modo simulação antes de ativar automação real

---

## Contribuindo

Este documento é uma compilação de informações públicas sobre NTSL. Para informações mais detalhadas e atualizadas, consulte sempre a documentação oficial da NeoLogica.

---

## Licença

Esta documentação é fornecida apenas para fins educacionais. NTSL é uma marca registrada da NeoLogica Sistemas de Software.

---

**Última atualização**: Dezembro 2024

**Fontes**:
- [NeoLogica - Central de Ajuda](https://ajuda.nelogica.com.br/)
- [NeoTraderBot](https://neotraderbot.com/)
- [Manual NTSL Oficial](https://www.nelogica.com.br/manualntsl)
