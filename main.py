from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

@app.get("/customers")
async def get_customers():
    url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")
    
    customers = [
        {
            "id": int(index + 1), 
            "name": customer["name"], 
            "username": customer["username"], 
            "address": customer["address"], 
            "profile": customer["profile"], 
            "company": customer["company"] 
        } for index, customer in enumerate(response.json())
    ]
    return customers

@app.get("/customers/{customer_id}")
async def get_customers_with_id(customer_id: int):
    url = f"https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/{customer_id}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Customer not found")
    
    customer = response.json()
    for customers in customer:
        customers = [
            {
                "id": customer["id"],
                "name": customer["name"],
                "username": customer["username"],
                "address": customer["address"],
                "profile": customer["profile"],
                "company": customer["company"]
            }
        ]
    return customers

@app.get("/products")
async def get_products():
    url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/products"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch data")
        
        # Filter the product information
        products = [{"id": int(index + 1),"name": product["name"], "details": product["details"], "stock": product["stock"]} for index, product in enumerate(response.json())]
        return products


    
