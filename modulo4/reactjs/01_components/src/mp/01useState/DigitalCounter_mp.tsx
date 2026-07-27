import { useState } from 'react'

interface MarcadorGolesProps {
  initialValue?: number
  step?: number
  label?: string
}

export default function MarcadorGoles({
  initialValue = 0,
  step = 1,
  label = 'Goles',
}: MarcadorGolesProps) {
  const [goles, setGoles] = useState(initialValue)

  function anotarGol() {
    setGoles(goles + step)
  }

  function anularGol() {
    setGoles(goles - step)
  }

  function reiniciarMarcador() {
    setGoles(initialValue)
  }

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
      <span style={{ fontSize: 14, color: '#666' }}>{label}</span>
      <button onClick={anularGol} style={btnStyle}>−</button>
      <span style={{ fontSize: 20, fontWeight: 600, minWidth: 40, textAlign: 'center' }}>
        {goles}
      </span>
      <button onClick={anotarGol} style={btnStyle}>+</button>
      <button onClick={reiniciarMarcador} style={{ ...btnStyle, fontSize: 12, color: '#999' }}>
        Reset
      </button>
    </div>
  )
}

const btnStyle = {
  width: 32,
  height: 32,
  borderRadius: 6,
  border: '1px solid #ddd',
  background: '#f5f5f5',
  cursor: 'pointer',
  fontSize: 16,
}
