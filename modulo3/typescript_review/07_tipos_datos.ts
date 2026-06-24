// Concepto puro
const entero: number = 42;
const decimal: number = 3.14;
const negativo: number = -100;
const hexadecimal: number = 0xff;   // 255 en base 16
const binario: number = 0b1010;     // 10 en base 2
const octal: number = 0o17;         // 15 en base 8
const grande: number = 1_000_000;   // _ como separador visual (ES2021)

console.log(hexadecimal); // 255
console.log(binario);     // 10
console.log(grande);      // 1000000

// Constantes especiales de number
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991
console.log(Number.isFinite(1 / 0)); // false (Infinity no es finito)
console.log(Number.isNaN(0 / 0));    // true


// Concepto puro
const simple: string = "Hola TypeScript";
const doble: string = 'También funciona';
const template: string = `Hola ${"mundo"}`; // template literal

const nombre: string = "Ana";
const edad: number = 28;

// Interpolación: embebe expresiones dentro de ${}
const saludo: string = `Hola, ${nombre}. Tienes ${edad} años.`;
const mayoria: string = `Eres ${edad >= 18 ? "mayor" : "menor"} de edad.`;

// Multilínea sin caracteres de escape
const mensaje: string = `
  Línea 1
  Línea 2
  Línea 3
`.trim();

// Métodos comunes (tipados, el editor autocompleta)
console.log("  hola  ".trim());         // "hola"
console.log("hola".toUpperCase());      // "HOLA"
console.log("2024-06-15".split("-"));   // ["2024", "06", "15"]
console.log("error: fallo".includes("error")); // true
console.log("archivo.ts".endsWith(".ts"));     // true


// Concepto puro
const activo: boolean = true;
const eliminado: boolean = false;

// Se infiere sin anotación explícita
const esMayor = 25 >= 18;    // boolean inferido → true
const tieneStock = 0 > 0;    // boolean inferido → false

// Valores "falsy" en TypeScript/JavaScript (importantes para narrowing)
// false, 0, "", null, undefined, NaN → todos se comportan como false en un if
if (!tieneStock) {
  console.log("Sin stock disponible");
}


// Concepto puro
let sinAsignar: undefined = undefined;
let sinValor: null = null;

// En la práctica: propiedades opcionales o resultados de búsqueda
function buscarUsuario(id: number): string | null {
  if (id === 1) return "Ana";
  return null; // encontrado = null cuando no existe
}

const usuario = buscarUsuario(5);

// Operador de coalescencia nula ?? (devuelve el lado derecho si el izquierdo es null/undefined)
const nombreUsuario = usuario ?? "Invitado";
console.log(nombre); // "Invitado"

// Encadenamiento opcional ?. (no lanza error si algo es null/undefined)
const longitud = usuario?.length;
console.log(longitud); // undefined (no lanza error)


// Concepto puro — dos sintaxis equivalentes
const numeros: number[] = [1, 2, 3, 4, 5];
const textos: Array<string> = ["a", "b", "c"];   // forma genérica

// TypeScript infiere el tipo del array si lo inicializas
const inferido = [10, 20, 30]; // number[] inferido

// Métodos tipados: el compilador conoce el tipo del elemento
const dobles: number[] = numeros.map((n) => n * 2);       // [2, 4, 6, 8, 10]
const pares: number[] = numeros.filter((n) => n % 2 === 0); // [2, 4]
const suma: number = numeros.reduce((acc, n) => acc + n, 0); // 15

// Mutación (cambia el array original)
numeros.push(6);       // agrega al final
numeros.unshift(0);    // agrega al inicio
const ultimo = numeros.pop();   // elimina y devuelve el último
const primero = numeros.shift(); // elimina y devuelve el primero

// Búsqueda
const existe: boolean = numeros.includes(3);       // true
const indice: number = numeros.indexOf(3);         // posición o -1
const encontrado: number | undefined = numeros.find((n) => n > 4); // 5

// Concepto puro
type Producto = {
  id: number;
  nombre: string;
  precio: number;
  disponible: boolean;
};

const catalogo: Producto[] = [
  { id: 1, nombre: "Laptop",  precio: 999,  disponible: true },
  { id: 2, nombre: "Mouse",   precio: 25,   disponible: true },
  { id: 3, nombre: "Monitor", precio: 350,  disponible: false },
];

// TypeScript sabe que cada "p" es de tipo Producto
const disponibles: Producto[] = catalogo.filter((p) => p.disponible);
const nombres: string[] = catalogo.map((p) => p.nombre);
const masBarato: Producto | undefined = catalogo.reduce((min, p) =>
  p.precio < min.precio ? p : min
);

console.log(nombres);                  // ["Laptop", "Mouse", "Monitor"]
console.log(masBarato?.nombre);       // "Mouse"
console.log(disponibles.length);      // 2

// Concepto puro
type Coordenada = [number, number];           // [x, y]
type RGB = [number, number, number];          // [rojo, verde, azul]
type Entrada = [string, number];              // [clave, valor]

const punto: Coordenada = [10.5, -3.2];
const color: RGB = [255, 128, 0];            // naranja
const par: Entrada = ["temperatura", 36.6];

// Desestructuración (la forma más cómoda de usar tuplas)
const [x, y] = punto;
const [rojo, verde, azul] = color;
const [clave, valor] = par;

console.log(`Punto: x=${x}, y=${y}`);         // Punto: x=10.5, y=-3.2
console.log(`Color: rgb(${rojo},${verde},${azul})`); // Color: rgb(255,128,0)

// Tuplas con nombre (TS 4.0+) — mejoran la legibilidad
type Rango = [inicio: number, fin: number];
const horario: Rango = [9, 18];              // de 9:00 a 18:00