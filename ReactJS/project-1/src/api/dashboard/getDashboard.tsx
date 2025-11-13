import { useEffect, useState } from "react";


export const getDashboardData = () => {

    const [loading, setLoading] = useState<boolean>(false);
    const [error, setError] = useState();
    const [data, setData] = useState<LCData[]>([]);

    useEffect(() => {
        const getData = async() => {
            let response = axios.get<DashboardApiResponse>("localhost:8080");
        }
        getData();
    }, []);
    return [loading, error]
}