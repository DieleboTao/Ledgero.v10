import React from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import UploadReceipt from './pages/UploadReceipt'
import Transactions from './pages/Transactions'
import Reports from './pages/Reports'

export default function App(){
  return (
    <BrowserRouter>
      <div style={{padding:20,fontFamily:'Arial, sans-serif'}}>
        <h1>Ledgero (Demo)</h1>
        <nav style={{marginBottom:10}}>
          <Link to='/'>Upload Receipt</Link> | <Link to='/txs'>Transactions</Link> | <Link to='/reports'>Reports</Link>
        </nav>
        <Routes>
          <Route path='/' element={<UploadReceipt />} />
          <Route path='/txs' element={<Transactions />} />
          <Route path='/reports' element={<Reports />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}
