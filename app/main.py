from dotenv import load_dotenv
from fastapi import FastAPI
from app.services.auth import login, register
from app.services.auth_user import register_user
from app.services.barang import get_barang, create, delete, update
from app.services.orders import get_orders, create_order, update_order

app = FastAPI(
    title="Logistic App",
    description="backend untuk aplikasi logistik barang (pencatatan, pelacakan, dan pengelolaan)",
    version="1.0.0"
)

#default
@app.get("/")
async def health_check():
    return {"status": "ok"}

# auth admin
app.include_router(login.router)
app.include_router(register.router)

# auth user
app.include_router(register_user.router)

# barang
app.include_router(get_barang.router)
app.include_router(create.router)
app.include_router(delete.router)
app.include_router(update.router)

#order
app.include_router(get_orders.router)
app.include_router(create_order.router)
app.include_router(update_order.router)
