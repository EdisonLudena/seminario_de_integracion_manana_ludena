import { useState } from 'react'

export default function ContadorTarjetasSeguro() {
  const [tarjetas, setTarjetas] = useState(0)

  function sacarTarjeta() {
    setTarjetas(tarjetas + 1)
    setTarjetas((prev) => prev + 1)
  }

  function sacarTresTarjetas() {
    setTarjetas(tarjetas + 1)
    setTarjetas(tarjetas + 1)
    setTarjetas(tarjetas + 1)

    setTarjetas((prev) => prev + 1)
    setTarjetas((prev) => prev + 1)
    setTarjetas((prev) => prev + 1)
  }

  return (
    <div>
      <p>Tarjetas: {tarjetas}</p>
      <button onClick={sacarTarjeta}>+1</button>
      <button onClick={sacarTresTarjetas}>+3</button>
    </div>
  )
}
