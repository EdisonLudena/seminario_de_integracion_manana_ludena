import { useRef, useState } from 'react'

export default function FichajeRapidoForm() {
  const nombreRef = useRef<HTMLInputElement>(null)
  const posicionRef = useRef<HTMLInputElement>(null)
  const [registroGuardado, setRegistroGuardado] = useState('Ingrese jugador y guarde')

  function guardarRegistro() {
    const nombre = nombreRef.current?.value.trim() ?? ''
    const posicion = posicionRef.current?.value.trim() ?? ''

    const textoNombre = nombre === '' ? '(vacío)' : nombre
    const textoPosicion = posicion === '' ? '(vacío)' : posicion

    setRegistroGuardado(`${textoNombre} | ${textoPosicion}`)
  }

  function limpiarCampos() {
    if (nombreRef.current) nombreRef.current.value = ''
    if (posicionRef.current) posicionRef.current.value = ''
    nombreRef.current?.focus()
  }

  return (
    <div style={{ maxWidth: 340, display: 'flex', flexDirection: 'column', gap: 10 }}>
      <p style={{ margin: 0, color: '#6b7280', fontSize: 13 }}>
        Registro guardado: <strong style={{ color: '#111827' }}>{registroGuardado}</strong>
      </p>

      <input
        ref={nombreRef}
        defaultValue=""
        placeholder="Nombre del futbolista..."
        style={{ padding: '8px 12px', border: '1px solid #d1d5db', borderRadius: 6 }}
      />
      
      <input
        ref={posicionRef}
        defaultValue=""
        placeholder="Posición..."
        style={{ padding: '8px 12px', border: '1px solid #d1d5db', borderRadius: 6 }}
      />

      <div style={{ display: 'flex', gap: 8 }}>
        <button
          onClick={guardarRegistro}
          style={{ flex: 1, padding: '8px', background: '#0070f3', color: '#fff', border: 'none', borderRadius: 6, cursor: 'pointer' }}
        >
          Guardar Registro
        </button>
        <button
          onClick={limpiarCampos}
          style={{ padding: '8px 16px', background: '#f3f4f6', color: '#6b7280', border: 'none', borderRadius: 6, cursor: 'pointer' }}
        >
          Limpiar
        </button>
      </div>
    </div>
  )
}
