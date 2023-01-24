// Vamos para o Hello World! */

console.log("Hello World!");

// Mas tem uma coisa errada com esse código. Qual é? 

// Exatamente, esse é um Hello World chato, se eu quisesse ver letrinha no terminal
// Eu ia passar raiva no C, e não estava no JavaScript

document.write("Hello World!");

// Agora ta melhor, mas ainda tem um problema, qual é? 
// Isso mesmo, ainda tá chato. Vamos melhor ainda mais esse hello world.

// Pega a tag do body
pagina = document.getElementsByTagName("body")[0]

// Cria um novo elemento de "h1"
texto = document.createElement("h1");

// Troca a cor para azul escuro
texto.style.color = "darkblue";

texto.style.fontWeight = "bold";

texto.style.fontStyle = "italic";

texto.style.textDecoration = "underline";

pagina.style.color = "orange";

pagina.appendChild(texto);

// Esse código é simples, mas nos próximos slides eu quero mostrar o quão genial ele realmente é.
// Pra isso, temos que ir numa máquina do tempo para 1991, quando o primeiro site do mundo foi lançado
// (Aqui explica como a partir daqui foi criado o HTML, que era apenas páginas com documentos linkados entre si, sem muita interação ou estilo)
// http://info.cern.ch/hypertext/WWW/TheProject.html


// (Falar da origem do CSS, falando que deixa mais bonito)

// E o JS traz todas essas API's juntas, e ainda colocam um lógica no site!
// Isso é genial
// React é a prova viva disso! 




// Agora sim, bem melhor.
// E com isso eu acabei de mostrar pra vocês exatamente para que o javascript foi criado
// E para o que exatamente? Fazer uma página horrível? Claro que não. 

// Antigamente, antes do javascript existir, bem nos primórdios da internet, 
// A maneira como a gente criava sites era simples: escrevia o conteúdo (html) o estilo (css)
// e o site estava pronto, ele iria ficar assim pra sempre, nunca mudaria, ou seja, era estático (só um documento html)
// esse hello world que a gente fez é um pequeno exemplo do próposito do javascript: transformar sites em coisas dinâmicas, que mudam e interagem
// e isso é só o começo, porque criar novos elementos em tela é só o mínimo que o js consegue fazer. 

