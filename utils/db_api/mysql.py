from typing import Union
from aiomysql.pool import Pool
import aiomysql
from data import config


import logging
class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None



    async def create(self):
        self.pool = await aiomysql.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            db=config.DB_NAME
        )




        # async def execute(
        #         self,
        #         command,
        #         *args,
        #         fetch: bool = False,
        #         fetchval: bool = False,
        #         fetchrow: bool = False,
        #         execute: bool = False,
        # ):
        #     async with self.pool.acquire() as connection:
        #         async with connection.cursor() as cursor:
        #             await cursor.execute(command, args)
        #             logging.info(f"func execute : {command}")
        #             print(f"func execute : {command}")
        #             if fetch:
        #                 result = await cursor.fetchall()
        #             elif fetchval:
        #                 result = await cursor.fetchone()
        #             elif fetchrow:
        #                 result = await cursor.fetchone()
        #             elif execute:
        #                 result = cursor.rowcount()
        #
        #             return result
    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
        ):
        async with self.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                logging.info(f"1 : func execute : {command}")
                await cursor.execute(command, args)
                logging.info(f"2 : func execute : {command}")
                if fetch:
                    result = await cursor.fetchall()
                elif fetchval:
                    result = await cursor.fetchone()
                elif fetchrow:
                    result = await cursor.fetchone()
                elif execute:
                    result = cursor.rowcount
                logging.info(f"3 : {result}")
                return result


    async def add_user(self, last_name, first_name, email, phone_num, telegram_id, telegram_username, manzil):
        """
        Bazaga foydalamuvhcilarni bazaga qo'shish
        """
        last_name = last_name.replace("'", "\\'")
        first_name = first_name.replace("'", "\\'")
        manzil = manzil.replace("'", "\\'")
        sql = f"CALL create_user('{last_name}', '{first_name}', '{email}', '{phone_num}', '{telegram_id}', '{telegram_username}', '{manzil}', '0');"
        await self.execute(sql, execute=True)

    async def add_admin(self, telegram_id):
        """
        Foydalanuvchini admin darajasiga ko'tarish
        """
        sql = f"CALL set_admin_user({telegram_id});"

        await self.execute(sql, execute=True)

    async def check_user(self, telegram_id):
        """
        Foydalanuvchi bazada bor yoki yo'qligini tekshirish
        """
        try:
            sql = f"CALL chek_user('{telegram_id}');"
            result = await self.execute(sql, fetchval=True)
            return result[0]

        except Exception as e:
            logging.error(str(e))
            return -1

    async def add_firma(self, f_name):
        sql = f"INSERT INTO products_firma (name) VALUES ('{f_name}');"
        await self.execute(sql, execute=True)