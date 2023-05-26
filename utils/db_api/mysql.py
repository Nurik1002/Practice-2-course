from typing import Union
from aiomysql.pool import Pool
import aiomysql
from data import config

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

    async def add_user(self, last_name, first_name, email, phone_num, telegram_id, telegram_username, manzil):
        """
        Bazaga foydalamuvhcilarni bazaga qo'shish
        """
        sql = f"DECLARE out INT; CALL create_user('{last_name}', '{first_name}', '{email}', '{phone_num}', '{telegram_id}', '{telegram_username}', '{manzil}', out); SELECT out;"

        await self.execute(sql, execute=True)

    async def add_admin(self, telegram_id):
        """
        Foydalanuvchini admin darajasiga ko'tarish
        """
        sql = f"CALL set_admin_user({telegram_id});"

        await self.execute(sql, execute=True)

    async def chek_user(self, telegram_id):
        """
        Foydalanuvchi bazada bor yoki yo'qligini tekshirish
        """
        sql = f"CALL chek_user({telegram_id});"
        #sql = f"SELECT id FROM products_users WHERE telegram_id = '{telegram_id}'"
        result = await self.execute(sql, fetchval=True)
        return result