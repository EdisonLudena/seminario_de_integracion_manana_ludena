import { useRef, useState } from 'react'

export default function EditorTactica() {
  const tacticaRef = useRef<HTMLInputElement>(null)
  const [tacticaGuardada, setTacticaGuardada] = useState('Escribe esquema táctico y guarda')

  function guardarTactica() {
    const valor = tacticaRef.current?.value ?? ''
    setTacticaGuardada(valor.trim() === '' ? '(vacío)' : valor)
  }

  function limpiarTactica() {
    if (tacticaRef.current) {
      tacticaRef.current.value = ''
      tacticaRef.current.focus()
    }
  }

  return (
    <div style={{ maxWidth: 340, display: 'flex', flexDirection: 'column', gap: 10 }}>
      <p style={{ margin: 0, color: '#6b7280', fontSize: 13 }}>
        Táctica guardada: <strong style={{ color: '#111827' }}>{tacticaGuardada}</strong>
      </p>

      <input
        ref={tacticaRef}
        defaultValue=""
        placeholder="Escribe esquema (ej. 4-3-3)..."
        style={{ padding: '8px 12px', border: '1px solid #d1d5db', borderRadius: 6 }}
      />

      <div style={{ display: 'flex', gap: 8 }}>
        <button
          onClick={guardarTactica}
          style={{ flex: 1, padding: '8px', background: '#0070f3', color: '#fff', border: 'none', borderRadius: 6, cursor: 'pointer' }}
        >
          Guardar
        </button>
        <button
          onClick={limpiarTactica}
          style={{ padding: '8px 16px', background: '#f3f4f6', color: '#6b7280', border: 'none', borderRadius: 6, cursor: 'pointer' }}
        >
          Limpiar
        </button>
      </div>
    </div>
  )
}
