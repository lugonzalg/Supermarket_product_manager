from sqlalchemy.orm import Session
import asyncio
import aiohttp
from Logger import logger

import params, models, database, crud

models.Base.metadata.create_all(bind=database.engine)

async def aio_get(
        client: aiohttp.ClientSession, 
        url: str, 
        headers: dict, 
        params: dict = None
        ) -> object:
    
    try:
        aio_res = await client.get(url, headers=headers, params=params)
        return aio_res
    except aiohttp.HTTPClientError as err:
        logger.logger.error(f"Error: client side error {err}")
    except aiohttp.HTTPServerError as err:
        logger.logger.error(f"Error: server side error {err}")
    except asyncio.TimeoutError as err:
        logger.logger.error(f"Error: timeout {err}")

def save_categories(db: Session, categories_info: dict) -> None:
    results = categories_info.get("results")
    if results is None or len(results) == 0:
        return None

    for result in results:
        categories = result.get("categories")
        for category in categories:
            db_category = models.Category(
                category = category.get("name"),
                category_id = category.get("id")
            )
            crud.add_category(db, db_category)

async def get_categories(client: aiohttp.ClientSession) -> None:

    url = params.URL_CATEGORIES
    res = await aio_get(client, url, headers=params.BASIC_HEADERS)
    if res is None:
        logger.logger.error("Error: categories fetching failed")
        return None

    db = next(database.get_db())
    categories_info = await res.json()
    save_categories(db, categories_info)
    db.close()


async def main() -> None:
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as client:
        await get_categories(client)
        
if __name__ == "__main__":

    asyncio.run(main())