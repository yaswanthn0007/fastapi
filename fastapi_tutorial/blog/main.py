from fastapi import FastAPI
import models
from database import engine
from routers import blog,user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()




