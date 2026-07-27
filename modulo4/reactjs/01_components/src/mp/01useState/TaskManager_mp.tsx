import { useState } from 'react'

interface JugadorConvocado {
  id: number
  nombre: string
  posicion: string
  confirmado: boolean
}

export default function ConvocatoriaManager() {
  const [jugadores, setJugadores] = useState<JugadorConvocado[]>([])
  const [inputPosicion, setInputPosicion] = useState('')
  const [inputNombre, setInputNombre] = useState('')

  function agregarJugador() {
    if (!inputPosicion.trim()) return
    setJugadores((prev) => [
      ...prev,
      { id: Date.now(), nombre: inputNombre.trim(), posicion: inputPosicion.trim(), confirmado: false },
    ])
    setInputPosicion('')
    setInputNombre('')
  }

  function eliminarJugador(id: number) {
    setJugadores((prev) => prev.filter((j) => j.id !== id))
  }

  function toggleConfirmacion(id: number) {
    setJugadores((prev) =>
      prev.map((j) =>
        j.id === id ? { ...j, confirmado: !j.confirmado } : j
      )
    )
  }

  return (
    <div style={{ maxWidth: 380 }}>
      <div style={{ display: 'flex', gap: 8, marginBottom: 16 }}>
        <input
          value={inputNombre}
          onChange={(e) => setInputNombre(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && agregarJugador()}
          placeholder="Nombre del jugador..."
          style={{ flex: 1, padding: '8px 12px', borderRadius: 6, border: '1px solid #ddd' }}
        />
        <input
          value={inputPosicion}
          onChange={(e) => setInputPosicion(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && agregarJugador()}
          placeholder="Posición..."
          style={{ flex: 1, padding: '8px 12px', borderRadius: 6, border: '1px solid #ddd' }}
        />
        <button
          onClick={agregarJugador}
          style={{ padding: '8px 16px', background: '#0070f3', color: '#fff', border: 'none', borderRadius: 6, cursor: 'pointer' }}
        >
          Convocar
        </button>
      </div>

      {jugadores.length === 0 && (
        <p style={{ color: '#999', fontSize: 14 }}>No hay convocados. ¡Agrega uno!</p>
      )}

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {jugadores.map((j) => (
          <li
            key={j.id}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '10px 0',
              borderBottom: '1px solid #eee',
            }}
          >
            <input
              type="checkbox"
              checked={j.confirmado}
              onChange={() => toggleConfirmacion(j.id)}
            />
            <span
              style={{
                flex: 1,
                textDecoration: j.confirmado ? 'line-through' : 'none',
                color: j.confirmado ? '#aaa' : '#333',
              }}
            >
              {j.nombre}
            </span>
            <span
              style={{
                flex: 1,
                textDecoration: j.confirmado ? 'line-through' : 'none',
                color: j.confirmado ? '#aaa' : '#333',
              }}
            >
              {j.posicion}
            </span>
            <button
              onClick={() => eliminarJugador(j.id)}
              style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#e00', fontSize: 16 }}
            >
              ✕
            </button>
          </li>
        ))}
      </ul>

      {jugadores.length > 0 && (
        <p style={{ fontSize: 13, color: '#888', marginTop: 8 }}>
          {jugadores.filter((j) => j.confirmado).length} de {jugadores.length} confirmados
        </p>
      )}
    </div>
  )
}
