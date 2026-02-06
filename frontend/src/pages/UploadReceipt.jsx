import React, { useState } from 'react';
import axios from 'axios';

export default function UploadReceipt(){
  const [file, setFile] = useState(null);
  const [msg, setMsg] = useState('');
  async function onSubmit(e){
    e.preventDefault();
    if(!file) return setMsg('Pick a file');
    const form = new FormData();
    form.append('file', file);
    try{
      const res = await axios.post((import.meta.env.VITE_API_BASE||'http://localhost:8000') + '/api/receipts/', form, { headers: {'Content-Type':'multipart/form-data'} });
      setMsg('Uploaded id: ' + res.data.id);
    }catch(err){
      setMsg('Upload failed: ' + (err.response?.data || err.message));
    }
  }
  return (
    <div>
      <h2>Upload Receipt</h2>
      <form onSubmit={onSubmit}>
        <input type='file' onChange={(e)=>setFile(e.target.files[0])} />
        <button type='submit'>Upload</button>
      </form>
      <p>{msg}</p>
    </div>
  )
}
