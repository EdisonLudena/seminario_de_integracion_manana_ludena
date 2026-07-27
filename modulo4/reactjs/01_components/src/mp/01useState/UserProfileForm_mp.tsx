import { useState } from 'react'

interface FichaFutbolista {
  nombre: string
  apellido: string
  club: string
  dorsal: number
}

export default function FichaFutbolistaForm() {
  const [ficha, setFicha] = useState<FichaFutbolista>({
    nombre: '',
    apellido: '',
    club: '',
    dorsal: 0,
  })

  function handleChange(field: keyof FichaFutbolista, value: string | number) {
    setFicha((prev) => ({
      ...prev,
      [field]: value,
    }))
  }

  return (
    <form style={{ display: 'flex', flexDirection: 'column', gap: 10, maxWidth: 320 }}>
      <input
        placeholder="Nombre"
        value={ficha.nombre}
        onChange={(e) => handleChange('nombre', e.target.value)}
        style={inputStyle}
      />
      <input
        placeholder="Apellido"
        value={ficha.apellido}
        onChange={(e) => handleChange('apellido', e.target.value)}
        style={inputStyle}
      />
      <input
        placeholder="Club"
        value={ficha.club}
        onChange={(e) => handleChange('club', e.target.value)}
        style={inputStyle}
      />
      <input
        placeholder="Dorsal"
        type="number"
        value={ficha.dorsal}
        onChange={(e) => handleChange('dorsal', Number(e.target.value))}
        style={inputStyle}
      />

      <div style={{ marginTop: 8, padding: 12, background: '#f5f5f5', borderRadius: 6 }}>
        <p style={{ margin: 0, fontSize: 13 }}>
          <strong>{ficha.nombre || '—'} {ficha.apellido || '—'}</strong> · {ficha.club || '—'} · Dorsal: {ficha.dorsal || '—'}
        </p>
      </div>
    </form>
  )
}

const inputStyle = {
  padding: '8px 12px',
  border: '1px solid #ddd',
  borderRadius: 6,
  fontSize: 14,
}
