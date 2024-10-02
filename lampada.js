function verificarLampada(tempoLigada) {
    if (tempoLigada > 0) {
        if (tempoLigada < 5) {
            return "quente";
        } else {
            return "muito quente";
        }
    }
    return "fria";
}


let interruptor1 = false;
let interruptor2 = false;
let interruptor3 = false;


let tempoLigado1 = 0;
let tempoLigado2 = 0;


interruptor1 = true;
tempoLigado1 = 3; 
console.log("Interruptor 1 ligado por 3 minutos.");

interruptor1 = false;
interruptor2 = true;
tempoLigado2 = 1; 
console.log("Interruptor 1 desligado e Interruptor 2 ligado por 1 minuto.");

let lampada1Estado = verificarLampada(tempoLigado1); 
let lampada2Estado = "acesa"; 
let lampada3Estado = "fria"; 

console.log("Resultados:");
console.log(`Lâmpada 1 está ${lampada1Estado} (controlada pelo interruptor 1)`);
console.log(`Lâmpada 2 está ${lampada2Estado} (controlada pelo interruptor 2)`);
console.log(`Lâmpada 3 está ${lampada3Estado} (controlada pelo interruptor 3)`);