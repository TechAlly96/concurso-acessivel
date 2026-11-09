# Curso, módulo 3. Informática: arquitetura do computador, periféricos e armazenamento, sistemas operacionais, Windows 10, Linux, arquivos, pastas e permissões

Olá! Este é o terceiro módulo de Informática. No primeiro, você estudou redes, internet e o Marco Civil; no segundo, segurança, criptografia e software livre. Agora vamos ao computador em si: as **peças** que o compõem, os **periféricos**, as **mídias de armazenamento**, os **sistemas operacionais** Windows 10 e Linux, os **arquivos e pastas**, os **atalhos de teclado** e as **permissões**.

Um aviso para quem estuda ouvindo: os atalhos de teclado são lidos com a palavra "**mais**". Por exemplo, "**Control mais C**" quer dizer apertar a tecla Control e, sem soltá-la, apertar a letra C. E os comandos do Linux, que são escritos em **letras minúsculas**, são soletrados letra por letra.

Uma curiosidade útil para você: os **leitores de tela**, que permitem a pessoas cegas usar o computador, funcionam justamente com os **atalhos de teclado**. Então, este módulo serve para a prova e para o seu dia a dia.

---

## Aula 1. A arquitetura do computador

**Hardware e software.** **Hardware** é a parte **física** do computador: as peças, os cabos, os circuitos. **Software** é a parte **lógica**: os programas, os sistemas, os dados. Uma frase antiga resume: hardware é o que você chuta; software é o que você xinga.

**O processador.** A **unidade central de processamento**, conhecida pela sigla **C P U**, é o "**cérebro**" do computador. Ela executa as instruções dos programas. Tem três partes principais:

a **unidade de controle**, que **coordena** a execução das instruções;

a **unidade lógica e aritmética**, que faz os **cálculos** e as comparações lógicas;

e os **registradores**, pequenas memórias **dentro do próprio processador**, as mais rápidas de todas.

**As memórias.** Há vários tipos, e a banca adora comparar.

**Memória R A M**, de acesso aleatório: é a memória **principal**, onde ficam os programas e os dados **que estão sendo usados naquele momento**. É de **leitura e escrita** e é **volátil**: **perde tudo quando o computador é desligado**. Por isso, se a energia cai antes de você salvar um documento, você perde o que não salvou.

**Memória R O M**, somente de leitura: é **não volátil**, ou seja, **não perde** o conteúdo ao desligar. Guarda o **programa de inicialização** do computador, o firmware, conhecido como **B I O S** ou, nos computadores mais novos, **U E F I**, que é o primeiro programa a rodar quando você liga a máquina.

**Memória cache**: uma memória **muito rápida e pequena**, que fica entre o processador e a memória R A M, guardando os dados usados com mais frequência, para o processador não precisar esperar.

**A hierarquia das memórias.** Da **mais rápida** e menor para a **mais lenta** e maior: **registradores, cache, memória R A M e armazenamento secundário**, como o disco. Quanto mais perto do processador, mais rápida, mais cara e menor. Macete: "**registrador, cache, R A M, disco: do mais rápido ao mais lento**".

**A memória virtual.** Quando a memória R A M fica cheia, o sistema operacional usa uma parte do **disco** como se fosse memória R A M. É a memória virtual: no Windows, chama-se **arquivo de paginação**; no Linux, **área de troca**, ou swap. Ela evita que o computador trave, mas deixa tudo **mais lento**, porque o disco é muito mais lento que a R A M.

**As unidades de medida.** O **bit** é a menor unidade de informação: um zero ou um. Um **byte** são **oito bits**, e representa, por exemplo, uma letra. Depois vêm o **kilobyte**, o **megabyte**, o **gigabyte** e o **terabyte**, cada um cerca de **mil vezes** maior que o anterior; tecnicamente, mil e vinte e quatro vezes. Macete: "**quilo, mega, giga, tera**", sempre multiplicando por mil.

---

## Aula 2. Os periféricos e as mídias de armazenamento

**Os periféricos.** São os dispositivos ligados ao computador para **trocar informações** com ele. Dividem-se em três grupos.

**Periféricos de entrada**: enviam dados **para** o computador. Exemplos: **teclado**, **mouse**, **scanner**, **microfone**, **webcam**, leitor de código de barras e leitor biométrico de impressão digital.

**Periféricos de saída**: recebem dados **do** computador e os apresentam ao usuário. Exemplos: **monitor**, **impressora**, **caixa de som** e **fone de ouvido**. Um ponto importante para você: os **leitores de tela** usam a placa de som e as caixas de som ou fones como saída.

**Periféricos de entrada e saída**, também chamados mistos: fazem as duas coisas. Exemplos: a **tela sensível ao toque**, que mostra a imagem e recebe o toque; a **impressora multifuncional**, que imprime e digitaliza; e o **modem**, que envia e recebe dados da rede.

**As mídias de armazenamento.** São os dispositivos que **guardam os dados de forma permanente**, mesmo com o computador desligado. É o chamado armazenamento **secundário**.

**Disco rígido**, conhecido pela sigla **H D**: armazenamento **magnético**, com discos que **giram** e uma cabeça de leitura que se move. Tem **grande capacidade** e é **barato**, mas é mais **lento** e mais **sensível a impactos**, por causa das partes móveis.

**Unidade de estado sólido**, conhecida pela sigla **S S D**: armazenamento em **memória flash**, **sem partes móveis**. É **muito mais rápida**, mais **silenciosa**, mais **resistente a impactos** e gasta menos energia que o disco rígido, mas é mais cara por gigabyte.

**Pendrive** e **cartão de memória**: também usam **memória flash**, são pequenos e portáteis, e se ligam pela porta **U S B** ou por leitores de cartão.

**Mídias ópticas**: lidas por **laser**. O **C D** guarda cerca de **setecentos megabytes**; o **D V D**, cerca de **quatro vírgula sete gigabytes** na camada simples; e o **Blu-ray**, cerca de **vinte e cinco gigabytes** na camada simples. Macete da ordem de capacidade: "**C D, D V D, Blu-ray: do menor ao maior**".

**Armazenamento em nuvem**: os arquivos ficam guardados em **servidores na internet**, de empresas como Google, Microsoft e outras, e podem ser acessados de qualquer lugar.

**A porta U S B.** É o **barramento serial universal**, o padrão para ligar a maioria dos periféricos. Uma característica cobrada é o **plug and play**: o dispositivo funciona **logo que é conectado**, sem precisar reiniciar o computador, e permite a conexão com o computador ligado, chamada **conexão a quente**.

---

## Aula 3. Os sistemas operacionais e os arquivos

**O que é o sistema operacional.** É o **software principal** do computador, que fica **entre o usuário e o hardware**. Ele **gerencia** o processador, a memória, os dispositivos e os arquivos, e permite que os outros programas funcionem. Exemplos: **Windows**, **Linux**, **macOS**, e, nos celulares, **Android** e **iOS**. O **núcleo** do sistema, que conversa diretamente com o hardware, chama-se **kernel**.

**As características que caem.**

**Multitarefa**: executa **vários programas ao mesmo tempo**. O Windows e o Linux são multitarefa.

**Multiusuário**: permite que **vários usuários** tenham **contas** separadas, com os seus próprios arquivos e permissões. O Windows e o Linux são multiusuário.

**Interface gráfica e linha de comando**: a interface gráfica usa **janelas, ícones e mouse**; a linha de comando, também chamada **terminal**, usa **comandos digitados**. Para quem usa leitor de tela, o terminal pode ser muito prático, porque é todo em texto.

**Os arquivos e as extensões.** Um arquivo é um conjunto de dados com um **nome**. A **extensão** é a parte do nome **depois do último ponto**, e indica o **tipo** de arquivo. As mais cobradas:

**ponto docx**, **ponto xlsx** e **ponto pptx**: documentos de texto, planilhas e apresentações do **Microsoft Office**;

**ponto odt**, **ponto ods** e **ponto odp**: os mesmos tipos no **LibreOffice**, no formato aberto **O D F**, que é um padrão internacional;

**ponto pdf**: documento portátil, que mantém a formatação em qualquer computador;

**ponto txt**: texto puro, sem formatação;

**ponto jpg**, **ponto png** e **ponto gif**: imagens;

**ponto mp3**: áudio; **ponto mp4**: vídeo;

**ponto zip**, **ponto rar** e **ponto sete z**: arquivos **compactados**, que reduzem o tamanho e agrupam vários arquivos num só;

**ponto exe**: programa **executável** do Windows. Atenção: é a extensão mais perigosa em anexos de e-mail, porque pode conter código malicioso.

**As pastas e os caminhos.** As pastas, também chamadas **diretórios**, organizam os arquivos numa **estrutura em árvore**, com uma pasta principal, a **raiz**, e subpastas dentro dela. O **caminho**, ou rota, é o endereço de um arquivo nessa árvore.

No **Windows**, o caminho começa pela **letra da unidade**, como **C dois-pontos**, e as pastas são separadas pela **barra invertida**. Exemplo: C dois-pontos, barra invertida, Usuários, barra invertida, Marlon, barra invertida, Documentos.

No **Linux**, não há letras de unidade: tudo começa na **raiz**, representada por uma **barra normal**, e as pastas são separadas também pela **barra normal**. Exemplo: barra, home, barra, marlon, barra, documentos.

Macete: "**Windows usa barra invertida e letra de unidade; Linux usa barra normal e começa na raiz**".

**O caminho absoluto e o relativo.** O caminho **absoluto** começa **da raiz**, e funciona de qualquer lugar. O caminho **relativo** começa **da pasta atual**. Dois símbolos especiais: **um ponto** representa a **pasta atual**; **dois pontos** representam a **pasta de cima**, chamada pasta pai. E, no Linux, o **til** representa a **pasta pessoal** do usuário.

---

## Aula 4. O Windows 10

**Os elementos principais.** A **área de trabalho** é a tela principal. O **menu Iniciar** dá acesso aos programas. A **barra de tarefas**, na parte de baixo, mostra os programas abertos. O **Explorador de Arquivos** é o programa para gerenciar arquivos e pastas. As **Configurações** e o **Painel de Controle** permitem ajustar o sistema.

**A Lixeira.** Guarda os arquivos **excluídos**, permitindo **restaurá-los**. Três regras muito cobradas:

apertar a tecla **Delete** envia o arquivo para a **Lixeira**;

apertar **Shift mais Delete** **exclui permanentemente**, **sem passar** pela Lixeira;

e os arquivos excluídos de **pendrives**, cartões de memória e **pastas de rede** **não vão para a Lixeira**: são excluídos definitivamente.

**Copiar e mover arrastando.** Quando você **arrasta** um arquivo com o mouse:

para uma pasta **na mesma unidade**, o arquivo é **movido**;

para uma pasta **em outra unidade**, como um pendrive, o arquivo é **copiado**.

E é possível forçar o comportamento: arrastar segurando **Control** sempre **copia**; segurando **Shift** sempre **move**; e segurando **Alt** cria um **atalho**.

**Os atalhos de arquivo.** Um atalho é um pequeno arquivo que **aponta** para outro arquivo, pasta ou programa. **Excluir o atalho não exclui o arquivo original**. Mas, se o original for excluído ou movido, o atalho para de funcionar.

**Os nomes de arquivos.** No Windows, um nome de arquivo **não pode conter** estes caracteres: barra invertida, barra, dois-pontos, asterisco, ponto de interrogação, aspas, sinal de menor, sinal de maior e barra vertical. E o Windows **não diferencia** letras maiúsculas de minúsculas nos nomes: "Relatório" e "relatório" são o mesmo arquivo. O Linux, ao contrário, **diferencia**.

**Os atalhos de teclado do Windows.** São muito cobrados. Os principais:

**Control mais C**: copiar. **Control mais X**: recortar. **Control mais V**: colar.

**Control mais Z**: desfazer. **Control mais Y**: refazer.

**Control mais A**: selecionar tudo.

**F2**: renomear o arquivo selecionado.

**F5**: atualizar a janela.

**Alt mais Tab**: alternar entre as janelas abertas.

**Alt mais F4**: fechar a janela ou o programa ativo.

**Tecla Windows mais E**: abrir o Explorador de Arquivos.

**Tecla Windows mais D**: mostrar a área de trabalho.

**Tecla Windows mais L**: **bloquear** o computador. Um hábito de segurança importante no trabalho policial: bloqueie sempre a máquina ao se afastar.

**Tecla Windows mais I**: abrir as Configurações.

**Tecla Windows mais V**: abrir o **histórico da área de transferência**, com os últimos itens copiados.

**Tecla Windows mais Shift mais S**: capturar um **recorte da tela**.

**Control mais Shift mais Esc**: abrir o **Gerenciador de Tarefas**, para encerrar programas travados.

**Control mais Shift mais N**, no Explorador de Arquivos: criar uma **nova pasta**.

**A área de transferência.** É uma memória temporária que guarda o que você **copiou ou recortou**, até você **colar**. Ela fica na memória R A M, e por isso é **apagada** quando o computador é desligado.

**As contas de usuário.** O Windows tem contas de **administrador**, que podem instalar programas e alterar configurações de todo o sistema, e contas **padrão**, com permissões limitadas. O **Controle de Conta de Usuário** é aquela janela que pede confirmação antes de uma alteração importante, para evitar que programas maliciosos façam mudanças sem a sua autorização.

**Os recursos de segurança.** O **Windows Defender**, chamado Segurança do Windows, é o **antivírus** e o **firewall** integrados. E o **BitLocker** **criptografa** o disco inteiro, protegendo os dados se o computador for perdido ou roubado.

**O sistema de arquivos.** O Windows 10 usa, em regra, o **N T F S**, que permite **permissões** de acesso, **criptografia** e arquivos muito grandes. O sistema antigo, **F A T 32**, ainda usado em pendrives, tem um limite de **quatro gigabytes por arquivo**: por isso, às vezes não é possível copiar um vídeo grande para um pendrive.

---

## Aula 5. O Linux

**O que é.** Você já estudou no módulo 2: o Linux é um sistema operacional **livre**, cujo **kernel** foi criado por **Linus Torvalds**, distribuído em várias **distribuições**, como **Ubuntu**, **Debian** e **Fedora**. Ele tem **interfaces gráficas**, como o **Gnome** e o **K D E**, mas é muito usado pela **linha de comando**, no **terminal**.

**A estrutura de diretórios.** Tudo começa na **raiz**, representada pela **barra**. As pastas principais, que caem na prova, são:

**barra home**: as pastas **pessoais** dos usuários. Cada usuário tem a sua, como barra home barra marlon;

**barra root**: a pasta pessoal do **superusuário**, o administrador do sistema. Atenção: não confunda a pasta **barra root** com a **raiz**, que é só a **barra**;

**barra etc**: os arquivos de **configuração** do sistema;

**barra bin** e **barra sbin**: os **programas executáveis**, os comandos do sistema;

**barra dev**: os **dispositivos**. No Linux, até os dispositivos, como discos e pendrives, são representados como arquivos;

**barra tmp**: os arquivos **temporários**;

**barra var**: os arquivos **variáveis**, como os registros de atividade, chamados logs;

**barra boot**: os arquivos de **inicialização** do sistema;

**barra media** e **barra mnt**: os pontos de **montagem** de dispositivos, como pendrives e outros discos;

e **barra usr**: os programas e as bibliotecas instalados para os usuários.

Macete: "**home é a casa dos usuários; etc é a configuração; bin são os comandos; dev são os dispositivos; tmp é o temporário**".

**O superusuário.** No Linux, o administrador do sistema é o usuário **root**, que tem **poder total** sobre o sistema. Por segurança, não se trabalha o tempo todo como root. Para executar um comando com poderes de administrador, usa-se o comando **sudo** antes dele. E o comando **S U** permite trocar de usuário, inclusive para o root.

**Os comandos mais cobrados.** Lembre: no terminal, eles são escritos em **letras minúsculas**, e o Linux **diferencia maiúsculas de minúsculas**.

**L S**: **lista** os arquivos e pastas. Com a opção **traço L**, mostra os detalhes, como as permissões; com a opção **traço A**, mostra também os **arquivos ocultos**, que no Linux são aqueles cujo nome **começa com um ponto**.

**C D**: **muda de diretório**, ou seja, entra numa pasta. **C D ponto ponto** sobe para a pasta de cima.

**P W D**: **mostra o diretório atual**, ou seja, em que pasta você está.

**M K D I R**: **cria** uma pasta.

**R M D I R**: **remove** uma pasta **vazia**.

**R M**: **remove** arquivos. Com a opção **traço R**, remove pastas **com todo o conteúdo**, de forma **recursiva**. Cuidado: não há lixeira no terminal.

**C P**: **copia** arquivos.

**M V**: **move** arquivos, e também serve para **renomear**.

**C A T**: **mostra o conteúdo** de um arquivo de texto.

**T O U C H**: cria um arquivo vazio.

**G R E P**: **procura um texto** dentro de arquivos.

**P S** e **T O P**: mostram os **processos** em execução. **K I L L**: **encerra** um processo.

**M A N**: abre o **manual** de um comando.

Macete: "**L S lista, C D entra, P W D diz onde estou, M K D I R cria pasta, R M apaga, C P copia, M V move**".

---

## Aula 6. As permissões de arquivos e as contas de usuário

**As permissões no Linux.** É um tema muito cobrado. Cada arquivo e cada pasta têm permissões para **três tipos de usuários**:

o **dono** do arquivo, chamado em inglês de user;

o **grupo** a que o arquivo pertence;

e os **outros**, ou seja, todos os demais usuários.

E há **três tipos de permissão**:

**leitura**, representada pela letra **R**: permite **ler** o arquivo, ou **listar** o conteúdo da pasta;

**escrita**, representada pela letra **W**: permite **alterar** o arquivo, ou criar e apagar arquivos dentro da pasta;

**execução**, representada pela letra **X**: permite **executar** o arquivo como programa, ou **entrar** na pasta.

**Como as permissões aparecem.** Quando você usa o comando L S traço L, aparece uma sequência de dez caracteres. O **primeiro** indica o tipo: um **traço** para arquivo comum, e a letra **D** para diretório. Os **nove seguintes** são as permissões, em três blocos de três: primeiro do **dono**, depois do **grupo**, depois dos **outros**. Em cada bloco, aparece a letra quando há a permissão, e um traço quando não há.

Exemplo: R W X, R traço X, R traço X. O dono pode ler, escrever e executar; o grupo e os outros podem ler e executar, mas não escrever.

**A notação numérica.** As permissões também podem ser escritas com **números**. Cada permissão tem um valor: **leitura vale quatro**, **escrita vale dois** e **execução vale um**. Somam-se os valores de cada bloco.

Leitura, escrita e execução: quatro mais dois mais um, igual a **sete**.

Leitura e execução: quatro mais um, igual a **cinco**.

Leitura e escrita: quatro mais dois, igual a **seis**.

Só leitura: **quatro**.

Assim, a permissão **sete, cinco, cinco** quer dizer: o dono pode tudo; o grupo e os outros podem ler e executar. É a permissão comum de programas e pastas. A permissão **seis, quatro, quatro** quer dizer: o dono lê e escreve; o grupo e os outros só leem. É a permissão comum de documentos. E **sete, sete, sete** dá todas as permissões a todos, o que é **inseguro**.

Macete: "**leitura quatro, escrita dois, execução um; dono, grupo e outros**".

**Os comandos de permissão.** O comando **C H M O D** **altera as permissões**. Por exemplo, C H M O D sete cinco cinco, seguido do nome do arquivo. O comando **C H O W N** **altera o dono** do arquivo.

**As contas e os grupos.** Tanto o Windows quanto o Linux organizam os usuários em **grupos**, para facilitar a administração: em vez de dar permissão a cada pessoa, dá-se a permissão ao grupo. Exemplo: numa delegacia, o grupo "investigadores" pode ter acesso à pasta de relatórios, e o grupo "administrativo" não.

**O compartilhamento no Windows.** No Windows, é possível **compartilhar** pastas na rede, definindo quem pode acessá-las. As permissões do sistema de arquivos N T F S incluem, entre outras: **controle total**, **modificar**, **leitura e execução**, **listar o conteúdo da pasta**, **leitura** e **gravação**. Um princípio de segurança importante, que vale para os dois sistemas, é o do **menor privilégio**: cada usuário deve ter **apenas as permissões necessárias** para o seu trabalho, e nada mais.

---

## Revisão do módulo 3 de Informática

Vamos revisar em frases curtas.

Hardware é a parte física; software, a lógica.

C P U: unidade de controle, unidade lógica e aritmética e registradores.

R A M é volátil, de leitura e escrita: perde tudo ao desligar.

R O M é não volátil e guarda o firmware de inicialização, a B I O S ou U E F I.

Cache fica entre o processador e a R A M.

Do mais rápido ao mais lento: registrador, cache, R A M e disco.

Memória virtual usa o disco como R A M: arquivo de paginação no Windows, swap no Linux.

Um byte são oito bits. Quilo, mega, giga, tera.

Entrada: teclado, mouse, scanner, microfone. Saída: monitor, impressora, caixa de som. Mistos: tela de toque e multifuncional.

H D é magnético, com partes móveis. S S D é flash, sem partes móveis, mais rápido.

C D, setecentos megabytes; D V D, quatro vírgula sete gigabytes; Blu-ray, vinte e cinco.

U S B é plug and play.

Sistema operacional fica entre o usuário e o hardware; o núcleo é o kernel.

Windows e Linux são multitarefa e multiusuário.

A extensão vem depois do último ponto. Docx, Word; odt, LibreOffice; exe, executável perigoso.

Windows usa barra invertida e letra de unidade; Linux usa barra normal e começa na raiz.

Um ponto é a pasta atual; dois pontos, a pasta de cima; til, a pasta pessoal no Linux.

Delete vai para a Lixeira; Shift mais Delete apaga de vez.

Pendrive e rede não têm Lixeira.

Arrastar na mesma unidade move; para outra unidade, copia.

Control arrastando copia; Shift move; Alt cria atalho.

Excluir o atalho não exclui o arquivo.

Windows não diferencia maiúsculas; Linux diferencia.

Windows mais L bloqueia. Windows mais E abre o Explorador. Windows mais D mostra a área de trabalho.

Control mais Shift mais Esc abre o Gerenciador de Tarefas.

F2 renomeia; Alt mais F4 fecha; Alt mais Tab alterna.

N T F S tem permissões e criptografia; F A T 32 limita arquivos a quatro gigabytes.

Barra home é a casa dos usuários; barra root, a casa do administrador; barra etc, configurações.

Root é o superusuário; sudo executa como administrador.

L S lista, C D entra, P W D mostra onde estou, M K D I R cria pasta, R M apaga, C P copia, M V move e renomeia.

Arquivo oculto no Linux começa com ponto.

Permissões: dono, grupo e outros. Leitura quatro, escrita dois, execução um.

Sete, cinco, cinco: dono pode tudo, os demais leem e executam.

C H M O D altera as permissões; C H O W N altera o dono.

Princípio do menor privilégio: só as permissões necessárias.

---

## Treino 1. Memórias

Sobre as memórias do computador, assinale a afirmativa correta.

Letra A: A memória R A M é não volátil e mantém os dados mesmo com o computador desligado.

Letra B: A memória R O M é volátil e armazena os documentos abertos pelo usuário.

Letra C: A memória R A M é volátil e armazena os programas e os dados em uso, perdendo o conteúdo quando o computador é desligado.

Letra D: A memória cache é mais lenta que a memória R A M.

Letra E: Os registradores ficam no disco rígido.

Pense na sua resposta.

**A explicação.** A memória R A M é volátil: guarda o que está em uso e perde tudo ao desligar. A R O M é não volátil e guarda o firmware de inicialização. A cache é mais rápida que a R A M. E os registradores ficam dentro do processador.

**Resposta: letra C.**

---

## Treino 2. Windows 10

No Windows 10, um usuário seleciona um arquivo que está em um pendrive e pressiona a tecla Delete. Sobre o resultado, é correto afirmar que

Letra A: o arquivo é enviado para a Lixeira e pode ser restaurado.

Letra B: o arquivo é excluído definitivamente, pois arquivos excluídos de unidades removíveis não vão para a Lixeira.

Letra C: o arquivo é movido para a área de trabalho.

Letra D: o arquivo é copiado para o disco rígido.

Letra E: nada acontece, pois arquivos de pendrive não podem ser excluídos.

Pense na sua resposta.

**A explicação.** Os arquivos excluídos de pendrives, cartões de memória e pastas de rede não vão para a Lixeira: são excluídos definitivamente. Só os arquivos das unidades internas vão para a Lixeira quando se usa a tecla Delete.

**Resposta: letra B.**

---

## Treino 3. Comandos do Linux

No terminal do Linux, o comando utilizado para exibir o caminho completo do diretório em que o usuário se encontra é

Letra A: L S.

Letra B: C D.

Letra C: P W D.

Letra D: M K D I R.

Letra E: R M.

Pense na sua resposta.

**A explicação.** O comando P W D mostra o diretório atual. L S lista o conteúdo; C D muda de diretório; M K D I R cria uma pasta; e R M remove arquivos.

**Resposta: letra C.**

---

## Treino 4. Permissões

No Linux, um arquivo recebeu a permissão seis, quatro, quatro. Isso significa que

Letra A: todos os usuários podem ler, escrever e executar o arquivo.

Letra B: o dono pode ler e escrever, e o grupo e os outros podem apenas ler.

Letra C: o dono pode apenas ler, e o grupo e os outros podem ler e escrever.

Letra D: ninguém pode ler o arquivo.

Letra E: o dono pode ler, escrever e executar, e os demais não têm nenhuma permissão.

Pense na sua resposta.

**A explicação.** Seis é leitura, quatro, mais escrita, dois. Quatro é só leitura. Então o dono, que é o primeiro número, pode ler e escrever; o grupo e os outros, que são o segundo e o terceiro números, só podem ler.

**Resposta: letra B.**

---

## Encerramento do módulo 3 de Informática

Parabéns! Você estudou o computador por dentro e os dois sistemas operacionais do edital. Repita em voz alta: R A M é volátil; registrador, cache, R A M e disco; Shift mais Delete apaga de vez; Windows mais L bloqueia; L S lista, P W D mostra onde estou; leitura quatro, escrita dois, execução um.

No próximo módulo de Informática, vamos estudar o correio eletrônico, com o Outlook e o webmail, e o pacote de escritório: Word e Writer, Excel e Calc, PowerPoint e Impress.
