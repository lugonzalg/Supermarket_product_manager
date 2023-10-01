import asyncio
import aiohttp
from bs4 import BeautifulSoup
import pandas as pd

async def query(client: aiohttp.ClientSession) -> None:
    url = 'https://tienda.mercadona.es/categories/112'
    response = await client.get(url)

    if response.status == 200:
        print(response.text)
        text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        products = soup.find_all('div', class_='product-container')
        
        data = []
        for product in products:
            name = product.find('span', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            data.append({'Product': name, 'Price': price})
            
        df = pd.DataFrame(data)
        print(df)

async def main() -> None:
    async with aiohttp.ClientSession() as client:
        await query(client)
        
if __name__ == "__main__":
    asyncio.run(main())