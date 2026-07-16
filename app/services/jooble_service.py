import httpx  # httpx is python library used to send http request to another server or APi and it works asynchronous 
from app.config import JOOBLE_API_KEY

async def search_jobs(keyword,location):

    url=f"https://jooble.org/api/{JOOBLE_API_KEY}"

    payload={
        "keywords":keyword,
        "location":location
    }
    try:
        async with httpx.AsyncClient() as client:
            response= await client.post(url,json=payload)
            data=response.json()
        print(data)
        jobs=[]
        for i in data["jobs"]:
            jobs.append({
                "Jobrole":i.get("title"),
                "company":i.get("company"),
                "location":i.get("location"),
                "salary":i.get("salary"),
                "website":i.get("link"),
                "jobtype":i.get("type")
            
        })
        return jobs
      


    except httpx.RequestError as e:
        print("Network Error:", e)
