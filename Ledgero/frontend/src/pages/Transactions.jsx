import React, {useEffect, useState} from 'react';
import axios from 'axios';

export default function Transactions(){
  const [txs,setTxs]=useState([]);
  useEffect(()=>{ fetchTxs(); },[]);
  async function fetchTxs(){
    const res = await axios.get((import.meta.env.VITE_API_BASE||'http://localhost:8000') + '/api/transactions/');
    setTxs(res.data);
  }
  return (
    <div>
      <h2>Transactions</h2>
      <ul>
        {txs.map(t=> <li key={t.id}>{t.type} — R{t.amount} — {t.description}</li>)}
      </ul>
    </div>
  )
}
