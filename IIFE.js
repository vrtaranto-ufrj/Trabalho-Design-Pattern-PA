/* Não achei uma maneira de usar esse design patter em python, por isso fiz em javascript */

(function() {
    // Todas as variáveis e funções aqui estão no escopo local da IIFE

    // Variável local
    var localVar = "Esta é uma variável local";

    // Função local
    function localFunction() {
        console.log(localVar);
    }

    // Chama a função local
    localFunction();

    // Podemos definir variáveis e funções sem medo de poluir o escopo global
    var anotherLocalVar = "Outra variável local";
    function anotherLocalFunction() {
        console.log(anotherLocalVar);
    }

    anotherLocalFunction();
})(); // A função é invocada imediatamente após ser definida

// Tentando acessar as variáveis e funções fora da IIFE causará erro
console.log(typeof localVar); // undefined
console.log(typeof localFunction); // undefined
console.log(typeof anotherLocalVar); // undefined
console.log(typeof anotherLocalFunction); // undefined
