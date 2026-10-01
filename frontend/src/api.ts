export async function getStatus() {
  const response = await fetch('/api/status')
  return response.json()
}

export async function startCollector() {
  const response = await fetch('/api/collector/start', {
    method: 'POST',
  })

  return response.json()
}