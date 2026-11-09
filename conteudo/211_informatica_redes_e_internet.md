# Curso, módulo 1. Informática: redes, internet, navegador e Marco Civil

Olá! Começamos a Informática, que vale 8 questões na prova, o mesmo peso de quase duas matérias de Direito juntas. O edital é extenso e técnico, mas a F G V cobra sempre os mesmos núcleos. Na prova de 2025, as questões 17 e 18 foram de redes, a 22 foi de golpes na internet e a 23 de criptografia.

Neste primeiro módulo, vamos estudar as redes de computadores, os endereços I P, os equipamentos de rede, os protocolos da internet, as U R Ls e os domínios, o navegador Google Chrome e o Marco Civil da Internet.

Uma dica para o estudo pelo ouvido: em Informática, muita coisa é sigla. Repita as siglas em voz alta, com o significado, até elas ficarem naturais.

---

## Aula 1. O que é uma rede e como ela se organiza

**O conceito.** Uma rede de computadores é um conjunto de dispositivos ligados entre si para trocar dados e compartilhar recursos, como arquivos, impressoras e acesso à internet.

**Classificação pelo tamanho.** A banca cobra as siglas em inglês.

**L A N**, rede local: cobre uma área pequena, como uma casa, uma delegacia ou um prédio.

**M A N**, rede metropolitana: cobre uma cidade ou uma região metropolitana.

**W A N**, rede de longa distância: cobre países e continentes. A internet é a maior W A N do mundo.

Existe também a **P A N**, rede pessoal, de alcance muito curto, como a ligação entre o celular e um fone Bluetooth.

**Internet, intranet e extranet.** A **internet** é a rede mundial, pública, aberta. A **intranet** é uma rede **privada**, de uma organização, que usa **as mesmas tecnologias da internet**, como navegador e páginas web, mas com acesso restrito aos funcionários. O sistema interno da Polícia Civil, acessado só por policiais, é uma intranet. A **extranet** é uma parte da intranet aberta a parceiros externos autorizados, como fornecedores ou outros órgãos.

Pegadinha frequente: a intranet **não precisa** estar desligada da internet, e **usa sim** os protocolos da internet. O que a define é o acesso restrito.

**Topologias.** É o desenho de como os computadores se ligam.

**Barramento**: todos ligados a um único cabo central. Se o cabo rompe, a rede para.

**Anel**: cada computador ligado ao próximo, formando um círculo. Os dados circulam num sentido.

**Estrela**: todos ligados a um equipamento central, como um switch. É a mais usada hoje. Se um cabo falha, só aquele computador sai da rede; se o equipamento central falha, todos param.

**Malha**: vários caminhos possíveis entre os pontos. Muito resistente a falhas. A internet funciona como uma grande malha.

**Redes com fio e sem fio.** A questão 18 de 2025 pediu a comparação. As redes **com fio**, chamadas **Ethernet**, normalmente com **cabo de par trançado**, oferecem **mais estabilidade, mais velocidade e mais segurança física**, porque para espionar é preciso acesso ao cabo. As redes **sem fio**, o **Wi-Fi**, priorizam **mobilidade e facilidade de instalação**, mas sofrem mais **interferência**, têm **latência maior**, ou seja, mais atraso, e exigem cuidado com segurança. O Wi-Fi opera principalmente nas frequências de **2,4 e 5 gigahertz**, e nas versões mais novas também em 6 gigahertz. A frequência de 2,4 alcança mais longe, mas é mais lenta e congestionada; a de 5 é mais rápida e de menor alcance.

Para proteger o Wi-Fi, usa-se criptografia. O padrão **W E P** é antigo e inseguro. O **W P A 2** é o mais comum, e o **W P A 3** é o mais moderno e seguro.

---

## Aula 2. Endereços I P, máscara, gateway, D N S e D H C P

**O protocolo T C P I P.** É o conjunto de regras que faz a internet funcionar. O **I P**, protocolo de internet, cuida do **endereçamento** e do **roteamento**: diz para onde cada pacote de dados vai. O **T C P**, protocolo de controle de transmissão, garante que os dados cheguem **completos e na ordem certa**: é confiável, confirma o recebimento e reenvia o que se perdeu. Existe também o **U D P**, mais rápido e sem garantia de entrega, usado em vídeo ao vivo, chamadas de voz e jogos, onde é melhor perder um pedacinho do que atrasar.

**O endereço I P versão 4.** É o número que identifica cada dispositivo na rede. Tem **32 bits**, escritos como **quatro números de 0 a 255**, separados por pontos. Exemplo: 192 ponto 168 ponto 0 ponto 1. Cada um desses quatro números é chamado de octeto, porque tem 8 bits.

O I P versão 4 permite cerca de 4 bilhões de endereços, o que se tornou **insuficiente** com o crescimento da internet.

**O endereço I P versão 6.** Tem **128 bits**, escritos em **números hexadecimais**, que usam os algarismos de 0 a 9 e as letras de A a F, em oito grupos separados por dois-pontos. Ele permite uma quantidade astronômica de endereços. Além disso, foi projetado com **segurança e mobilidade nativas**, que eram opcionais no I P versão 4. Foi a resposta da questão 17 de 2025.

Pegadinhas da questão 17: o I P versão 4 tem 32 bits, e não 64; e o I P versão 6 não dá apenas quatro vezes mais endereços, dá um número incomparavelmente maior.

**Endereços privados.** Alguns intervalos são reservados para redes internas e não circulam na internet. Os mais conhecidos começam com **10**, com **172 ponto 16 a 172 ponto 31**, e com **192 ponto 168**. O roteador da sua casa provavelmente usa um endereço que começa com 192 ponto 168. Para sair para a internet, esses endereços passam pelo **N A T**, a tradução de endereços, que permite que vários aparelhos da casa usem um único endereço público.

O endereço **127 ponto 0 ponto 0 ponto 1** é o **loopback**, ou localhost: significa o próprio computador.

**Máscara de rede.** Indica qual parte do endereço I P identifica a **rede** e qual parte identifica o **dispositivo** dentro dela. A máscara mais comum em redes domésticas é 255 ponto 255 ponto 255 ponto 0, também escrita como barra 24, que quer dizer que os primeiros 24 bits são da rede.

**Gateway padrão.** É o equipamento, normalmente o **roteador**, por onde os dados saem da rede local para outras redes, como a internet. É a porta de saída da rede.

**D N S.** O **sistema de nomes de domínio** traduz **nomes** em **endereços I P**. Você digita um nome de site, e o D N S descobre qual é o endereço numérico do servidor. É como uma lista telefônica da internet. Sem D N S, teríamos que decorar números.

**D H C P.** O **protocolo de configuração dinâmica** distribui **automaticamente** os endereços I P, a máscara, o gateway e o D N S para os aparelhos que entram na rede. Quando seu celular se conecta ao Wi-Fi e já começa a funcionar, foi o D H C P que configurou tudo.

Para não confundir: **D N S traduz nomes; D H C P distribui endereços.**

---

## Aula 3. Os equipamentos de rede

O edital cita hubs, repetidores, bridges, switches e o gerenciamento por S N M P. Vamos de um por um.

**Repetidor.** Recebe o sinal, **regenera** e retransmite, para ampliar o alcance. Não toma nenhuma decisão sobre os dados. Os repetidores de Wi-Fi da casa são um exemplo.

**Hub.** O concentrador mais simples e antigo. Recebe os dados por uma porta e **repete para todas as outras portas**, para todos os computadores ligados a ele. Isso gera tráfego desnecessário e colisões. É pouco inteligente e quase não se usa mais.

**Bridge, ou ponte.** Liga **dois segmentos** de rede e filtra o tráfego, deixando passar só o que precisa ir para o outro lado.

**Switch, ou comutador.** O concentrador inteligente. Ele **aprende** o endereço físico de cada aparelho ligado a ele, chamado **endereço M A C**, e envia os dados **somente para a porta do destinatário**. É muito mais eficiente e seguro que o hub. É o equipamento central das redes em estrela de hoje.

**Roteador.** Liga **redes diferentes** entre si, como a rede da sua casa e a internet, escolhendo o **melhor caminho** para os dados, com base no **endereço I P**. O switch trabalha dentro da rede local, com o endereço M A C; o roteador trabalha entre redes, com o endereço I P.

**Modem.** Converte o sinal da operadora, que vem pelo cabo, pela fibra ou pelo telefone, em sinal digital para o computador, e vice-versa. Hoje, muitas vezes, o modem e o roteador vêm no mesmo aparelho.

**Ponto de acesso.** O equipamento que cria a rede Wi-Fi, ligando os aparelhos sem fio à rede com fio.

**S N M P.** O **protocolo simples de gerenciamento de rede** serve para **monitorar e gerenciar** os equipamentos da rede: verificar se estão ligados, ver o tráfego, receber alertas de falhas. É usado pelos administradores de rede.

**O endereço M A C.** É o **endereço físico** da placa de rede, gravado de fábrica, com 48 bits, escrito em hexadecimal. Diferente do I P, que pode mudar conforme a rede, o M A C identifica o próprio equipamento.

---

## Aula 4. Os protocolos da internet

Os protocolos da camada de aplicação são as regras usadas pelos programas que você usa todos os dias. A banca cobra a função de cada um, e às vezes a porta padrão. Vou dizer o protocolo, a função e a porta.

**H T T P**, protocolo de transferência de hipertexto: transfere as **páginas da web**. Porta 80. Não é criptografado.

**H T T P S**: é o H T T P **seguro**, com **criptografia**, usando os protocolos T L S, o sucessor do antigo S S L. Porta 443. Aparece o cadeado no navegador. Atenção: o cadeado garante que a conexão é **criptografada**, mas **não garante que o site é honesto**. Sites de phishing também podem ter cadeado.

**F T P**, protocolo de transferência de arquivos: envia e recebe **arquivos** entre computadores. Usa as portas 20, para os dados, e 21, para o controle.

**S M T P**: **envia** e-mails. Porta 25, ou 587 nos envios autenticados.

**P O P 3**: **recebe** e-mails, **baixando** as mensagens para o computador e, em regra, **apagando do servidor**. Porta 110.

**I M A P**: **recebe** e-mails, mas **mantém as mensagens no servidor**, sincronizando entre vários aparelhos. É o que permite ler o mesmo e-mail no celular e no computador. Porta 143.

Para lembrar: **S M T P sobe**, envia; **P O P baixa** e leva para casa; **I M A P mantém** no servidor.

**D N S**: traduz nomes em endereços. Porta 53.

**D H C P**: distribui endereços automaticamente.

**S S H**: **acesso remoto seguro**, criptografado, a outro computador, por linha de comando. Porta 22.

**Telnet**: acesso remoto **sem criptografia**, inseguro, hoje substituído pelo S S H. Porta 23.

**S N M P**: gerenciamento de rede, como você viu na aula anterior.

---

## Aula 5. U R L, domínios, cookies, proxy e o navegador

**U R L** é o **endereço completo** de um recurso na internet. Ela tem partes, e a banca pede para identificá-las. Pense no endereço "https, dois-pontos, barra, barra, w w w ponto policiacivil ponto m g ponto gov ponto br, barra, concursos".

**O protocolo**: https, que diz como acessar.

**O nome do servidor**, ou host: w w w.

**O domínio**: policiacivil ponto m g ponto gov ponto br.

**O caminho**: barra concursos, que indica a página ou o arquivo dentro do site.

**Os domínios.** O final do domínio indica o tipo e o país. Os mais comuns no Brasil: **ponto gov ponto br**, para órgãos de governo; **ponto jus ponto br**, para o Poder Judiciário; **ponto mp ponto br**, para o Ministério Público; **ponto leg ponto br**, para o Poder Legislativo; **ponto edu ponto br**, para instituições de ensino; **ponto org ponto br**, para organizações sem fins lucrativos; e **ponto com ponto br**, para o comércio. O **ponto br** é o domínio do Brasil. Uma dica de segurança: um site que diz ser de um órgão público, mas não termina em gov ponto br, merece desconfiança.

**Cookies.** São **pequenos arquivos de texto** que os sites gravam no seu navegador, para **lembrar informações**: o login, as preferências, os itens do carrinho de compras. Cookies **não são vírus** e não executam programas. Mas podem ser usados para **rastrear** os seus hábitos de navegação, principalmente os cookies de terceiros, usados por anunciantes. Por isso têm a ver com privacidade.

**Proxy.** É um **servidor intermediário** entre o seu computador e a internet. Ele pode **filtrar** o acesso, bloqueando sites proibidos, **guardar cópias** de páginas para acelerar o acesso, o chamado cache, e **esconder** o endereço do usuário. Muitas empresas e órgãos públicos usam proxy para controlar a navegação dos funcionários. A configuração de proxy fica nas configurações de rede do sistema ou do navegador.

**O navegador Google Chrome.** O edital pede o Chrome. Os recursos mais cobrados:

**Navegação anônima**, que no Chrome se chama **janela anônima**: não guarda **no seu computador** o histórico, os cookies e os dados de formulários depois que você fecha a janela. Mas ela **não esconde** a sua navegação do provedor de internet, da empresa onde você trabalha nem dos sites que você visita. E os **downloads** e os **favoritos** criados continuam salvos. Essa é a pegadinha clássica.

**Os atalhos mais cobrados**, com a tecla Control:

Control e T: nova guia.

Control e N: nova janela.

Control, Shift e N: nova janela anônima.

Control e W: fecha a guia atual.

Control, Shift e T: reabre a última guia fechada.

Control e H: histórico.

Control e J: downloads.

Control e D: adiciona a página aos favoritos.

Control e F: procurar uma palavra na página.

Control e mais, e Control e menos: aumentar e diminuir o zoom. Útil para quem tem baixa visão.

F5: recarregar a página.

**Sincronização.** Ao entrar com a conta Google no Chrome, os favoritos, o histórico e as senhas podem ser sincronizados entre os aparelhos.

---

## Aula 6. O Marco Civil da Internet

O edital pede o Marco Civil da Internet, a **Lei 12965, de 2014**. Ela estabelece princípios, garantias, direitos e deveres para o uso da internet no Brasil. Para o investigador, ela é essencial, porque regula a **guarda de registros** que você vai requisitar nas investigações.

**Os princípios.** Entre outros: a **liberdade de expressão**, a **proteção da privacidade** e dos dados pessoais, e a **neutralidade da rede**. Neutralidade quer dizer que o provedor deve tratar **de forma igual** todos os pacotes de dados, sem discriminar por conteúdo, origem, destino ou aplicativo. A operadora não pode, por exemplo, deixar um aplicativo de vídeo mais lento para favorecer outro.

**Os dois tipos de registro.** Esta é a parte mais importante para a investigação.

**Registros de conexão**: o conjunto de informações sobre a **data e a hora de início e de término** de uma conexão à internet, a sua **duração** e o **endereço I P** usado. Quem guarda é o **provedor de conexão**, a operadora que dá o acesso à internet. O prazo é de **um ano**, em sigilo.

**Registros de acesso a aplicações**: as informações sobre a **data e a hora de uso** de uma aplicação, como uma rede social ou um site, a partir de um endereço I P. Quem guarda é o **provedor de aplicação**, como as redes sociais e os sites, quando constituído como pessoa jurídica com fins econômicos. O prazo é de **seis meses**, em sigilo.

Para memorizar: **conexão, um ano; aplicação, seis meses.**

A autoridade policial ou o Ministério Público podem **requerer cautelarmente** que esses registros sejam guardados **por prazo maior**. Mas o **acesso ao conteúdo** dos registros depende de **ordem judicial**.

E o **provedor de conexão** é **proibido** de guardar os registros de acesso a aplicações. Ou seja, a operadora sabe quando você se conectou, mas não pode registrar quais sites você visitou.

**Os dados cadastrais.** Nome, filiação e endereço do usuário podem ser requisitados diretamente pelas autoridades administrativas que tenham competência legal para isso, como o delegado de polícia, **sem ordem judicial**. O conteúdo das comunicações e os registros, não.

**A responsabilidade por conteúdo de terceiros.** Em regra, o provedor de aplicação só pode ser responsabilizado civilmente por conteúdo postado por outra pessoa se, **depois de ordem judicial específica**, não tomar providências para tornar o conteúdo indisponível. Há uma exceção importante: a divulgação, sem autorização, de **imagens, vídeos ou outros materiais com cenas de nudez ou de atos sexuais de caráter privado**. Nesse caso, basta uma **notificação da vítima** ao provedor: se ele não remover, responde subsidiariamente. É a proteção contra a chamada pornografia de vingança.

O Supremo, em 2025, ampliou essas hipóteses de responsabilidade, considerando o artigo 19 parcialmente inconstitucional. Fique atento a como o próximo edital e a banca vão tratar esse ponto.

---

## Revisão do módulo 1 de Informática

Vamos revisar em frases curtas.

L A N é local, M A N é metropolitana, W A N é de longa distância.

Intranet é privada, com as mesmas tecnologias da internet.

Topologia estrela é a mais comum, com um switch no centro.

Cabo: estabilidade, velocidade e segurança. Wi-Fi: mobilidade e flexibilidade.

T C P é confiável; U D P é rápido e sem garantia.

I P versão 4: 32 bits, quatro números de 0 a 255.

I P versão 6: 128 bits, hexadecimal, segurança e mobilidade nativas.

192 ponto 168 é endereço privado; 127 ponto 0 ponto 0 ponto 1 é o próprio computador.

Gateway é a porta de saída da rede.

D N S traduz nomes; D H C P distribui endereços.

Hub repete para todos; switch entrega só ao destinatário; roteador liga redes diferentes.

Switch usa endereço M A C; roteador usa endereço I P.

S N M P gerencia a rede.

H T T P, porta 80; H T T P S, porta 443, com criptografia.

Cadeado não garante que o site é honesto.

S M T P envia; P O P baixa; I M A P mantém no servidor.

S S H é acesso remoto seguro; Telnet é inseguro.

Gov ponto br é governo; jus ponto br é Judiciário.

Cookies não são vírus, mas podem rastrear.

Proxy é intermediário que filtra, guarda cache e esconde o usuário.

Janela anônima não esconde nada do provedor, e downloads e favoritos ficam salvos.

Control, Shift e N abre janela anônima; Control, Shift e T reabre a guia fechada.

Marco Civil: neutralidade da rede.

Registros de conexão: um ano. Registros de aplicação: seis meses.

Conteúdo dos registros só com ordem judicial; dados cadastrais podem ser requisitados pelo delegado.

Nudez não autorizada: basta notificação da vítima.

---

## Treino 1. Redes

Sobre os equipamentos de rede, assinale a afirmativa correta.

Letra A: O hub envia os dados apenas para a porta do computador de destino, com base no endereço M A C.

Letra B: O switch encaminha os dados somente para a porta do destinatário, aprendendo os endereços M A C dos dispositivos conectados.

Letra C: O roteador opera exclusivamente dentro da rede local e não interliga redes distintas.

Letra D: O repetidor analisa o conteúdo dos pacotes e escolhe a melhor rota entre redes.

Letra E: O D H C P é o equipamento que liga a rede local à internet.

Pense na sua resposta.

**A explicação.** O switch aprende os endereços M A C e entrega cada pacote só ao destinatário. O hub repete para todas as portas. O roteador interliga redes diferentes. O repetidor só regenera o sinal. E o D H C P não é equipamento, é um protocolo que distribui endereços.

**Resposta: letra B.**

---

## Treino 2. Protocolos de e-mail

Um investigador acessa o seu e-mail funcional no computador da delegacia e no celular, e quer que as mensagens fiquem guardadas no servidor e apareçam iguais nos dois aparelhos. O protocolo de recebimento mais adequado é o

Letra A: S M T P.

Letra B: P O P 3.

Letra C: I M A P.

Letra D: F T P.

Letra E: S N M P.

Pense na sua resposta.

**A explicação.** O I M A P mantém as mensagens no servidor e sincroniza entre os aparelhos. O P O P 3 baixa as mensagens e, em regra, as apaga do servidor. O S M T P é de envio, o F T P transfere arquivos e o S N M P gerencia redes.

**Resposta: letra C.**

---

## Treino 3. Navegação anônima

Sobre a janela anônima do Google Chrome, assinale a afirmativa correta.

Letra A: Impede que o provedor de internet e o empregador saibam quais sites foram visitados.

Letra B: Apaga automaticamente os arquivos baixados quando a janela é fechada.

Letra C: Não salva, no computador, o histórico de navegação e os cookies depois que a janela é fechada.

Letra D: Impede o acesso a sites que exigem login.

Letra E: Criptografa todos os dados enviados, tornando qualquer site seguro.

Pense na sua resposta.

**A explicação.** A janela anônima só evita que o histórico, os cookies e os dados de formulários fiquem salvos no próprio computador. Ela não esconde a navegação do provedor nem da empresa, não apaga os downloads, não impede logins e não criptografa nada além do que o site já faz.

**Resposta: letra C.**

---

## Treino 4. Marco Civil da Internet

Durante uma investigação de estelionato praticado pela internet, a autoridade policial precisa identificar o endereço I P e o horário da conexão usados pelo suspeito. De acordo com o Marco Civil da Internet, é correto afirmar que

Letra A: os registros de conexão devem ser mantidos pelo provedor de conexão pelo prazo de um ano, e o acesso ao seu conteúdo depende de ordem judicial.

Letra B: os registros de conexão devem ser mantidos pelo prazo de seis meses, e o delegado pode acessá-los diretamente.

Letra C: o provedor de conexão deve guardar também os registros de acesso a aplicações por cinco anos.

Letra D: os registros de conexão não podem ser guardados, em respeito à neutralidade da rede.

Letra E: o acesso aos registros depende apenas de requisição do Ministério Público.

Pense na sua resposta.

**A explicação.** O provedor de conexão guarda os registros de conexão por um ano, em sigilo, e o acesso ao conteúdo depende de ordem judicial. Seis meses é o prazo dos registros de aplicação. O provedor de conexão é proibido de guardar registros de aplicação. E a neutralidade da rede não tem relação com a guarda de registros.

**Resposta: letra A.**

---

## Encerramento do módulo 1 de Informática

Parabéns, você terminou o primeiro módulo de Informática. Repita em voz alta: D N S traduz, D H C P distribui; S M T P sobe, P O P baixa, I M A P mantém; conexão um ano, aplicação seis meses.

No próximo módulo de Informática, vamos estudar a segurança da informação: vírus, cavalo de Troia, worm, ransomware, phishing e pharming, backup, criptografia com chaves pública e privada, certificação digital e a I C P Brasil, assuntos das questões 21, 22 e 23 de 2025.
