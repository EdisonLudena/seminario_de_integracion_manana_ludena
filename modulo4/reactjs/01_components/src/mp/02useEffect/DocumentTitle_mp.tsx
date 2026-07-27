import { useEffect } from 'react'

export default function DocumentTitleFutbol() {
  useEffect(() => {
    document.title = 'Futbol Manager - Plantilla'

    return () => {
      document.title = 'Futbol App'
    }
  }, [])

  return (
    <p style={{ fontSize: 14, color: '#6b7280' }}>
      El título de la pestaña cambió al montar este componente.
    </p>
  )
}
