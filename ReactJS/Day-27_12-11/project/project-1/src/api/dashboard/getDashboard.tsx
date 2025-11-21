// import axios from "axios";
// import { useEffect, useState } from "react"
// interface BaseApiResponse {
//   message: string;
//   traceId: string;
// }

// interface LCData {
//   name: string;
//   uv: number;
//   pv: number;
//   amt: number;
// }

// interface DashboardApiResponse extends BaseApiResponse{
//     data: LCData[];
// }

// export const getDashboardData = () => {
//     const [loading, setLoading] = useState<boolean>(false);
//     const [error, setError] = useState();
//     const [data, setData] = useState<LCData[]>([]);

//     useEffect(()=>{
//         const getData = async() => {
//             let response = await axios.get<DashboardApiResponse>("http://localhost:8080");
//         }

//         getData();
//     },[]);

//     return [loading, error, data]
// }