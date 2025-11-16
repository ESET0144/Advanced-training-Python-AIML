interface BaseApiResponse{
    message: string;
    traceId: string;
}

type LCData = { // Line chart data
    name: string,
    uv: number,
    pv:number,
    amt:number
}

interface DashboardApiResponse extends BaseApiResponse{
    data: LCData[];
}

export type {
    LCData,
    DashboardApiResponse
}