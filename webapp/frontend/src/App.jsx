import React, { useState, useEffect } from 'react'

export default function App() {
  const [items, setItems] = useState([])
  const [form, setForm] = useState({ name: '', value: '' })

  const fetchData = async () => {
    const res = await fetch('/api/data')
    const data = await res.json()
    setItems(data)
  }

  useEffect(() => {
    fetchData()
  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault()
    await fetch('/api/data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: form.name, value: parseFloat(form.value) })
    })
    setForm({ name: '', value: '' })
    fetchData()
  }

  return (
    <div style={{ padding: '2rem' }}>
      <h1>FastAPI + React Demo</h1>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Name"
          value={form.name}
          onChange={e => setForm({ ...form, name: e.target.value })}
        />
        <input
          placeholder="Value"
          type="number"
          value={form.value}
          onChange={e => setForm({ ...form, value: e.target.value })}
        />
        <button type="submit">Add</button>
      </form>
      <ul>
        {items.map((item, idx) => (
          <li key={idx}>{item.name}: {item.value}</li>
        ))}
      </ul>
    </div>
  )
}
