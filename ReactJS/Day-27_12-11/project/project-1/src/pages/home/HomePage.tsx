import {useEffect, useState} from 'react'
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

interface BaseApiResponse {
  message: string;
  traceId: string;
}

interface LCData {
  name: string;
  uv: number;
  pv: number;
  amt: number;
}

interface DashboardApiResponse extends BaseApiResponse{
    data: LCData[];
}


export default function HomePage() {

    const [data, setData] = useState<LCData[]>([])


    useEffect(()=>{
        const getData = async() => {
            const response = await axios.get<DashboardApiResponse>("http://localhost:8000");
            setData(response.data.data);
        }
        getData();
    },[]);


  return (
    <div>
      <LineChart
      style={{ width: '100%', maxWidth: '700px', height: '100%', maxHeight: '70vh', aspectRatio: 1.618 }}
      responsive
      data={data}
      margin={{
        top: 5,
        right: 0,
        left: 0,
        bottom: 5,
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis width="auto" />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="pv" stroke="#8884d8" activeDot={{ r: 8 }} />
      <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
    </LineChart>
  );
    </div>
  )
}
