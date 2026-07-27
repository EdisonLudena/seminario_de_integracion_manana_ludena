// Union de literales: más simple, cero código JS generado
type Estado = "pendiente" | "procesando" | "completado" | "error";
type Prioridad = "baja" | "media" | "alta";

function procesarPedido(id: number, estado: Estado): void {
  console.log(`Pedido #${id}: ${estado}`);
}

procesarPedido(1, "procesando"); // ok
// procesarPedido(2, "cancelado"); // Error de compilación: no es un Estado válido