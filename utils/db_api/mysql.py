from typing import Union
from aiomysql.pool import Pool
import aiomysql
from data import config
import logging
import asyncio

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None
        self.loop = loop = asyncio.get_event_loop()



    async def create(self):
        self.pool = await aiomysql.create_pool(
        host=config.DB_HOST,
        port=3306,
        user=config.DB_USER,
        password=config.DB_PASS,
        db=config.DB_NAME ,
        loop=self.loop, 
        autocommit=True
        )
        # self.pool = await aiomysql.create_pool(
        #     user=
        #     password=config.DB_PASS,
        #     host=
        #     db=
        # )


    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
        ):
        # async with self.pool.acquire() as connection:
        #     async with connection.cursor() as cursor:
        
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cursor:
                
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
    
    # -----------------------------
    async def get_all_computer(self):
        sql = f"CALL get_all_computer()"
        return await self.execute(sql, fetch=True)
    
    async def get_all_computer_id(self):
        sql = f"CALL get_all_computer_id();"
        return await self.execute(sql, fetchrow=True)
    
    async def get_computer_id(self, comp_id):
        sql = f"CALL get_computer_id('{comp_id}')"
        return await self.execute(sql, fetchrow=True)
    
    # -----------------------------------------
    async def get_all_smartphone(self):
        sql = f"CALL get_all_smartphone()"
        return await self.execute(sql, fetch=True)
    
    async def get_all_smartphone_id(self):
        sql = f"CALL get_all_smartphone_id();"
        return await self.execute(sql, fetchrow=True)
    
    async def get_smartphone_id(self, comp_id):
        sql = f"CALL get_smartphone_id('{comp_id}')"
        return await self.execute(sql, fetchrow=True)
    
    # -----------------------------------------
    async def get_all_smartwatch(self):
        sql = f"CALL get_all_smarwatche()"
        return await self.execute(sql, fetch=True)
    
    async def get_all_smartwatch_id(self):
        sql = f"CALL get_all_smartwatch_id();"
        return await self.execute(sql, fetchrow=True)
    
    async def get_smartwatch_id(self, comp_id):
        sql = f"CALL get_smartwatch_id('{comp_id}')"
        return await self.execute(sql, fetchrow=True)
    
    # -----------------------------------------
    async def get_all_accessory(self):
        sql = f"CALL get_all_accessory()"
        return await self.execute(sql, fetch=True)
    
    async def get_all_accessory_id(self):
        sql = f"CALL get_all_accessory_id();"
        return await self.execute(sql, fetchrow=True)
    
    async def get_accessory_id(self, comp_id):
        sql = f"CALL get_accessory_id('{comp_id}')"
        return await self.execute(sql, fetchrow=True)
    
    # -----------------------------------------
    async def get_all_otherproducts(self):
        sql = f"CALL get_all_otherproducts()"
        return await self.execute(sql, fetch=True)
    
    async def get_all_accessory_id(self):
        sql = f"CALL get_all_otherproducts_id();"
        return await self.execute(sql, fetchrow=True)
    
    async def get_otherproducts_id(self, comp_id):
        sql = f"CALL get_otherproducts_id('{comp_id}')"
        return await self.execute(sql, fetchrow=True)
    