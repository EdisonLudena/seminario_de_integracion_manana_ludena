// Concepto puro
type Producto = {
  id: number;
  nombre: string;
  precio: number;
  disponible: boolean;
  existencias: number;
};

const catalogo: Producto[] = [
  { id: 1, nombre: "Laptop",  precio: 999,  disponible: true, existencias: 30},
  { id: 2, nombre: "Mouse",   precio: 25,   disponible: true, existencias: 20 },
  { id: 3, nombre: "Monitor", precio: 350,  disponible: false, existencias: 10 },
  { id: 4, nombre: "Audifonos",   precio: 49,   disponible: false, existencias: 100 },
  { id: 5, nombre: "Parlantes", precio: 1000,  disponible: true, existencias: 65 },
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
console.log(catalogo);
console.log(catalogo[3].existencias);


//incluir existencia, incluir dos elementos al arrat y imprimir el arreglo completo impimir
// la existencia del 4 elementos del array
