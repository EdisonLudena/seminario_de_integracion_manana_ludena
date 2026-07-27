import { useState, useEffect } from 'react'

interface FutbolistaAPI {
  id:       number
  name:     string
  email:    string
  username: string
  company:  ClubAPI
}
interface ClubAPI {
  name:     string
  catchPhrase:    string
  bs: string
}

export default function FetchJugadoresList() {
  const [jugadores, setJugadores] = useState<FutbolistaAPI[] | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false

    async function fetchJugadores() {
      setLoading(true)
      setError(null)

      try {
        const res = await fetch(`https://jsonplaceholder.typicode.com/users`)
        if (!res.ok) throw new Error(`Error HTTP ${res.status}`)

        const data: FutbolistaAPI[] = await res.json()

        if (!cancelled) setJugadores(data)
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : 'Error desconocido')
        }
      } finally {
        if (!cancelled) setLoading(false)
      }
    }

    fetchJugadores()

    return () => { cancelled = true }
  }, [])

  return (
    <div style={{ maxWidth: 360 }}>
      {loading && (
        <p style={{ color: '#6b7280', fontSize: 14 }}>Cargando...</p>
      )}
      {error && (
        <p style={{ color: '#991b1b', fontSize: 14 }}>Error: {error}</p>
      )}
      {jugadores && !loading && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          {jugadores.map((jugador) => (
            <div key={jugador.id} style={{ padding: 14, border: '1px solid #e5e7eb', borderRadius: 8 }}>
              <p style={{ margin: '0 0 4px', fontWeight: 600 }}>{jugador.name}</p>
              <p style={{ margin: '0 0 4px', fontSize: 13, color: '#6b7280' }}>
                Posición/Apodo: @{jugador.username}
              </p>
              <p style={{ margin: 0, fontSize: 13, color: '#6b7280' }}>
                Contacto: {jugador.email}
              </p>
              <p style={{ margin: 0, fontSize: 13, color: '#6b7280' }}>
                Club: {jugador.company.name}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
