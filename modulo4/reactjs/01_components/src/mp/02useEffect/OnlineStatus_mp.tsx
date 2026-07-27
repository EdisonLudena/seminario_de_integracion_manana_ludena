import { useState, useEffect } from 'react'

export default function VarStatusTracker() {
  const [isVarActive, setIsVarActive] = useState(navigator.onLine)

  useEffect(() => {
    function handleOnline()  { setIsVarActive(true)  }
    function handleOffline() { setIsVarActive(false) }

    window.addEventListener('online',  handleOnline)
    window.addEventListener('offline', handleOffline)

    return () => {
      window.removeEventListener('online',  handleOnline)
      window.removeEventListener('offline', handleOffline)
    }
  }, [])

  return (
    <p style={{ color: isVarActive ? '#166534' : '#991b1b', fontWeight: 500 }}>
      {isVarActive ? '🟢 VAR Activo y Conectado' : '🔴 VAR Inactivo (Sin conexión)'}
    </p>
  )
}
