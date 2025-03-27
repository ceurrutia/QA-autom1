console.log("Hola")

let numeros = [23,4,5]
numeros.push(34)
console.log(numeros)

console.log(numeros.sort())

// Multiplicar cada número por 2 usando forEach
numeros.forEach((numero, index) => {
    numeros[index] = numero * 2
})
console.log("Números multiplicados por 2:", numeros)




