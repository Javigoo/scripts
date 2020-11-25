function suma(a,b){
    return a+b;
}
console.log(suma(2,2))

var varSuma = function(a,b){
    return a+b;
}
console.log(varSuma(2,3));

const arrowSuma = (a,b) => a+b;
console.log(arrowSuma(2,4))

let sum;
(function(){
    sum=2+5;
})();
console.log(sum)

let sum2;
(function(){
    sum2=2+x;
})(x=6);
console.log(sum2);

(() => console.log(2+7))();

// Pero por qué se pueden crear funciones de tantas maneras @|#¢|@#∞∞¢÷““”≠|å∂∑≤©ƒ√√®€ß