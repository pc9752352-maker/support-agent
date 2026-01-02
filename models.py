from pydantic import BaseModel,Field         #pydantic model is used        #field is a method

class TicketCreate(BaseModel):
    title: str = Field(...,min_length=5,max_length=100)                  #field
    description:str=Field(...,min_length=5,max_length=1000)              #field
    
class Ticket(TicketCreate):                #inherited ticketcreat
        id:int                                                  
        ai_reply: str   |None = None
         
        