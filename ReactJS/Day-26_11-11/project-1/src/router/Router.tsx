import React from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Homepage from '../pages/home/Homepage'
import LoginPage from '../pages/login/LoginPage'
import Layout from './Layout'

export default function Router() {
  return (
    <div>
        <BrowserRouter>
            <Routes >
                <Route path="" element={<Layout />}>
                    <Route path="" element= {<Homepage/>}/>
                    <Route path="login" element= {<LoginPage/>}/>
                </Route>
            </Routes>
        
        </BrowserRouter>
    </div>
  )
}
