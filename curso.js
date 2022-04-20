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

// Agora sim, bem melhor.
// E com isso eu acabei de mostrar pra vocês exatamente para que o javascript foi criado
// E para o que exatamente? Fazer uma página horrível? Claro que não. 

// Antigamente, antes do javascript existir, bem nos primórdios da internet, 
// A maneira como a gente criava sites era simples: escrevia o conteúdo (html) o estilo (css)
// e o site estava pronto, ele iria ficar assim pra sempre, nunca mudaria, ou seja, era estático (só um documento html)
// esse hello world que a gente fez é um pequeno exemplo do próposito do javascript: transformar sites em coisas dinâmicas, que mudam e interagem
// e isso é só o começo, porque criar novos elementos em tela é só o mínimo que o js consegue fazer. 

