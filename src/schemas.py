from pydantic import BaseModel


class WebsiteBase(BaseModel):
    title: str
    url: str
    xpath: str

class WebsiteCreate(WebsiteBase):
    pass

class Website(WebsiteBase):
    id: int
    price: float | None = None
    
    class Config:
        orm_mode = True