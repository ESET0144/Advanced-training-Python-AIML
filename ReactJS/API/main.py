from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["http://localhost:5173",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True, # Allow cookies and authorization headers
    allow_methods=["*"],    # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],    # Allow all headers
)
@app.get("/")
async def read_root():
    return {
        "message": "data was extracted successfully",
        "traceId":"oa98x3nxrm38h",
        "data":[
  {
    "name": 'Page A',
    "uv": 4000,
    "pv": 2400,
    "amt": 2400,
  },
  {
    "name": 'Page B',
    "uv": 3000,
    "pv": 1398,
    "amt": 2210,
  },
  {
    "name": 'Page C',
    "uv": 2000,
    "pv": 9800,
    "amt": 2290,
  },
  {
    'name': 'Page D',
    'uv': 2780,
    'pv': 3908,
    'amt': 2000,
  },
  {
    'name': 'Page E',
    'uv': 1890,
    'pv': 4800,
    'amt': 2181,
  },
  {
    'name': 'Page F',
    'uv': 2390,
    'pv': 3800,
    'amt': 2500,
  },
  {
    'name': 'Page G',
    'uv': 3490,
    'pv': 4300,
    'amt': 2100,
  },
]
        }

 