# Curso, módulo 2. Informática: segurança da informação, pragas virtuais, golpes, backup, criptografia, certificação digital e software livre

Olá! No primeiro módulo de Informática, você estudou redes, protocolos e o Marco Civil da Internet. Agora vamos ao tema que a banca mais gosta de cobrar e que mais se aproxima do seu futuro trabalho: a **segurança da informação**.

Na prova de 2025, a questão 22 foi sobre golpes na internet e a 23 sobre criptografia. E, como investigador, você vai lidar com crimes cibernéticos, celulares apreendidos, golpes do falso parente e provas digitais. Entender como as pragas virtuais e a criptografia funcionam vai ajudar na prova e na carreira.

---

## Aula 1. Os princípios da segurança da informação

**A ideia central.** Segurança da informação é o conjunto de medidas para **proteger as informações** contra acessos indevidos, alterações e perdas. A doutrina organiza essa proteção em **princípios**, e a banca cobra cada um pelo nome.

**Os três princípios básicos.** Formam a chamada **tríade** da segurança.

**Confidencialidade**: a informação só pode ser acessada por **quem tem autorização**. Exemplo: um inquérito sigiloso só pode ser lido pelas pessoas autorizadas. Quando um hacker lê os seus e-mails, quem foi violada foi a confidencialidade.

**Integridade**: a informação **não pode ser alterada** indevidamente. Ela deve chegar exatamente como saiu. Exemplo: um laudo pericial não pode ter o texto modificado depois de assinado. Quando alguém adultera um documento, a integridade foi violada.

**Disponibilidade**: a informação deve estar **acessível quando for necessária**, para quem tem autorização. Exemplo: o sistema da delegacia precisa estar no ar durante o plantão. Quando um ataque derruba um site, a disponibilidade foi violada.

**Os princípios complementares.**

**Autenticidade**: garante que a informação vem de **quem diz ter enviado**. Exemplo: ter certeza de que o ofício foi mesmo enviado pelo delegado, e não por alguém se passando por ele.

**Irretratabilidade**, também chamada **não repúdio**: o autor **não pode negar** que praticou o ato. Exemplo: quem assina digitalmente um documento não pode depois dizer que não assinou.

Macete: **dica**, de **d**isponibilidade, **i**ntegridade, **c**onfidencialidade e **a**utenticidade. E some o não repúdio.

**Uma dica para as questões.** Leia a situação e pergunte: o que foi atingido? Alguém **leu** o que não devia? Confidencialidade. Alguém **mudou** o conteúdo? Integridade. O sistema **ficou fora do ar**? Disponibilidade. Alguém **se passou** por outra pessoa? Autenticidade. Alguém **negou** que fez? Não repúdio.

**A Lei Geral de Proteção de Dados.** A **Lei 13709, de 2018**, conhecida como **L G P D**, regula o tratamento de **dados pessoais** por pessoas e empresas, públicas ou privadas. Ela diferencia o **dado pessoal**, que é qualquer informação relacionada a uma pessoa identificada ou identificável, como nome, C P F e endereço, do **dado pessoal sensível**, que trata de origem racial ou étnica, convicção religiosa, opinião política, filiação sindical, dados de saúde, vida sexual, dados genéticos ou biométricos. Os dados sensíveis têm proteção reforçada. A fiscalização cabe à **Autoridade Nacional de Proteção de Dados**.

Um ponto importante para o policial: a **L G P D não se aplica** ao tratamento de dados feito para fins exclusivos de **segurança pública**, **defesa nacional**, **segurança do Estado** e **atividades de investigação e repressão de infrações penais**. Esses casos devem ser regulados por lei específica.

---

## Aula 2. As pragas virtuais

**O conceito.** O nome técnico é **malware**, uma junção das palavras inglesas para "software malicioso". São programas feitos para causar dano, roubar informações ou tomar o controle de um computador. A banca cobra a diferença entre cada tipo, então preste atenção às palavras-chave.

**Vírus.** É um programa que **se anexa a outro arquivo** ou programa, chamado **hospedeiro**, e **depende da execução** desse hospedeiro para agir e se espalhar. Sem que alguém abra o arquivo infectado, o vírus não age. Palavras-chave: **hospedeiro** e **precisa ser executado**. Exemplo: um anexo de e-mail infectado que só causa dano quando a pessoa o abre.

**Worm**, que quer dizer verme. É um programa que **se propaga sozinho** pela rede, explorando **vulnerabilidades**, **sem precisar de hospedeiro** e **sem precisar ser executado** pelo usuário. Ele cria **cópias de si mesmo** e costuma **consumir muitos recursos** da rede e do computador, deixando tudo lento. Palavras-chave: **autorreplicação** e **propagação automática**.

A diferença que mais cai: o **vírus precisa de hospedeiro e de execução**; o **worm não precisa de nenhum dos dois**.

**Cavalo de troia**, ou trojan. É um programa que **parece útil ou inofensivo**, como um jogo, um protetor de tela ou um falso atualizador, mas que, escondido, executa funções maliciosas. O nome vem da história do cavalo de madeira que os gregos deram de presente a Troia, com soldados escondidos dentro. O cavalo de troia **não se replica sozinho**: depende de o usuário instalá-lo. Palavra-chave: **disfarce**.

**Spyware**, que quer dizer programa espião. **Monitora** as atividades do usuário e **envia as informações** a terceiros. Tem subtipos:

**keylogger**: captura as **teclas digitadas**, inclusive senhas;

**screenlogger**: captura **imagens da tela**, inclusive a posição do clique do mouse, criado para burlar os teclados virtuais dos bancos;

**adware**: exibe **propagandas** indesejadas, e muitas vezes coleta dados de navegação.

**Backdoor**, que quer dizer porta dos fundos. É um programa que **abre uma entrada** no computador para o invasor **voltar** quando quiser, sem precisar invadir de novo.

**Rootkit**. É um conjunto de ferramentas que serve para **esconder** a presença do invasor e de outros códigos maliciosos, dificultando a sua detecção pelo antivírus. Palavra-chave: **ocultação**.

**Bot e botnet**. O **bot** é um programa que permite que o invasor **controle o computador remotamente**, transformando-o num **zumbi**. A **botnet** é uma **rede de computadores zumbis**, que o invasor usa em conjunto, por exemplo, para enviar spam em massa ou para fazer ataques de negação de serviço.

**Ransomware**, que vem da palavra inglesa para resgate. **Sequestra os dados**: ele **criptografa os arquivos** da vítima e exige um **resgate**, normalmente em **criptomoeda**, para entregar a chave que os libera. Atinge hospitais, prefeituras e órgãos públicos. A melhor defesa é ter **backup atualizado e guardado separado**. Palavras-chave: **criptografa e pede resgate**.

Macete geral: **vírus, hospedeiro; worm, sozinho pela rede; troia, disfarce; spyware, espiona; backdoor, porta de volta; rootkit, esconde; bot, zumbi; ransomware, resgate**.

---

## Aula 3. Os golpes e os ataques

**Engenharia social.** É a técnica de **manipular pessoas** para que entreguem informações ou façam algo que as prejudique, explorando a **confiança**, a **curiosidade**, o **medo** ou a **pressa**. Não é um ataque à máquina, mas **ao ser humano**. Por isso, diz-se que o elo mais fraco da segurança é o usuário. A maior parte dos golpes abaixo usa engenharia social.

**Phishing**, do inglês para "pescaria". É o golpe em que o criminoso se faz passar por uma **instituição confiável**, como um banco, a Receita Federal ou uma loja, enviando **mensagens falsas** com **links** para **páginas falsas**, onde a vítima digita os seus dados. A vítima é "pescada". Palavras-chave: **mensagem falsa e site falso**.

Há variações: o **smishing**, por mensagem de texto no celular; o **vishing**, por ligação de voz, como a falsa central do banco; e o **spear phishing**, ou phishing direcionado, que mira uma **pessoa ou empresa específica**, com informações personalizadas para parecer mais convincente.

**Pharming**. Aqui a vítima digita o endereço **correto** do site, mas é **redirecionada** para um site **falso**, porque o criminoso **alterou o funcionamento do D N S**, o sistema que traduz nomes em endereços, que você estudou no módulo 1. Por isso também se chama **envenenamento de D N S**. A diferença para o phishing: no **phishing**, a vítima **clica num link falso**; no **pharming**, a vítima **digita o endereço certo** e mesmo assim cai no site falso.

**O golpe do falso parente e do WhatsApp clonado.** O criminoso usa a foto de um parente da vítima, ou **toma o controle da conta de aplicativo** de mensagens de alguém, geralmente obtendo o **código de verificação** por engenharia social, e pede dinheiro aos contatos, alegando uma urgência. A principal defesa é ativar a **verificação em duas etapas** no aplicativo e **nunca informar códigos** recebidos por mensagem.

**Hoax**, ou boato. É uma **mensagem falsa**, com conteúdo alarmante, que pede para ser **repassada** a todos os contatos, como falsas campanhas e falsos alertas. Serve para espalhar desinformação e, às vezes, links maliciosos.

**Negação de serviço.** O nome técnico é **D o S**, do inglês para negação de serviço, e, quando vem de muitas máquinas ao mesmo tempo, **D D o S**, negação de serviço **distribuída**, normalmente usando uma **botnet**. O ataque **sobrecarrega** um servidor com um volume enorme de acessos, até que ele **saia do ar**. O princípio violado é a **disponibilidade**. Atenção: o ataque de negação de serviço **não invade** nem rouba dados; ele **derruba** o serviço.

**Força bruta.** O criminoso tenta **adivinhar a senha** testando **todas as combinações** possíveis, ou listas de senhas comuns, por tentativa e erro. A defesa é usar senhas longas e bloquear o acesso depois de algumas tentativas erradas.

**Sniffing**, do inglês para farejar. É a **interceptação do tráfego** de rede para capturar dados, como senhas que trafegam **sem criptografia**. Por isso é perigoso usar redes Wi-Fi públicas para acessar contas sem a proteção do H T T P S.

**Spoofing**, do inglês para falsificação. É a **falsificação da origem** de uma comunicação, como forjar o **remetente de um e-mail** ou o endereço I P de um computador, para parecer que a mensagem vem de outra pessoa. Viola a **autenticidade**.

---

## Aula 4. As ferramentas de proteção e o backup

**Antivírus.** Detecta e remove códigos maliciosos, comparando os arquivos com uma **base de assinaturas** de pragas conhecidas e analisando comportamentos suspeitos. Precisa ser **atualizado** com frequência, porque novas pragas surgem todos os dias.

**Firewall**, que quer dizer parede corta-fogo. **Filtra o tráfego** de rede, **permitindo ou bloqueando** conexões de acordo com **regras** definidas. Ele controla **o que entra e o que sai** do computador ou da rede. Atenção, porque a banca adora esta pegadinha: o **firewall não é antivírus**. Ele **não remove** pragas que já estão no computador, e **não analisa** o conteúdo dos arquivos em busca de vírus. Ele controla **conexões**.

**Sistemas de detecção e de prevenção de intrusão.** O sistema de **detecção** **monitora** a rede e **alerta** sobre atividades suspeitas. O sistema de **prevenção** vai além: **detecta e bloqueia** automaticamente. Macete: **detecção avisa; prevenção age**.

**V P N**, rede privada virtual. Cria um **túnel criptografado** através da internet, permitindo acessar uma rede privada, como a rede interna da polícia, de forma segura a partir de outro local.

**Autenticação multifator.** É a verificação da identidade usando **dois ou mais fatores** de categorias **diferentes**:

**algo que você sabe**: senha, P I N, resposta secreta;

**algo que você tem**: celular que recebe um código, token, cartão;

**algo que você é**: biometria, como impressão digital, reconhecimento facial ou de íris.

Atenção: **duas senhas** não são autenticação em dois fatores, porque são do **mesmo tipo**. É preciso combinar categorias diferentes, como a **senha** e o **código no celular**.

**Senhas fortes.** Devem ser **longas**, misturar **letras maiúsculas e minúsculas, números e símbolos**, não usar dados pessoais, como data de nascimento, e **não ser reutilizadas** em vários sites. Um gerenciador de senhas ajuda a guardar senhas diferentes para cada serviço.

**O backup**, ou cópia de segurança. É a principal defesa contra a perda de dados e contra o ransomware. A banca cobra muito os **três tipos**.

**Backup completo**, ou normal: copia **todos os arquivos** selecionados e **marca** todos como copiados. É o mais demorado para fazer e o mais simples para restaurar.

**Backup incremental**: copia **apenas os arquivos criados ou alterados desde o último backup**, **seja ele completo ou incremental**, e **marca** os arquivos como copiados. É o **mais rápido** para fazer e o que ocupa **menos espaço**. Mas, para **restaurar**, é preciso o **último completo e todos os incrementais** feitos depois dele, na ordem.

**Backup diferencial**: copia **todos os arquivos criados ou alterados desde o último backup completo**, e **não marca** os arquivos como copiados. Por isso, a cada dia, ele fica **maior**, porque acumula as alterações. Mas, para **restaurar**, basta o **último completo e o último diferencial**.

Macete: **incremental, desde o último de qualquer tipo; diferencial, desde o último completo**. Ou ainda: o incremental é **rápido para fazer e lento para restaurar**; o diferencial é **lento para fazer e rápido para restaurar**.

**A regra três, dois, um.** É uma boa prática de backup: ter **três cópias** dos dados, em **dois tipos diferentes** de mídia, sendo **uma delas fora do local**, como em outro prédio ou na nuvem. Assim, um incêndio ou um ransomware não destrói todas as cópias.

---

## Aula 5. A criptografia, o hash e a certificação digital

**O que é criptografia.** É a técnica de **transformar uma informação legível** em um **texto ilegível**, chamado texto cifrado, usando um **algoritmo** e uma **chave**. Só quem tem a chave correta consegue **decifrar** e ler de novo. A criptografia protege principalmente a **confidencialidade**.

**A criptografia simétrica**, ou de chave secreta. Usa **uma única chave**, a **mesma** para cifrar e para decifrar. É **rápida**, por isso é usada para grandes volumes de dados. O seu problema é a **distribuição da chave**: como enviar a chave secreta ao destinatário sem que alguém a intercepte? Exemplo de algoritmo: o **A E S**.

**A criptografia assimétrica**, ou de chave pública. Usa **um par de chaves** diferentes, ligadas matematicamente: uma **chave pública**, que pode ser divulgada para qualquer pessoa, e uma **chave privada**, que fica **só com o dono** e nunca é compartilhada. O que uma chave cifra, **só a outra** decifra. É **mais lenta**, mas resolve o problema da distribuição de chaves. Exemplo de algoritmo: o **R S A**.

**Como garantir a confidencialidade com a assimétrica.** Se Ana quer mandar uma mensagem secreta para Bruno, ela **cifra com a chave pública de Bruno**. Só a **chave privada de Bruno** pode decifrar. Assim, só Bruno lê.

**A assinatura digital.** Funciona ao contrário. Ana quer provar que **foi ela** quem enviou o documento. Ela **assina com a sua própria chave privada**. Qualquer pessoa pode **verificar a assinatura** com a **chave pública de Ana**. Como só Ana tem a sua chave privada, fica provado que foi ela.

Guarde as regras:

para **sigilo**, usa-se a **chave pública do destinatário**;

para **assinar**, usa-se a **chave privada do remetente**.

E a assinatura digital garante **autenticidade**, **integridade** e **não repúdio**. Mas atenção, porque a banca adora esta pegadinha: a assinatura digital, **sozinha**, **não garante a confidencialidade**. O documento assinado pode ser lido por qualquer um. Se quiser sigilo, é preciso também **cifrar**.

**O hash.** É uma **função de resumo**: transforma um arquivo de qualquer tamanho em um **código de tamanho fixo**, como uma **impressão digital** do arquivo. Tem três características: é **de mão única**, ou seja, não é possível reconstruir o arquivo a partir do hash; **qualquer alteração mínima** no arquivo, até uma vírgula, gera um hash **completamente diferente**; e o mesmo arquivo sempre gera o **mesmo hash**. Exemplo de algoritmo: o **S H A 256**. O hash garante a **integridade**.

**O hash na investigação policial.** Esta é uma aplicação muito importante para o seu trabalho. Quando a perícia faz a **cópia** de um celular ou de um disco rígido apreendido, ela calcula o **hash** do material. Depois, a qualquer momento, basta calcular o hash de novo: se der o mesmo resultado, fica provado que **nada foi alterado**. É assim que se preserva a **cadeia de custódia** da prova digital, um tema que você vai estudar no próximo módulo de Processo Penal.

**O certificado digital.** É um **documento eletrônico** que **vincula uma chave pública** a uma **pessoa ou empresa**, como uma **carteira de identidade digital**. Ele é emitido por uma **Autoridade Certificadora**, uma entidade de confiança que confirma a identidade do titular. Contém o nome do titular, a sua chave pública, a validade e a assinatura da Autoridade Certificadora.

**A I C P Brasil.** É a **Infraestrutura de Chaves Públicas Brasileira**, criada pela Medida Provisória 2200-2, de 2001. Ela garante a **validade jurídica** dos documentos assinados digitalmente com certificados emitidos dentro da sua estrutura: eles têm o mesmo valor de um documento assinado à mão. No topo da hierarquia está a **Autoridade Certificadora Raiz**, que é o **Instituto Nacional de Tecnologia da Informação**.

Os certificados mais comuns são o **A1**, que fica **gravado no próprio computador**, como um arquivo, e tem validade menor; e o **A3**, que fica gravado num **cartão inteligente** ou **token**, um dispositivo físico, e é mais seguro.

---

## Aula 6. O software livre

**O conceito.** Software livre é aquele que respeita a **liberdade** do usuário. A definição foi criada pela **Free Software Foundation**, fundada por **Richard Stallman**. Atenção à confusão mais comum: **livre não quer dizer gratuito**. A palavra inglesa "free" tem os dois sentidos, mas aqui significa **liberdade**. Um software livre pode ser vendido.

**As quatro liberdades.** São numeradas a partir do zero, como os programadores costumam contar:

**liberdade zero**: **executar** o programa, para **qualquer propósito**;

**liberdade um**: **estudar** como o programa funciona e **adaptá-lo** às suas necessidades. Para isso, o **acesso ao código-fonte** é um **pré-requisito**;

**liberdade dois**: **redistribuir cópias**, para ajudar outras pessoas;

**liberdade três**: **aperfeiçoar** o programa e **distribuir as suas melhorias** ao público, para beneficiar toda a comunidade. Aqui também o acesso ao código-fonte é pré-requisito.

Macete: "**usar, estudar, copiar e melhorar**".

**O copyleft e a G P L.** A licença mais famosa de software livre é a **G P L**, Licença Pública Geral. Ela adota o **copyleft**, um trocadilho com copyright: quem redistribuir o programa, modificado ou não, deve manter **as mesmas liberdades**, ou seja, a versão derivada **também tem de ser livre**. Ninguém pode pegar um software livre, modificá-lo e transformá-lo em software fechado.

**Os outros tipos de software.**

**Software proprietário**: o código-fonte é **fechado**, e o uso depende de **licença** do fabricante, que impõe restrições. Exemplo: o Microsoft Windows e o Microsoft Office.

**Freeware**: é **gratuito**, mas **não é livre**, porque o código-fonte é fechado e não se pode modificá-lo.

**Shareware**: é distribuído gratuitamente para **teste**, por tempo limitado ou com funções limitadas. Depois, é preciso pagar.

**Código aberto**, ou open source: movimento parecido com o do software livre, mais focado nas **vantagens técnicas** do código aberto do que na filosofia da liberdade. Na prática, a maioria dos programas de código aberto também é livre.

**Domínio público**: software sem direitos autorais, que qualquer um pode usar livremente.

**Os exemplos que caem.** O **Linux** é o exemplo clássico. O seu **núcleo**, chamado **kernel**, foi criado por **Linus Torvalds**, em 1991. Em volta do kernel, várias organizações montam as **distribuições**, como o **Ubuntu**, o **Debian**, o **Fedora** e o **Linux Mint**. Também são livres o **LibreOffice**, pacote de escritório que concorre com o Microsoft Office, o navegador **Firefox**, e o próprio **Android**, que é baseado no kernel Linux, embora muitos aplicativos do Google que vêm nele sejam proprietários.

E uma curiosidade que se liga a você: a plataforma em que você está estudando agora usa apenas tecnologias livres e de código aberto, e a voz que você ouve é gerada por um sintetizador de voz livre.

---

## Revisão do módulo 2 de Informática

Vamos revisar em frases curtas.

Confidencialidade: só quem pode, lê.

Integridade: ninguém altera.

Disponibilidade: está acessível quando precisa.

Autenticidade: vem de quem diz ter enviado.

Não repúdio: o autor não pode negar.

Macete: dica, mais o não repúdio.

A L G P D não se aplica à segurança pública e à investigação de infrações penais.

Vírus precisa de hospedeiro e de execução.

Worm se espalha sozinho pela rede, sem hospedeiro.

Cavalo de troia se disfarça de programa útil.

Keylogger captura teclas; screenlogger captura a tela.

Backdoor abre a porta de volta; rootkit esconde o invasor.

Bot transforma o computador em zumbi; botnet é a rede de zumbis.

Ransomware criptografa os dados e pede resgate.

Engenharia social ataca o ser humano.

Phishing: mensagem falsa com link para site falso.

Pharming: endereço correto, mas o D N S foi envenenado.

Spear phishing é direcionado a um alvo específico.

Negação de serviço derruba o serviço e ataca a disponibilidade.

Spoofing falsifica a origem e ataca a autenticidade.

Firewall filtra conexões, mas não é antivírus.

Detecção avisa; prevenção age.

Autenticação multifator: o que você sabe, o que você tem e o que você é.

Backup completo copia tudo.

Incremental: desde o último backup de qualquer tipo. Rápido para fazer, lento para restaurar.

Diferencial: desde o último completo. Lento para fazer, rápido para restaurar.

Regra três, dois, um.

Simétrica: uma chave, rápida, com problema de distribuição.

Assimétrica: chave pública e chave privada.

Sigilo: chave pública do destinatário.

Assinatura: chave privada do remetente.

Assinatura digital garante autenticidade, integridade e não repúdio, mas não confidencialidade.

Hash é a impressão digital do arquivo e garante a integridade.

A perícia usa o hash para preservar a cadeia de custódia digital.

Certificado digital vincula uma chave pública a uma pessoa, emitido por Autoridade Certificadora.

A I C P Brasil dá validade jurídica; a raiz é o Instituto Nacional de Tecnologia da Informação.

A1 no computador; A3 em cartão ou token.

Software livre não é grátis: é liberdade.

Quatro liberdades: usar, estudar, copiar e melhorar.

Código-fonte é pré-requisito para estudar e melhorar.

G P L e copyleft: o derivado também deve ser livre.

Freeware é grátis, mas não é livre.

Linux, criado por Linus Torvalds; LibreOffice e Firefox são livres.

---

## Treino 1. Pragas virtuais

Um programa malicioso se espalhou automaticamente pelos computadores de uma rede, explorando uma falha de segurança do sistema operacional, sem que nenhum usuário abrisse arquivos, e deixou a rede extremamente lenta. Trata-se de um

Letra A: vírus.

Letra B: cavalo de troia.

Letra C: worm.

Letra D: keylogger.

Letra E: hoax.

Pense na sua resposta.

**Resposta: letra C: worm.**

**Por quê.** O worm se propaga sozinho pela rede, explorando vulnerabilidades, sem precisar de hospedeiro nem da execução pelo usuário, e costuma consumir muitos recursos, deixando a rede lenta. O vírus depende de um hospedeiro e de ser executado. O cavalo de troia depende de o usuário instalá-lo.

---

## Treino 2. Golpes

Um usuário digitou corretamente, no navegador, o endereço do site do seu banco, mas foi direcionado a uma página falsa, idêntica à verdadeira, onde digitou a sua senha. Esse golpe, que envolve a alteração do sistema de resolução de nomes, é chamado de

Letra A: phishing.

Letra B: pharming.

Letra C: spoofing.

Letra D: negação de serviço.

Letra E: força bruta.

Pense na sua resposta.

**Resposta: letra B: pharming.**

**Por quê.** No pharming, a vítima digita o endereço correto, mas é redirecionada para um site falso porque o D N S foi alterado, ou envenenado. No phishing, a vítima clica em um link falso recebido por mensagem.

---

## Treino 3. Backup

Uma empresa faz backup completo aos domingos e backup diferencial nos demais dias. Na quinta-feira, todos os dados foram perdidos. Para a restauração completa, serão necessários

Letra A: apenas o backup diferencial de quarta-feira.

Letra B: o backup completo de domingo e todos os diferenciais de segunda a quarta-feira.

Letra C: o backup completo de domingo e o último backup diferencial, de quarta-feira.

Letra D: apenas o backup completo de domingo.

Letra E: o backup diferencial de segunda-feira e o de quarta-feira.

Pense na sua resposta.

**Resposta: letra C: o backup completo de domingo e o último backup diferencial, de quarta-feira.**

**Por quê.** O backup diferencial copia tudo o que mudou desde o último backup completo. Por isso, o diferencial de quarta já contém todas as alterações de segunda, terça e quarta. Basta o completo de domingo mais o último diferencial. Se fossem backups incrementais, seriam necessários o completo e todos os incrementais.

---

## Treino 4. Criptografia e assinatura digital

Sobre a assinatura digital com criptografia assimétrica, é correto afirmar que

Letra A: o remetente assina o documento com a chave pública do destinatário.

Letra B: a assinatura digital garante, por si só, a confidencialidade do documento.

Letra C: o remetente assina o documento com a sua chave privada, e a assinatura é verificada com a chave pública do remetente, garantindo autenticidade, integridade e não repúdio.

Letra D: a criptografia assimétrica utiliza uma única chave, compartilhada entre remetente e destinatário.

Letra E: a assinatura digital dispensa o uso de funções de hash.

Pense na sua resposta.

**Resposta: letra C: o remetente assina o documento com a sua chave privada, e a assinatura é verificada com a chave pública do remetente, garantindo autenticidade, integridade e não repúdio.**

**Por quê.** Na assinatura digital, o remetente usa a sua própria chave privada, e qualquer pessoa verifica com a chave pública dele. Ela garante autenticidade, integridade e não repúdio, mas não garante sigilo. A criptografia assimétrica usa um par de chaves, e a assinatura digital usa o hash para resumir o documento antes de assiná-lo.

---

## Encerramento do módulo 2 de Informática

Parabéns! Agora você entende como os criminosos atacam e como a informação é protegida. Repita em voz alta: dica, mais o não repúdio; vírus precisa de hospedeiro, worm vai sozinho; sigilo com a pública do destinatário, assinatura com a privada do remetente; software livre não é grátis, é liberdade.

No próximo módulo de Informática, vamos estudar os sistemas operacionais Windows e Linux, e os aplicativos de escritório, com editores de texto e planilhas eletrônicas, que a banca cobra com muitas questões práticas.
