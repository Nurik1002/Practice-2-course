from typing import Union
from aiomysql.pool import Pool

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await aiomysql.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result
        
    
    def add_user(self, last_name, first_name, email, phone_num, telegram_id, telegram_username, manzil):
        """
        Bazaga foydalamuvhcilarni bazaga qo'shish
        """
        sql = f"DECLARE out INT; CALL create_user('{last_name}', '{first_name}', '{email}', '{phone_num}', '{telegram_id}', '{telegram_username}', '{manzil}', out); SELECT out;"
        
        await self.execute(sql, execute=True)

        
    
    def add_admin(self, telegram_id):
        """
        Foydalanuvchini admin darajasiga ko'tarish
        """
        sql = f"CALL set_admin_user({telegram_id})"

        await self.execute(sql, execute=True)

    
    
        